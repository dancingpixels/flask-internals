from app import app # importing app variable from the app folder

@app.route("/")
def index():
	return "Hello World!"

@app.route("/about")
def about():
	return "All about Flask"
