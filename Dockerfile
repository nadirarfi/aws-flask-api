FROM python:3.9.15-alpine

WORKDIR /aws-flask-api

# Keeps Python from generating .pyc files in the container
#ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
#ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy source code to image
COPY . .

EXPOSE 5000

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
#RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
#USER appuser

CMD ["python", "app.py"]
