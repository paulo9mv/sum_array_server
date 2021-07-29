# Index Array Equilibrium API

This API provides an endpoint to get the _index array equilibrium_ based on the provided array.
It is hosted at Heroku.

## Documentation

```
Request
POST ${BASE_URL}/equilibrium, { arr: Array<number> }
#BASE_URL is the current URL where the API is hosted. Today is hosted at https://sumarray.herokuapp.com/

Response
{ index: number }
#If the array doesn't have an index of equilibrium, it returns index -1

In case of error, it returns the error message
{ error: string }

```
## To start the server
This tutorial supposes that you have **Python 3.7** installed.

First, let's start a virtual environment. If you don't have `venv` installed, check the [official docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)

```
$ python3 -m venv env
$ source env/bin/activate
(env) $
```

Now let's install the packages from `requirements.txt`
```
(env) $ pip3 install -r /path/to/requirements.txt
(env) $ flask run
```

You should see the following output and now, your API is **UP**!
```
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## To run tests

```
$ py.test
```
The tests check for error status and assert if the algorithm is correct.

## Tools used in the project :paperclip:
:wrench: Configuration:
- [Python3](https://reactjs.org/)
- [Pip3](https://create-react-app.dev/)

🖥️ Server:
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Flask-CORS](https://flask-cors.readthedocs.io/)


:art: Helpers:
- [Numpy](https://numpy.org/)


:cloud: Deploy:
- [Heroku](https://heroku.com)

