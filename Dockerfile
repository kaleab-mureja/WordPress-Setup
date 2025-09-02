FROM python:3.9-slim

# Install the requests library
RUN pip install requests

# Set the working directory
WORKDIR /app

# Copy the Python test script into the container
COPY test_fastapi.py .

# Command to run the test script
CMD ["python", "test_fastapi.py"]
