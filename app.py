import requests

url = "https://docs.composio.dev/api/fern-docs/search/v2/chat"

headers = {
}

payload = {
    "filters": [],
    "documentUrls": [],
    "messages": [
        {
            "role": "user",
            "parts": [
                {
                    "type": "text",
                    "text": "Hi"
                }
            ],
        }
    ],
    "trigger": "submit-user-message"
}

response = requests.post(url, headers=headers, json=payload)

import json
for line in response.text.split('\n'):
    if line.startswith('data: '):
        try:
            data = json.loads(line[6:]) 
            if data.get('type') == 'text-delta':
                print(data.get('delta', ''), end='')
        except:
            pass
