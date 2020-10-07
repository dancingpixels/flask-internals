from app import app # importing app variable from the app folder
from flask import render_template

@app.route("/")
def index():
	return render_template("public/index.html")

@app.route("/about")
def about():
	return """<h1 style='color: red;'> I am a red H1 reading</h1>
	          <p> This is a lovely little paragraph</p>
	          <code> Flask is <em>awesome</em></code>"""
