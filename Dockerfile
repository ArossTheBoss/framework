# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Run the command to install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

ENV TEST_ENV=DEV

# Run hello.py when the container launches
CMD ["pytest", "tests/","--html=reports/report.html", "--self-contained-html", "-v"]
