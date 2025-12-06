# Backend (FastAPI)

Run:
```
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Endpoints:
- `POST /upload/document` : upload ID document
- `POST /upload/photo` : upload selfie
- `GET /status/{file_id}` : check processing status
