# Project Title

Simple Travelex Demo

## Description

An in-depth paragraph about your project and overview of use.


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

### Beanstalk Init
```
eb init -p python-3.6 travelex-env --region eu-west-2
```

then again to manually select
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

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_dockerpreconfig.walkthrough.html

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

ex. Sebastian Cheung




