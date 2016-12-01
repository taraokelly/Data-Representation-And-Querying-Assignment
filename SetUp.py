# Tara O'Kelly- G00322214.
# Third Year, Data Representation and Querying, Software Development, GMIT.
import couchdb

couch = couchdb.Server('http://127.0.0.1:5984/')

#create databases
dbPosts = couch.create('posts_tf')
dbUsers = couch.create('users_tf')
