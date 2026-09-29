import json
import urllib.request
import urllib.error

url = 'http://127.0.0.1:8000/check-defect'
body = {
    'title': 'App crashes on save',
    'description': 'When saving a file with special characters the app crashes with exit code 1.',
    'steps': '1. Open app\n2. Create new file\n3. Paste special chars\n4. Click Save',
    'environment': 'Windows 10, App v1.2.3'
}
req = urllib.request.Request(url, data=json.dumps(body).encode('utf-8'), headers={'Content-Type': 'application/json'}, method='POST')
try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = resp.read().decode('utf-8')
        print('STATUS', resp.status)
        print('BODY')
        print(data)
except urllib.error.HTTPError as e:
    print('HTTP ERROR', e.code)
    try:
        print(e.read().decode('utf-8'))
    except Exception:
        pass
except Exception as ex:
    print('REQUEST FAILED')
    print(str(ex))
