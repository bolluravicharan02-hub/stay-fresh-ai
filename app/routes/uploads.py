import os
import uuid

from fastapi import APIRouter, File, UploadFile, HTTPException

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/")
async def upload_invoice(file: UploadFile = File(...)):

    try:

        extension = os.path.splitext(file.filename)[1]

        file_id = f"{uuid.uuid4()}{extension}"

        file_path = os.path.join(
            UPLOAD_DIR,
            file_id
        )

        with open(file_path, "wb") as f:
            f.write(await file.read())

        return {
            "success": True,
            "file_id": file_id,
            "filename": file.filename
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )