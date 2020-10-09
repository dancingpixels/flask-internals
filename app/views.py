from app import app # importing app variable from the app folder
from flask import render_template
from datetime import datetime
from flask import request
from flask import redirect

@app.route("/")
def index():
	return render_template("public/index.html")

@app.route("/about")
def about():
	return render_template("public/about.html")

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

