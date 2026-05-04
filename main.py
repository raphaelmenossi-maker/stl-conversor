from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Pasta temporária para guardar ficheiros
UPLOAD_DIR = "temp_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def home():
    return {"mensagem": "Conversor STL Ativo! Envia um ficheiro para /convert"}

@app.post("/convert")
async def convert_stl(file: UploadFile = File(...)):
    """
    Rota que recebe o ficheiro STL.
    Por agora, ela apenas confirma a receção.
    """
    file_location = f"{UPLOAD_DIR}/{file.filename}"
    
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
        
    return {
        "info": "Ficheiro recebido com sucesso",
        "nome_arquivo": file.filename,
        "tamanho": f"{os.path.getsize(file_location)} bytes"
    }