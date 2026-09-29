import axios from "axios";
import { API_BASE_URL } from "../config";

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000, // prevent hanging requests
});

export const analyzeBug = async (data) => {
  try {

    console.log("Sending bug report to API:", data);

    const response = await api.post("/check-defect", data);

    console.log("API response:", response.data);

    return response.data;

  } catch (error) {

    console.error("API request failed:", error);

    if (error.response) {
      throw new Error(error.response.data.detail || "Server error");
    }

    throw new Error("Unable to connect to backend API");
  }
};