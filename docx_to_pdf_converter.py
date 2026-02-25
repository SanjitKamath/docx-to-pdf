import subprocess
import os

def convert_docx_to_pdf(input_docx_path: str, output_dir: str):
    """
    Converts a DOCX file to PDF using headless LibreOffice.
    Raises an exception if the conversion fails.
    """
    if not os.path.exists(input_docx_path):
        raise FileNotFoundError(f"The file {input_docx_path} does not exist.")

    # The command to run LibreOffice without a graphical interface
    command = [
        'soffice',           
        '--headless',        
        '--convert-to', 'pdf',               
        '--outdir', output_dir,
        input_docx_path      
    ]

    try:
        # Run the command and capture any errors
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        # Decode the error and raise it so main.py can catch it
        error_message = e.stderr.decode('utf-8')
        raise RuntimeError(f"LibreOffice conversion failed: {error_message}")