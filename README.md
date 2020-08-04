<p align="center"><img src="https://github.com/Fag42/Blood-Cells-Classifier/blob/master/Documents/Media/GradCam.png"></p>
<H1 align="center">A Peripheral Blood Cell Classification App</H1>

## To build:

1 - Install Docker and git

2 - Open a command console (cmd,bash)

3 - Clone the official-repo:
```bash
  git clone https://github.com/Fag42/Blood-Cells-Classifier
```

4 - Go to app folder:
```bash
  cd /Blood-Cells-Classifier/App
```

5 - Build the docker image:
```bash
  sudo docker build -t ds4a2 . --no-cache
```

## To try:

1 - Open a command console (cmd,bash)

2 - Go to app folder: 
```bash
  cd /Blood-Cells-Classifier/App
```

3 - Execute the Docker container 
```bash
  sudo docker run -d -p 80:8050 --name ds4a -v $(pwd):/var/www/app/ ds4a2 -c "gunicorn app1:server -b :8050 -t 1000"
```

4 - Go to webpage: localhost:80

5 - <b>Enjoy</b>

## To run:

We have a demo application accessible from <b>https://bloodcells.ddns.net</b> (User: team14, Password: t34m14)
- Subject to server availability restrictions, <b>¡Feel free to try it!</b>
