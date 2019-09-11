from flask import Flask, render_template

app=Flask(__name__)


@app.route("/")
def index():
	return "ola"

@app.route("/pagina")
def pagina():
	return render_template("index.html")

@app.route("/test")
def test():	
	return "<input type='submit' value='intervalo'></input>"

app.run(debug=True,host="0.0.0.0")
