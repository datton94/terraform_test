#!/usr/bin/python3


import flask


app = flask.Flask(__name__)

@app.route('/')
def helloworld():
	return "Hello World!"

print(__name__)
if __name__ == "__main__":
	app.run(host='0.0.0.0')

