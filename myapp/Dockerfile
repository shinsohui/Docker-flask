FROM python:3.6.9

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /home/ubuntu/
RUN git clone https://github.com/shinsohui/Docker-flask.git

COPY . .

CMD ["python", "app.py"]