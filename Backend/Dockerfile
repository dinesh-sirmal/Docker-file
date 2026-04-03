# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements first (better caching)
COPY requirements.txt .

# Install pip dependencies with longer timeout and no cache
RUN pip install --no-cache-dir --default-timeout=200 -r requirements.txt

# Copy the app code
COPY app.py .

# Expose the port your app runs on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
