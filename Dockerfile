FROM python:3.10

WORKDIR /root

# you're API Token
ENV API_TELEGRAM_BOT=""

COPY *.py requirements.txt /root/

# install dependencies
RUN pip install -r requirements.txt

CMD [ "python3", "server.py" ]