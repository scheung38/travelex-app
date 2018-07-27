# Project Title

Travelex API Demo

## Description

This is a Python-Flask API backend demo, with pytest unittesting and
Dockerized, and deployed to AWS Beanstalk

### Installing MacOSX

* brew install pipenv


### To start a shell:

* pipenv shell

### Install from Pipfile

* pipenv install

### Executing program

To Start the app
```
$ cd travelex-app &&
$ export FLASK_APP=application
$ python -m flask run
```

To Stop the app
```
Ctrl-C
```

Running unittest:
```
$ python -m pytest -v
```

### Dockerize app
Ensure docker is running in the background then

```
$ docker build -t niceseb/travelex-app .
```


Run the containerize app
```
$ docker run -it  --rm -p 5000:5000 niceseb/travelex-app:latest
```

### To view in browser:
```
http://localhost:5000
```

### AWS Beanstalk Steps to Deploy
```
eb init -p python-3.6 travelex-env --region eu-west-2
```

then again to manually select or override settings
```
eb init
```

Create an environment and deploy with eb create
```
eb create travelex-env
```

### To zip bundle for AWS
```
$ git archive -v -o travelex-app.zip --format=zip HEAD
```

### Deploy to AWS

```
$ eb deploy
```

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_dockerpreconfig.walkthrough.html

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

Sebastian Cheung




