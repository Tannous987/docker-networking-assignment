# Use an official Python image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy necessary files
COPY requirements.txt .
COPY app.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for communication
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]
