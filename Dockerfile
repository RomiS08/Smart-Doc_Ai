# Use an Alpine-based Python image
FROM python:3.11-alpine

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install MySQL development packages (including mysql_config) using apk
RUN apk update && apk add mariadb-dev


# Install Python packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Set the command to run your application
CMD python manage.py runserver 0.0.0.0:8000


