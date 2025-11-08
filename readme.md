# Composio-Revved

A simple Python script to interact with **Composio Docs Chat API** and stream responses.

## Install
```bash
pip install requests gradio
```

## Usage

### Basic Script (`app.py`)
```python
import requests, json

url = "https://docs.composio.dev/api/fern-docs/search/v2/chat"
headers = {}

payload = {
    "filters": [],
    "documentUrls": [],
    "messages": [{"role": "user", "parts": [{"type": "text", "text": "Hi"}]}],
    "trigger": "submit-user-message"
}

response = requests.post(url, headers=headers, json=payload)

for line in response.text.split('\n'):
    if line.startswith('data: '):
        try:
            data = json.loads(line[6:])
            if data.get('type') == 'text-delta':
                print(data.get('delta', ''), end='')
        except:
            pass
```

Run with:
```bash
python app.py
```

## Optional: Gradio UI

For a ChatGPT-like interface, use `gradio_app.py`:

```bash
python gradio_app.py
```

## Files
- `app.py` - Basic command-line script
- `gradio_app.py` - Web-based chat interface

## Built Using
Composio Docs API
