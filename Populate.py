# Tara O'Kelly- G00322214.
# Third Year, Data Representation and Querying, Software Development, GMIT.
import couchdb

couch = couchdb.Server('http://127.0.0.1:5984/')

#open existing databases
dbPosts = couch['posts_tf']
dbUsers = couch['users_tf']

#populate users_tf
dbUsers.save({'username': 'John Smith', 'password': 'password1'})
dbUsers.save({'username': 'Alice', 'password': 'password1'})
dbUsers.save({'username': 'Anna55', 'password': 'password1'})
dbUsers.save({'username': 'Kelly Davis', 'password': 'password1'})
dbUsers.save({'username': 'Jack101', 'password': 'password1'})

#populate posts_tf
dbPosts.save({'username' : 'Anna55', 'post_content' : 'It can not be time to go to work again :( ', 'post_time' : 'Mon Nov  7 22:45:16 2016', 'tags' : [{"tag" : "tired"}, {"tag" : "work"}], 'tags_string' : '#tired #work'})
dbPosts.save({'username' : 'Jack', 'post_content' : 'THANK GOD ITS FRIDAY', 'post_time' : 'Fri Nov  13 14:27:12 2016', 'tags' : [{"tag" : "TGIF"}], 'tags_string' : '#TGIF'})
dbPosts.save({'username' : 'John Smith', 'post_content' : 'What a long day...', 'post_time' : 'Sat Nov  19 22:45:16 2016', 'tags' : [{"tag" : "tired"}, {"tag" : "readyforbed"}], 'tags_string' : '#tired #readyforbed'})
dbPosts.save({'username' : 'Alice', 'post_content' : 'Great time with my girls today', 'post_time' : 'Sun Nov  20 20:18:29 2016', 'tags' : [{"tag" : "fun"}, {"tag" : "friends"}], 'tags_string' : '#fun #friends'})
dbPosts.save({'username' : 'Kelly Davis', 'post_content' : 'TGIF', 'post_time' : 'Sun Nov  25 17:03:34 2016', 'tags' : [{"tag" : "TGIF"}, {"tag" : "Friday"}], 'tags_string' : '#TGIF #Friday'})
dbPosts.save({'username' : 'Kelly Davis', 'post_content' : 'On holiday at last! The weather is fab in Spain.', 'post_time' : 'Sun Nov  27 13:26:57 2016', 'tags' : [{"tag" : "sunny"}, {"tag" : "holiday"}, {"tag" : "friends"}, {"tag" : "byebyeireland"}], 'tags_string' : '#sunny #holiday #byebyeireland #friends'})
dbPosts.save({'username' : 'Jack', 'post_content' : 'Just got promoted! Delighted :D', 'post_time' : 'Fri Nov  28 17:07:12 2016', 'tags' : [{"tag" : "promotion"},{"tag" : "promotion"}], 'tags_string' : '#promotion #work'})
dbPosts.save({'username' : 'Alice', 'post_content' : 'Yum, Nandos!!', 'post_time' : 'Thu Dec  1 14:27:12 2016', 'tags' : [{"tag" : "hungry"}], 'tags_string' : '#hungry'})
dbPosts.save({'username' : 'John Smith', 'post_content' : 'Wonderful day to walk my dog!', 'post_time' : 'Thu Dec  1 14:43:48 2016', 'tags' : [], 'tags_string' : ''})
dbPosts.save({'username' : 'John Smith', 'post_content' : 'Good Morning All', 'post_time' : 'Fri Dec  2 12:32:05 2016', 'tags' : [{"tag" : "afternoonreally"}, {"tag" : "morning"}], 'tags_string' : '#morning #afternoonreally'})