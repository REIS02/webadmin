from flask import Flask

app=Flask(__name__)


@app.route("/")
def index():
	return "ola"

app.run(debug=True,host="0.0.0.0")
