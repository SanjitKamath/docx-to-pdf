import subprocess
import os

def convert_docx_to_pdf(input_docx_path, output_dir):
    """
    Converts a DOCX file to PDF using headless LibreOffice.
    """
    if not os.path.exists(input_docx_path):
        print(f"Error: The file {input_docx_path} does not exist.")
        return

    print(f"Converting '{input_docx_path}' to PDF...")

    # The command to run LibreOffice without a graphical interface
    command = [
        'soffice',           # The LibreOffice executable
        '--headless',        # Run without a UI
        '--convert-to',      # Tell it we are converting a file
        'pdf',               # Target format
        '--outdir',          # Where to save the result
        output_dir,
        input_docx_path      # The file to convert
    ]

    try:
        # Run the command and capture any errors
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Success! PDF saved to {output_dir}")
    except subprocess.CalledProcessError as e:
        print("Conversion failed!")
        print(f"Error details: {e.stderr.decode('utf-8')}")

