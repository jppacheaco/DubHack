# // the main where we find responses and 
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time
# import findfriends

#while there are no friends nearby keep searching

#access firestore data
cred = credentials.Certificate('secretkey.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()
main_user = db.collection(u'users').document(u'user1')

response = input("Are you free to hang out?")
if response == 'no':
    #change your status to false
    main_user.update({
    	u'busy': True
	})
    #set a timer before you continute searching
    # delay = input("How long will you be busy?")
    # if delay.find()
    # time.sleep()
if response == 'yes':
    #change your status to true
    main_user.update({
    	u'busy': False
	})
	#search through database for other friends with yes
	


# closefriends = []
# # //while friends list response is still empty keep searching
# while len(closefriends) < 1:
#     closefriends = findfriends()

# # now we have found a friend

# # check if you are free


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
