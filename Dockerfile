FROM ubuntu:latest
MAINTAINER  Your_name "felix141996@gmail.com"
RUN apt-get update -y
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y software-properties-common build-essential python3.8 python-dev python3-pip git
COPY /home/AzureUser/DS4A/MinTIC-DS4A-Project---Team-14/requirements.txt /var/www/app/
RUN pip3 install -r requirements.txt
WORKDIR /var/www/app/
ENTRYPOINT ["python3"]
CMD ["public/app1.py"]
