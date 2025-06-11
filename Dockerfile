# Use official Python image
FROM python:3.13.4-slim

# Set working directory
# WORKDIR /app
WORKDIR /app

COPY . /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the app code

# # Expose port
# EXPOSE 8000

# # Run FastAPI app
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]