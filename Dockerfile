# Start with a standard, lightweight Python image
FROM python:3.11-slim

# Install LibreOffice and some standard fonts
# We use --no-install-recommends to keep the container size as small as possible
RUN apt-get update && \
    apt-get install -y --no-install-recommends libreoffice fonts-liberation && \
    rm -rf /var/lib/apt/lists/*

# Set up the working directory
WORKDIR /app

RUN pip install -r requirements.txt

# Copy your Python script and a sample document into the container
COPY docx_to_pdf_converter.py .
COPY test.py .
COPY create_complex_docx.py .

# Run the Python script when the container starts
CMD ["python", "test.py"]