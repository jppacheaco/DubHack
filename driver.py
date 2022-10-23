# // the main where we find responses and 
# import findfriends
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate('secretkey.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

users_ref = db.collection(u'users')
docs = users_ref.stream()

userid = []
attributes = []
#reading data
for doc in docs:
    userid.append(doc.id)
    attributes.append(doc.to_dict())
    
#writing data
doc_ref = db.collection(u'users')
print(doc_ref)


# closefriends = []
# # //while friends list response is still empty keep searching
# while len(closefriends) < 1:
#     closefriends = findfriends()

# # now we have found a friend

# # check if you are free
# response = input("Are you free to hang out?")

# if response == 'no':
    
	#search through database for other friends with yes

# //if response is single element
#     //ask if you want to meet up with that friend
#     //if yes, link up
#     //if no, set a timer for x amount of time
#     // when timer is up, restart at top of file
# //if response is greater than one element
#     //ask if you want to link up with any of the friends
#     //if response is yes
#         //which friends 
#         //link up with those friends
#     //if no 
#         //set timer
#         //when timer is up, restart at top of file
