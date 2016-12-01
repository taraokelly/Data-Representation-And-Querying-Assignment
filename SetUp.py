import couchdb

couch = couchdb.Server('http://127.0.0.1:5984/')

#create databases
dbPosts = couch.create('posts_tf')
dbUsers = couch.create('users_tf')

#populate users_tf
dbUsers.save({'username': 'John Smith', 'password': 'password1'})
dbUsers.save({'username': 'Alice', 'password': 'password1'})
dbUsers.save({'username': 'Anna55', 'password': 'password1'})
dbUsers.save({'username': 'Kelly Davis', 'password': 'password1'})
dbUsers.save({'username': 'Jack101', 'password': 'password1'})
