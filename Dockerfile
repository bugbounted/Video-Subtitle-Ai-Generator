FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN sudo apt install portaudio19-dev

COPY . .

CMD [ "python", "./main.py" ]
