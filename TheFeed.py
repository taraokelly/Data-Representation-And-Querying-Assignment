import couchdb
import json
import time
from flask import Flask, render_template, request
from flask import request

import flask as fl

app = fl.Flask(__name__)

#couch = couchdb.Server()

couch = couchdb.Server('http://127.0.0.1:5984/')

db = couch['test1'] # existing

db1 = couch['posts']

cur_doc = ""

@app.route("/")
def root():
	if(not bool(cur_doc)):
		return render_template("index.html", loggedOut="loggedOut")
	rows = db1.view('_all_docs', include_docs=True)
	docs = [row.doc for row in rows]
	jstring = json.dumps((docs), indent=4)
	posts = json.loads(jstring)
	posts.reverse()
	return render_template("index.html", home="home", cur_doc=cur_doc, posts=posts)

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
	post_time = time.strftime("%c")
	if(not bool(post_content) or post_content.isspace()):
		return 'Error'
	tags = {tag.strip("#") for tag in post_tags.split() if tag.startswith("#")}
	count=0
	if(bool(tags)):
		count =0 
		for tag in tags:
			if(count==0):
				tags1 = '['
			else:
				tags1 += ','
			tags1 += '{ "tag" : "'+ tag + '"}'
			count+=1
		tags1 += ']' 
		tags = json.loads(tags1)
		doc = {'username' : cur_doc['username'], 'post_content' : post_content, 'post_time' : post_time, 'tags' : tags }
	else:
		doc = {'username' : cur_doc['username'], 'post_content' : post_content, 'post_time' : post_time}
	db1.save(doc)
	return ''

@app.route('/logout', methods=["GET", "POST"])
def logout():
	global cur_doc
	cur_doc=""
	return ''

@app.route("/Error/<reason>")
def error(reason):
	if(not bool(cur_doc)):
		return render_template("index.html", loggedOut = "loggedOut", error=reason)
	rows = db1.view('_all_docs', include_docs=True)
	docs = [row.doc for row in rows]
	jstring = json.dumps((docs), indent=4)
	posts = json.loads(jstring)
	posts.reverse()
	return render_template("index.html", home="home", cur_doc=cur_doc, posts=posts)

@app.route('/profile')
def profile():
	if(not bool(cur_doc)):
		return render_template("index.html", loggedOut = "loggedOut")
	string=''
	count = 0
	for id in db1:
		doc=db1[id]
		if(doc['username']==cur_doc['username']):
			if(count==0):
				string += '['
			else:
				string += ','
			string += '{"username": "'+ doc['username'] +'", "post_content": "'+ doc['post_content'] +'", "post_time": "'+ doc['post_time'] +'"}'
			count+=1
	if(count!=0):
		string+=']'
	posts = json.loads(string)
	posts.reverse()
	return render_template("index.html", profile="profile", cur_doc=cur_doc, posts=posts)

@app.route('/search')
def search():
	return ''

if __name__ == "__main__":
   app.run()