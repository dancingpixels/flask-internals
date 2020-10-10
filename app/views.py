from app import app # importing app variable from the app folder
from flask import render_template
from datetime import datetime
from flask import request
from flask import redirect

@app.route("/")
def index():
	app.config["SECRET_KEY"] = "iuhto743yto34iuho287gh78"
	print(app.config["SECRET_KEY"])
	print(app.config)
	return render_template("public/index.html")

@app.route("/about")
def about():
	return render_template("public/about.html")

# routes with multiple variables
@app.route("/multiple/<one>/<two>/<three>")
def multiple(one, two, three):
	return f"One is {one}, two is {two}, three is {three}."

# dynamic urls
@app.route("/profile/<username>")
def profile(username):

	users = {
	    "rona": {
	        "name": "Armin Ronacher",
	        "bio": "Creator of the Flask framework",
	        "twitter_handle": "@mitsuhiko"
	    },
	    "guido": {
	        "name": "Guido Van Rossum",
	        "bio": "Creator of the Python programming language",
	        "twitter_handle": "@gvanrossum"
	    },
	    "elonmusk": {
	        "name": "Elon Musk",
	        "bio": "technology entrepreneur, investor, and engineer",
	        "twitter_handle": "@elonmusk"
	    }
    }

	user = None

	if username in users:
		user = users[username]

	return render_template("public/profile.html", 
		                   username=username,
		                   user=user)


@app.route("/sign-up", methods=["GET","POST"])
def sign_up():

	if request.method == 'POST':
		
		username = request.form.get('username')
		email = request.form.get('email')
		password = request.form.get('password')

		# An alternate way of getting information from forms

		# username = request.form['username']
		# email = request.form['email']
		# password = request.form['password']

		req = request.form
		missing = list()

		for key, value in req.items():
			if value == "":
				missing.append(key)

		if missing:
			feedback = f"Missing fields for {', '.join(missing)}"
			return render_template("public/sign_up.html", feedback=feedback)

		return redirect(request.url)
	return render_template("public/sign_up.html")

@app.route("/jinja")
def jinja():
	# Strings 
	my_name = "Santiago Sevilla"

	#integers
	my_age = 105

	#Lists
	langs = ["Python", "Scheme", "Lisp", "Elixir","Ruby", "Ocaml"]

	#Dictionaries
	friends = {
	  "Kounde" : 90,
	  "Takefuso" : 81,
	  "Adama" : 79,
	  "Camavinga" : 80,
	  "Lunin" : 80
	}

	# tuple 
	clubs = ("Barcelona", "Celta Vigo")

	# Booleans
	cool_beans = True

    #classes
	class GitRemote():
		def __init__(self, name, description, domain):
			self.name = name
			self.description = description
			self.domain = domain

		def pull(self):
			return f"Pulling repo  '{self.name}'"

		def clone(self, repo):
			return f"Cloning into {repo}"

	my_remote = GitRemote(name="Inside Flask",
		description="Mastering the internals of the flask framework",
		domain="https://github.com/dancingpixels/inside-flask.git")

	# functions
	def repeat(x, qty=1):
		return x * qty

	date = datetime.utcnow()

	my_html = "<h1>This is some dope HTML</h1>"

	suspicious = "<script>alert('NEVER TRUST USER INPUT')</script>"


	return render_template("public/jinja.html", my_name=my_name, my_age=my_age, langs=langs,
		friends=friends, clubs=clubs, cool_beans=cool_beans, repeat=repeat,
		GitRemote=GitRemote, my_remote=my_remote, date=date, my_html=my_html, 
		suspicious=suspicious)

# Registering a template filter
@app.template_filter("clean_date")
def clean_date(dt):
	return dt.strftime("%d %b %Y")

@app.route("/query")
def query():

	if request.args:

	    # We have our query string nicely serialized as a Python dictionary
	    args = request.args

	    # We'll create a string to display the parameters & values
	    serialized = ", ".join(f"{k}: {v}" for k, v in request.args.items())

	    # Display the query string to the client in a different format
	    return f"(Query) {serialized}", 200

	else:

	    return "No query string received", 200 
