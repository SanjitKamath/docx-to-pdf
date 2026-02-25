FROM python:3.11-slim

# Install LibreOffice and core fonts
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libreoffice \
    fonts-liberation \
    fonts-crosextra-carlito \
    fonts-dejavu && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python API dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy API server code
COPY main.py .

# Expose the API port
EXPOSE 8000

# Start the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]