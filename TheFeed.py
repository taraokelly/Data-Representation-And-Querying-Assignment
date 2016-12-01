import couchdb, json, time
from flask import Flask, render_template, request
import flask as fl

app = fl.Flask(__name__)

couch = couchdb.Server('http://127.0.0.1:5984/')
db = couch['test1'] # existing
db1 = couch['posts']

cur_doc = ""

@app.route("/")
def root():
	if(not bool(cur_doc)):
		return render_template("index.html", loggedOut="loggedOut")
	posts=getPosts()
	return render_template("index.html", home="home", cur_doc=cur_doc, posts=posts)

@app.route("/Error/<reason>")
def error(reason):
	if(not bool(cur_doc)):
		return render_template("index.html", loggedOut = "loggedOut", error=reason)
	posts=getPosts()
	return render_template("index.html", home="home", cur_doc=cur_doc, posts=posts)

@app.route('/profile')
def profile():
	if(not bool(cur_doc)):
		return render_template("index.html", loggedOut = "loggedOut")
	posts=getPostsByUser(cur_doc['username'])
	return render_template("index.html", profile="profile", cur_doc=cur_doc, posts=posts)

@app.route('/search/users/<user>')
def search(user):
	if(not bool(cur_doc)):
		return render_template("index.html", loggedOut = "loggedOut")
	posts=getPostsByUser(user);
	return render_template("index.html", search=user, cur_doc=cur_doc, posts=posts)

@app.route('/search/tags/<tag>')
def searchTag(tag):
	if(not bool(cur_doc)):
		return render_template("index.html", loggedOut = "loggedOut")
	posts=getPostsByTag(tag);
	return render_template("index.html", search=tag, cur_doc=cur_doc, posts=posts)

@app.route('/settings')
def settings():
	if(not bool(cur_doc)):
		return render_template("index.html", loggedOut = "loggedOut")
	return render_template("index.html", settings="settings", cur_doc=cur_doc)

@app.route('/logout', methods=["GET", "POST"])
def logout():
	global cur_doc
	cur_doc=""
	return ''

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
				temp = '['
			else:
				temp+= ','
			temp += '{ "tag" : "'+ tag + '"}'
			count+=1
		temp += ']' 
		tags = json.loads(temp)
		doc = {'username' : cur_doc['username'], 'post_content' : post_content, 'post_time' : post_time, 'tags' : tags, 'tags_string' : post_tags}
	else:
		doc = {'username' : cur_doc['username'], 'post_content' : post_content, 'post_time' : post_time, 'tags' : [], 'tags_string' : post_tags} 
	db1.save(doc)
	return ''

@app.route('/delete', methods=["GET","POST"])
def delete():
	global cur_doc 
	for id in db1:
		doc = db1[id]
		if(doc['username']==cur_doc['username']):
			db1.delete(doc)
	db.delete(cur_doc)
	cur_doc= ""
	return ''

@app.route('/updateName', methods=["GET","POST"])
def updateName():
	global cur_doc
	name = fl.request.values["name"]
	for id in db:
		doc =db[id]
		if(name==doc['username']):
			return 'Username Already Exists'
	# Database Containing Posts
	for id in db1:
		doc =db1[id]
		if(doc['username']==cur_doc['username']):
			doc['username']=name
			db1[doc.id]=doc	
	# Database Containing User Info
	for id in db:
		doc =db[id]
		if(doc['username']==cur_doc['username']):
			doc['username']=name
			db[doc.id]=doc
			cur_doc = doc
	return 'successful'

@app.route('/updatePass', methods=["GET","POST"])
def updatePass():
	password = fl.request.values["password"]
	password1 = fl.request.values["password1"]
	global cur_doc
	if(password!=password1):
		return 'Passwords Do Not Match'
	elif(' ' in password):
		return 'Password Contains Spaces'
	elif(len(password) < 8):
		return 'Password Must Contain 8 Characters'
	for id in db:
		doc =db[id]
		if(doc['username']==doc['username']):
			doc['password']=password
			db[doc.id]=doc	
			cur_doc = doc
	return 'successful'

@app.route('/securityCheck', methods=["GET","POST"])
def check():
	temp = fl.request.values["password"]
	if(temp==cur_doc['password']):
		return 'Correct'
	return 'Incorrect Password'

def getPosts():
	rows = db1.view('_all_docs', include_docs=True)
	docs = [row.doc for row in rows]
	jstring = json.dumps((docs), indent=4)
	posts = json.loads(jstring)
	posts.reverse()
	return posts

def getPostsByUser(username):
	posts=[]
	count = 0
	for id in db1:
		doc=db1[id]
		if(doc['username']==username):
			if(count==0):
				string = '['
			else:
				string += ','
			string += '{"username": "'+ doc['username'] +'", "post_content": "'+ doc['post_content'] +'", "post_time": "'+ doc['post_time'] +'", "tags_string" : "'+ doc['tags_string'] +'"}'
			count+=1
	if(count!=0):
		string+=']'
		#Adapted from http://stackoverflow.com/questions/9347419/python-strip-with-n
		string = string.replace('\n',' ')
		posts = json.loads(string)
		posts.reverse()
	return posts

def getPostsByTag(TAG):
	posts=[]
	count = 0
	for id in db1:
		doc = db1[id]
		for tag in doc['tags']:
			print(tag)
			if(tag):
				if(tag['tag']==TAG):
					print(tag)
					if(count==0):
						string = '['
					else:
						string += ','
					string += '{"username": "'+ doc['username'] +'", "post_content": "'+ doc['post_content'] +'", "post_time": "'+ doc['post_time'] +'","tags_string" : "'+ doc["tags_string"] +'"}'
					count+=1
	if(count!=0):
		string+=']'
		string = string.replace('\n',' ')
		posts = json.loads(string)
		posts.reverse()
		print(posts)
	return posts

if __name__ == "__main__":
   app.run()