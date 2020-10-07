from app import app
from flask import render_template

@app.route("/python")
def praise_python():
	return render_template("praise/praise-python.html")


