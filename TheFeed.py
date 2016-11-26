import couchdb
from flask import Flask, render_template
from flask import request

import flask as fl

app = fl.Flask(__name__)

couch = couchdb.Server()

couch = couchdb.Server('http://127.0.0.1:5984/')

# to create new database
#db = couch.create('test')

db = couch['test1'] # existing

#doc = {'foo': 'bar'}
#db.save(doc)

#	for id in db:
#		print(id)


@app.route("/")
def root():
    #return app.send_static_file('index.html')
    return render_template("index.html")

@app.route('/name', methods=["GET", "POST"])
def login():
	name = fl.request.values["userinput"]
	password = fl.request.values["password"]
	for id in db:
		doc = db[id]
		if(doc['username']== name):
			if(doc['password']== password):
				return 'Login for user ' + doc['username'] + ' successful.'
			if(doc['password']!= password):
				return 'Invalid Password'
	return 'User not found'

@app.route('/register', methods=["GET", "POST"])
def register():
	name = fl.request.values["user"]
	password = fl.request.values["pass"]
	password1 = fl.request.values["pass1"]
	if(password!=password1):
		string = 'Passwords do not match'
	else:
		string = name + ' added successfully'
		doc = {'username': name, 'password': password}
		db.save(doc)
	return string

@app.route('/Home')
def exampletwo():
	header = "Second example"
	return render_template("example.html", header=header)

if __name__ == "__main__":
   app.run()