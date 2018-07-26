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
$ cd travelex-flask-aws-docker &&
$ export FLASK_APP=application
$ flask run
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
$ docker build -t niceseb/travelex-flask .
```


Run the containerize app
```
$ docker run -it  --rm -p 5000:5000 niceseb/travelex-flask:latest
```

To view in browser:
```
http://localhost:5000
```


## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

ex. Sebastian Cheung




