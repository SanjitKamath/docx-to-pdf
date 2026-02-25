from dox_to_pdf_converter import convert_docx_to_pdf
from create_complex_docx import create_complex_docx
import os

create_complex_docx("test.docx")
current_directory = os.path.abspath(os.path.dirname(__file__))
convert_docx_to_pdf("test.docx", current_directory)