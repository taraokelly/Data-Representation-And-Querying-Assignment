import couchdb
import json
from flask import Flask, render_template, request
from flask import request

import flask as fl

app = fl.Flask(__name__)

couch = couchdb.Server()

couch = couchdb.Server('http://127.0.0.1:5984/')

db = couch['test1'] # existing

db1 = couch['posts']

loggedIn = 0

cur_doc = ""

@app.route("/")
def root():
	if(loggedIn==0):
		return render_template("index.html", loggedOut="loggedOut")
	return render_template("index.html", home="home", cur_doc=cur_doc)

@app.route('/login', methods=["GET", "POST"])
def login():
	name = fl.request.values["username"]
	password = fl.request.values["password"]
	for id in db:
		doc = db[id]
		if(doc['username']== name):
			if(doc['password']== password):
				global loggedIn
				loggedIn = 1
				global cur_doc
				cur_doc = db[id]
				return '/'
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
	if(not bool(name)):
		string = '/Error/Enter Username'
	elif(name.isspace()):
		string = '/Error/Username Must Contain Characters'
	elif(password!=password1):
		string = '/Error/Passwords Do Not Match'
	elif(' ' in password):
		string = '/Error/Password Contains Spaces'
	elif(len(password) < 8):
		string = '/Error/Password Must Contain 8 Characters'
	else:
		string = 'Congrats ' + name + '!'
		doc = {'username': name, 'password': password}
		db.save(doc)
	return string

@app.route('/addPost', methods=["GET", "POST"])
def addPost():
	post_content = fl.request.values["post_content"]
	post_tags = fl.request.values["post_tags"]
	if(not bool(post_content) or post_content.isspace()):
		return 'Error'
	tags = {tag.strip("#") for tag in post_tags.split() if tag.startswith("#")}
	count=0
	if(bool(tags)):
		for tag in tags:
			if(count==0):
				tags1 = '['
			else:
				tags1 += ','
			tags1 += '{ "tag"' 
			tags1 += ' : ' 
			tags1 += '"'
			tags1 += tag 
			tags1 += '"' 
			tags1 += '}'
			count+=1
		tags1 += ']'  
		print(tags1)
		tags = json.loads(tags1)
	else:
		tags=''
	doc = {'username' : cur_doc['username'], 'post_content' : post_content, 'tags' : tags }
	db1.save(doc)
	return ''

@app.route("/Error/<reason>")
def error(reason):
	if(loggedIn==0):
		return render_template("index.html", loggedOut = "loggedOut", error=reason)
	return render_template("index.html")

@app.route('/profile')
def profile():
	if(loggedIn==0):
		return render_template("index.html", loggedOut = "loggedOut")
	return render_template("index.html", profile="profile", cur_doc=cur_doc)

#@app.route('/Home/logout')

if __name__ == "__main__":
   app.run()