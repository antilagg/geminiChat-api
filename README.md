# gemini api

simple flask wrapper for google gemini originally made for my project switched to deepseek and decided to share it

## installation

```
pip install flask curl-cffi
```

## usage

1. run the server:

```
python gemini.py
```

2. send a request:

```
curl -X POST http://localhost:5000/api/gemini \
  -H "Content-Type: application/json" \
  -d '{"prompt":"your question here"}'
```

## api endpoints

- `POST /api/gemini` - send a prompt to gemini
  - request body: `{"prompt":"your question"}`
  - response: `{"deepthoughts":"gemini's response"}`
  - error: `{"err":"error message"}` or `{"wtf":"exception message"}`

server runs on `http://localhost:5000` by default
