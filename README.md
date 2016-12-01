# Data-Representation-And-Querying-Assignment
*A single-page web application(SPA) written in the programming language Python using the Flask framework. Third year, Data Representation and Querying, Software Development.*

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

1. Python3 and Flask - I used Python3 and Flask, a microframework for Python based on Werkzeug and Jinja2, for the server-side scripting. I used the @app.route decorator to map the URL to functions in my Flask App. I then used the Jinja2 template engine to render new templates when the functions mapped to @app.route decorator is called.

2. HTML and Bootstrap - For the client side I used HTML and jQuery. I used Bootstap to create responsive designs in my HTML pages.

3. CouchDB - I choose to utilize CouchDB a mechanism to store data. 

**Running this application**

You will need to install Python3: [here](https://www.python.org/downloads/). After the installation of Python, you will have to import two Python modules: 

1. Flask

2. Couchdb

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

Finally, to run the app:

```
Python TheFeed.py
```

**Conclusion:**

To conclude, this project has been immensely rewarding. I had no experience in these technologies pior to this module(excluding HTML). I am certainly interested in continuing and furthing the progress and funtionality of this project. There are numerous other features that I would like to add to this SPA. Such as: allowing users to follow one another, allowing users to customize their profile and allowing users to view profiles, adding comments... etc. However if if were to follow up on this idea, I would start from the beginning and design the web app more efficiently.

**References:**

[Bootstrap](http://getbootstrap.com/)

[Python](https://www.python.org/)

[CouchDB](http://couchdb.apache.org/)

-----

__*Tara O'Kelly - G00322214@gmit.ie*__
