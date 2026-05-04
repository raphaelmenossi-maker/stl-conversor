from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import uuid, os
from converter import jpg_to_stl

app = FastAPI()

UPLOAD_DIR = "temp"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/convert")
async def convert(file: UploadFile = File(...)):
    ext = file.filename.split(".")[-1]
    input_path = f"{UPLOAD_DIR}/{uuid.uuid4()}.{ext}"
    output_path = input_path.replace(f".{ext}", ".stl")

    with open(input_path, "wb") as f:
        f.write(await file.read())

    jpg_to_stl(input_path, output_path)

    return FileResponse(output_path, filename="modelo.stl")