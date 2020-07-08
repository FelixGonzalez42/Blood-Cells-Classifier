FROM ubuntu:latest
MAINTAINER  Your_name "felix141996@gmail.com"
RUN apt-get update -y
RUN apt-get install software-properties-common
RUN apt-add-repository universe
RUN apt-get update -y
RUN apt-get install -y build-essential python3.8 python-pip python-dev
VOLUME ["/var/www/app/public"]
ADD ~/DS4A/MinTIC-DS4A-Project---Team-14 /var/www/app/public
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
