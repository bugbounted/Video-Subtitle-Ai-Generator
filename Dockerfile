FROM mcr.microsoft.com/playwright/python:v1.29.0-focal

RUN pip install --upgrade pip

RUN apt-get update -y && \
    apt-get install -y portaudio19-dev

RUN mkdir /app
ADD . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]
