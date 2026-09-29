import importlib.util
import types
import os
import sys
from types import SimpleNamespace

# ensure project root is on sys.path so relative imports like `ai.*` resolve
sys.path.insert(0, os.path.abspath('.'))

service_path = os.path.abspath(os.path.join('api-backend','services','defect_service.py'))
spec = importlib.util.spec_from_file_location('local_defect_service', service_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

req = SimpleNamespace(title='App crashes on save', description='When saving a file with special characters the app crashes with exit code 1.', steps='1. Open app\n2. Create new file\n3. Paste special chars\n4. Click Save', environment='Windows 10, App v1.2.3')

try:
    result = module.analyze_bug(req)
    print('TYPE', type(result))
    print('REPR', repr(result))
except Exception as e:
    import traceback
    traceback.print_exc()
