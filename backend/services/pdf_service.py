from pathlib import Path
from fastapi import UploadFile
import fitz

class PDFService:
    def __init__(self):
        self.books_dir = Path("data/books")
        self.books_dir.mkdir(parents=True, exist_ok=True)

    async def save_pdf(self, file:UploadFile):
        filepath = self.books_dir/file.filename
        with open(filepath, "wb") as f:
            content = await file.read()
            f.write(content)

        return str(filepath)

    def extract_text(self, filepath: str):
        document = fitz.open(filepath)
        text = ''
        for page in document:
            t = page.get_text()
            text += '\n' + t
        document.close()
        return text

pdf_service = PDFService()
