FROM python:3.8

WORKDIR /home

ENV API_BOT=""

COPY *.py requirements.txt ./
RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "server.py" ]