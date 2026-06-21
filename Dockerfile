# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY monitor.py .
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Run the monitor script
CMD ["python3", "monitor.py"]
