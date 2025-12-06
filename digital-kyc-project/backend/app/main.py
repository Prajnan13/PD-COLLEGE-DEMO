from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn
import uuid, os, asyncio, datetime

app = FastAPI(title="Digital KYC Backend")

STORAGE_DIR = os.environ.get("STORAGE_DIR", "/tmp/digital_kyc_storage")
os.makedirs(STORAGE_DIR, exist_ok=True)

class UploadResponse(BaseModel):
    id: str
    status: str
    message: str

@app.get("/")
async def root():
    return {"service": "digital-kyc-backend", "time": datetime.datetime.utcnow().isoformat()}

@app.post("/upload/document", response_model=UploadResponse)
async def upload_document(user_id: str, doc_type: str, file: UploadFile = File(...)):
    # Save file locally (dev)
    file_id = str(uuid.uuid4())
    filename = f"{file_id}_{file.filename}"
    path = os.path.join(STORAGE_DIR, filename)
    with open(path, "wb") as f:
        content = await file.read()
        f.write(content)
    # Enqueue job to process (placeholder)
    # In production, you would push message to queue (RabbitMQ/Kafka)
    # Here we simulate async processing
    asyncio.create_task(simulate_processing(file_id, user_id, doc_type, path))
    return UploadResponse(id=file_id, status="queued", message="Document uploaded and queued for processing")

async def simulate_processing(file_id, user_id, doc_type, path):
    # Placeholder: simulate OCR/validation delay
    await asyncio.sleep(2)
    # Create a result file
    result_path = os.path.join(STORAGE_DIR, f"{file_id}_result.json")
    import json
    res = {"file_id": file_id, "user_id": user_id, "doc_type": doc_type, "status": "processed", "confidence": 0.95}
    with open(result_path, "w") as f:
        f.write(json.dumps(res))

@app.post("/upload/photo", response_model=UploadResponse)
async def upload_photo(user_id: str, file: UploadFile = File(...)):
    # Save user selfie
    file_id = str(uuid.uuid4())
    filename = f"{file_id}_{file.filename}"
    path = os.path.join(STORAGE_DIR, filename)
    with open(path, "wb") as f:
        f.write(await file.read())
    asyncio.create_task(simulate_processing(file_id, user_id, "selfie", path))
    return UploadResponse(id=file_id, status="queued", message="Photo uploaded and queued for processing")

@app.get("/status/{file_id}")
async def status(file_id: str):
    result_path = os.path.join(STORAGE_DIR, f"{file_id}_result.json")
    if os.path.exists(result_path):
        import json
        with open(result_path, "r") as f:
            return json.loads(f.read())
    return JSONResponse(status_code=202, content={"file_id": file_id, "status": "processing"})

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
