# // the main where we find responses and 

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

cred_obj = credentials.Certificate('/home/jp/Documents/DubHack/secretkey.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'https://dubhack-nearby-default-rtdb.firebaseio.com':"URL to database"
	})


ref = db.reference("/")
with open("userinfo.json", "r") as file:
    data = json.load(file)
ref.set(data)

# load file contents




# //create instance of FIRDatabaseReference
# var ref: DatabaseReference!

# ref = Database.database().reference()

# //while friends list response is still empty keep searching
# let nearby = findfriends ()
# while(nearby.count == 0){
#     //keep searching 
#     nearby = findfriends ()
# }
# //now we have found a friend
# //check if you are free
# print("Are you free to hang out?")
# let status = readLine
# var freelist
# if (status == "Yes" || status = "yes"){
#     //search for response in nearby list
#     for item in nearby{
#         //if they are free 
#         freelist.append
#     }
#     //for all who are also free append to freelist
# }
# if
# //if no 
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
