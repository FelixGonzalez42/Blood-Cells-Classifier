FROM ubuntu:latest
MAINTAINER  Your_name "felix141996@gmail.com"
RUN apt-get update -y
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y software-properties-common build-essential python3.8 python-dev python3-pip
COPY . /app
WORKDIR /app
RUN python3 pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]
