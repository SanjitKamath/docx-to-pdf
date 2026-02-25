# Start with a standard, lightweight Python image
FROM python:3.11-slim

# Install LibreOffice and standard fonts, plus metric-compatible MS fonts and symbols
# We use --no-install-recommends to keep the container size as small as possible
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libreoffice \
    fonts-liberation \
    fonts-crosextra-carlito \
    fonts-crosextra-caladea \
    fonts-dejavu && \
    rm -rf /var/lib/apt/lists/*

# Set up the working directory
WORKDIR /app

RUN pip install --upgrade pip

# Copy and install requirements first for Docker caching
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# Copy your Python scripts
COPY docx_to_pdf_converter.py .
COPY test.py .
COPY create_complex_docx.py .

# Run the Python script when the container starts
CMD ["python", "test.py"]