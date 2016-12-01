# Data-Representation-And-Querying-Assignment
*A single-page web application(SPA) written in the programming language Python using the Flask framework. Third year, Data Representation and Querying, Software Development.*

![Alt Text](https://github.com/taraokelly/Data-Representation-And-Querying-Assignment/blob/master/static/img/thumbnail_logo.png "TheFeed")

**TheFeed**

I chose to create a blogging website as my single web-page application, as I thought it would provide a good demonstration of data representation and querying. The way I intended to deploy TheFeed would involve routing, which was a strong component in the project requirements. 

**Goals:**

- [x] Login/Sign up page
- [x] Home page displaying all user posts
- [x] Profile page showing current user posts 
- [x] Search bar to search users or tags
- [x] Settings page
- [x] Logout functionality

**Technologies**:

*Python3 and Flask
  *I used Python3 and Flask, a microframework for Python based on Werkzeug and Jinja2, for the server-side scripting. I used the @app.route decorator to map the URL to functions in my Flask App. I then used the Jinja2 template engine to render new templates when the functions mapped to @app.route decorator is called.
*HTML and Bootstrap
  *For the client side I used HTML and jQuery. I used Bootstap to create responsive designs in my HTML pages.

**Running this application**

You will need to install Python3: https://www.python.org/downloads/. After the installation of Python, you will have to import two Python modules: 

*Flask
*couchdb

Run the following commands to import the modules:

```
pip install flask
```

```
pip install couchdb
```

Install Bootstrap in the static folder with the bower file. First make sure you are in the static folder, then run the following command:

```
bower install bootstrap
```

To set up the required databases, return to the previous folder.

```
cd..
```

Ensure CouchDB is running and you are in the correct folder. Run:

```
Python SetUp.py
```

If you wish to populate the database with fake users:

```
Python Populate.py
```

