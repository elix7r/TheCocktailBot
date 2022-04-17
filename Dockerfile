FROM python:3.8

WORKDIR /app

# you're API Token
ENV API_BOT=""

COPY *.py requirements.txt /app/

# install libraries
RUN pip install -r requirements.txt

CMD [ "python", "server.py" ]