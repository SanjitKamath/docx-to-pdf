import os
import tempfile
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from fastapi.background import BackgroundTasks

# Import the logic from your dedicated converter file
from docx_to_pdf_converter import convert_docx_to_pdf

app = FastAPI(title="DOCX to PDF Converter API")

def cleanup_temp_files(*file_paths):
    """Deletes temporary files after the response is sent."""
    for path in file_paths:
        if os.path.exists(path):
            os.remove(path)

@app.post("/convert")
async def convert_docx(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    if not file.filename.endswith('.docx'):
        raise HTTPException(status_code=400, detail="Only .docx files are supported")
    
    # 1. Create a safe temporary file for the incoming DOCX
    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp_in:
        tmp_in.write(await file.read())
        input_path = tmp_in.name
    
    # 2. Define output paths
    output_dir = os.path.dirname(input_path)
    output_filename = os.path.splitext(os.path.basename(input_path))[0] + ".pdf"
    output_path = os.path.join(output_dir, output_filename)

    # 3. Run LibreOffice conversion using your custom module
    try:
        convert_docx_to_pdf(input_path, output_dir)
    except Exception as e:
        cleanup_temp_files(input_path) # Cleanup on failure
        raise HTTPException(status_code=500, detail=str(e))
    
    # 4. Return the PDF and schedule the cleanup
    background_tasks.add_task(cleanup_temp_files, input_path, output_path)
    
    return FileResponse(
        output_path, 
        media_type="application/pdf", 
        filename=file.filename.replace('.docx', '.pdf')
    )