import requests
import os
import sys

class DocumentConverterClient:
    def __init__(self, api_url: str = "http://localhost:8000"):
        self.api_url = api_url.rstrip("/")
        self.endpoint = f"{self.api_url}/convert"

    def convert_to_pdf(self, input_docx_path: str, output_pdf_path: str):
        if not os.path.exists(input_docx_path):
            print(f"Error: Cannot find file: {input_docx_path}")
            sys.exit(1)

        print(f"Sending '{input_docx_path}' to conversion server...")

        with open(input_docx_path, 'rb') as f:
            files = {
                'file': (os.path.basename(input_docx_path), f, 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            }
            response = requests.post(self.endpoint, files=files)

        if response.status_code == 200:
            with open(output_pdf_path, 'wb') as f:
                f.write(response.content)
            print(f"Success! PDF saved locally to '{output_pdf_path}'")
        else:
            print(f"Server Error ({response.status_code}): {response.text}")
            sys.exit(1)

if __name__ == "__main__":
    client = DocumentConverterClient(api_url="http://localhost:8000")
    
    # We use test.docx assuming you have uploaded one to your repo
    client.convert_to_pdf("test.docx", "final_output.pdf")