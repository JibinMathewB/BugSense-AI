from pathlib import Path

import numpy as np
import onnxruntime as ort
from huggingface_hub import hf_hub_download
from transformers import AutoTokenizer


class EmbeddingEngine:
    """
    Generates MiniLM embeddings using the quantized ONNX model.

    Optimized for low-memory CPU environments such as Render.
    """

    MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
    MODEL_FILE = "onnx/model_quint8_avx2.onnx"
    MAX_LENGTH = 64

    def __init__(self, model_name: str = MODEL_NAME):
        self.model_name = model_name

        # Download/load tokenizer automatically.
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name
        )

        # Download the quantized ONNX model automatically
        # if it is not already available in the Hugging Face cache.
        self.model_path = hf_hub_download(
            repo_id=model_name,
            filename=self.MODEL_FILE,
        )

        session_options = ort.SessionOptions()

        session_options.graph_optimization_level = (
            ort.GraphOptimizationLevel.ORT_ENABLE_BASIC
        )

        # Reduce memory usage.
        session_options.enable_cpu_mem_arena = False
        session_options.enable_mem_pattern = False

        # Keep CPU usage controlled.
        session_options.intra_op_num_threads = 1
        session_options.inter_op_num_threads = 1

        self.session = ort.InferenceSession(
            str(self.model_path),
            sess_options=session_options,
            providers=["CPUExecutionProvider"],
        )

    def _mean_pooling(
        self,
        token_embeddings: np.ndarray,
        attention_mask: np.ndarray,
    ) -> np.ndarray:
        mask = attention_mask[..., np.newaxis].astype(
            np.float32
        )

        summed = np.sum(
            token_embeddings * mask,
            axis=1,
        )

        counts = np.clip(
            np.sum(mask, axis=1),
            a_min=1e-9,
            a_max=None,
        )

        return summed / counts

    def _normalize(
        self,
        embeddings: np.ndarray,
    ) -> np.ndarray:
        norms = np.linalg.norm(
            embeddings,
            axis=1,
            keepdims=True,
        )

        return embeddings / np.clip(
            norms,
            a_min=1e-12,
            a_max=None,
        )

    def encode_texts(
        self,
        texts: list[str],
        batch_size: int = 1,
    ) -> np.ndarray:

        if not texts:
            raise ValueError(
                "Input text list is empty."
            )

        all_embeddings = []

        for start in range(
            0,
            len(texts),
            batch_size,
        ):
            batch = texts[
                start:start + batch_size
            ]

            encoded = self.tokenizer(
                batch,
                padding=True,
                truncation=True,
                max_length=self.MAX_LENGTH,
                return_tensors="np",
            )

            inputs = {
                "input_ids": encoded[
                    "input_ids"
                ].astype(np.int64),

                "attention_mask": encoded[
                    "attention_mask"
                ].astype(np.int64),

                "token_type_ids": encoded.get(
                    "token_type_ids",
                    np.zeros_like(
                        encoded["input_ids"]
                    ),
                ).astype(np.int64),
            }

            outputs = self.session.run(
                ["last_hidden_state"],
                inputs,
            )

            token_embeddings = outputs[0]

            embeddings = self._mean_pooling(
                token_embeddings,
                inputs["attention_mask"],
            )

            embeddings = self._normalize(
                embeddings
            )

            all_embeddings.append(
                embeddings.astype(
                    np.float32
                )
            )

        return np.vstack(
            all_embeddings
        )

    def encode_query(
        self,
        text: str,
    ) -> np.ndarray:

        if (
            not isinstance(text, str)
            or not text.strip()
        ):
            raise ValueError(
                "Query text cannot be empty."
            )

        return self.encode_texts(
            [text],
            batch_size=1,
        )[0]