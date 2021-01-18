# Use an official Python runtime as a parent image
FROM python:3

WORKDIR /src/webfin
COPY . .
RUN python -m pip install .
EXPOSE 80
webCMD ["webfin", "serve", "--port" ,"80", "--host", "0.0.0.0"]

#CMD /bin/bash
