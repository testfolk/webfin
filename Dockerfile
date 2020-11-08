# Use an official Python runtime as a parent image
FROM python:3

RUN apt-get update
RUN apt install -y wget build-essential libssl-dev zlib1g-dev libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev libgdbm-dev libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev libffi-dev uuid-dev
EXPOSE 8088
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

RUN python setup.py install

WORKDIR /src/webfin

CMD ["webfin", "serve", "--port" ,"8088", "--host", "0.0.0.0"]

#CMD /bin/bash