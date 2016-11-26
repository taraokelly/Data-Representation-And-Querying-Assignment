import couchdb
from flask import Flask, render_template
from flask import request

import flask as fl

app = fl.Flask(__name__)

couch = couchdb.Server()

couch = couchdb.Server('http://127.0.0.1:5984/')

db = couch['test1'] # existing

@app.route("/")
def root():
    return render_template("index.html")

@app.route('/name', methods=["GET", "POST"])
def login():
	name = fl.request.values["userinput"]
	password = fl.request.values["password"]
	for id in db:
		doc = db[id]
		if(doc['username']== name):
			if(doc['password']== password):
				return '/Home'
			if(doc['password']!= password):
				return '/Error/Invalid Password'
	return '/Error/User Not Found'

@app.route('/register', methods=["GET", "POST"])
def register():
	name = fl.request.values["user"]
	password = fl.request.values["pass"]
	password1 = fl.request.values["pass1"]
	for id in db:
		doc = db[id]
		if(doc['username']== name):
			return '/Error/Username Already Exists'
	if(password!=password1):
		string = '/Error/Passwords Do Not Match'
	else:
		string = 'User Account Added Successfully'
		doc = {'username': name, 'password': password}
		db.save(doc)
	return string

@app.route("/Error/<reason>")
def error(reason):
	return render_template("index.html", error=reason)

@app.route('/Home')
def exampletwo():
	header = "Second example"
	return render_template("example.html", header=header)

if __name__ == "__main__":
   app.run()