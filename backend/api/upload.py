from fastapi import File, UploadFile, APIRouter
from services import pdf_service

router = APIRouter()
pdf_service = pdf_service.PDFService()

@router.post("/upload")
async def upload_pdf(file:UploadFile=File(...)):
    fpath = await pdf_service.save_pdf(file)
    return {'message':'success','file_path':fpath, 'file_name':file.filename}