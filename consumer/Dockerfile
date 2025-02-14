# Use an official Python image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy necessary files
COPY requirements.txt .
COPY app.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Define a volume mount point
VOLUME /data

# Start the application
CMD ["python", "app.py"]
