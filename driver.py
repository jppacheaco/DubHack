#import needed packages
import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'firebase-admin'])

#the main where we find responses and 
from contextlib import nullcontext
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time

#helper files
import runRadius
import findfriends


cred = credentials.Certificate('secretkey.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()
users_ref = db.collection(u'users')
docs = users_ref.stream()
main_user = db.collection(u'users').document(u'user1')
available = []


#return the information of the local user
@app.route('/user_info()')
def user_info():
    id = 'unknown user'
    attributes = []
    for doc in docs:
        if doc.id == 'user1':
            id = doc.id
            attributes = doc.to_dict()
    return (id, attributes)

#contantly running function that returns a list of nearby friends when there are friends nearby the user
@app.route('/makeconnections')
def makeconnections():
	localfriends = []
	#while there are no friends nearby keep searching every minute
	while len(localfriends) == 0:
		localfriends = runRadius.nearby(db)
		if len(localfriends) == 0:
			time.sleep(60)
   
	return localfriends

#function to ask if the user is free
@app.route('/ask_free')
def ask_free():
    response = input("Are you free to hang out?")
    return response

#if the user this asks how long the user will be busy
@app.route('/busy_user')
def busy_user():
	delay = input("How long will you be busy?")
	return delay

#updates the busy status of the user
@app.route('/update_busy')
def update_busy():
		main_user.update({
			u'busy': True
		})
  
#if the user responds that they are busy
@app.route('/not_free()')
def not_free(delay):
	#change your status to falseprint("ERROR: Invalid entry")
	main_user.update({
		u'busy': True
	})
	
	sorter = ''.join(x for x in delay if x.isdigit())
	number = int(sorter)

	if 'hour' in delay or 'hr' in delay:
		total = number*60*60
	elif 'minute' in delay or 'min' in delay:
		total = number*60
	elif 'sec' in delay or 'second' in delay:
		total = number
	#wait designated time and then restart
	else:
		bad_entry()
	time.sleep(total)

#error to be thrown if we recieve an entry that doesnt make sense
@app.route('/bad_entry')
def bad_entry():
    print("ERROR: Invalid entry")

#function to ask user if they want to hang out with a single friend
@app.route('/single_friend')
def single_friend(name):
    response = input("Would you like to do something with " + name + "?")
    return response

#finds the friends that are also free
@app.route('/findfriends')
def get_available(localfriends):
    list = (db, localfriends)
    available = findfriends.findFriends(list)
    return available

#asks user if they want to hang out with multiple friends
@app.route('/multi_friend')
def multi_friends(available):
    response = input("Would you like to do something with any of the following friends " + str(', '.join(available)) + "?")
    return response

#lets the user choose which of the nearby friends they want to hang out with
@app.route('/which_friends')
def which_friends(available):
    interested = (input("Who would you like to hang out with from " + str(', '.join(available)) + "?")).split(" ")
    return interested

#notifies the user that all of their friends are busy
@app.route('/busy_friend')
def busy_friend():
    print("Sorry, your friends are busy right now")
  
#update the interest the user has in hanging out with their other friends
#true if they are interested and false if they are not
@app.route('/updateStatusT')
def updateStatusT():
    main_user.update({u'status': True})

#false
@app.route('/updateStatusF')
def updateStatusF():
    main_user.update({u'status': False})
    
#check to see which of the friends also are interested in the user
@app.route('/match_responses')
def match_responses(interested):
	mutual = []
	for doc in docs:
		if doc.id in interested and doc.id in available:
			main_user.update({u'status': True})
			if (doc.to_dict()).get('status'):
				mutual.append(doc.id)
	return mutual
    
#sort through the friends the user wants to hang out and returns the friends that also want to hang out with the user
@app.route('/available_friends')
def available_friends(mutual):

	if len(mutual) == 0:
		busy_friend()
	#if one friend
	elif len(mutual) == 1:
		print(mutual[0] + " is free to hang out!")
	else:
		i = 1
		for friend in mutual:
			if len(mutual) == i:
				if len(mutual) == 2:
					print(" and " + mutual[1] + " are free to hang out")
				else:
					print(",and " + friend, end = "")
			else:
				i += 1
				print(friend, end = "")
		print(" are also free!", end = "")
  
#this returns the dictionary with all of the traits of the users friends
@app.route('/docelements')
def docelements():
    elements = []
    for doc in docs:
        elements.append((doc.id)(doc.get_dict))
    return elements


#check the interest the users friends have in hanging out with the user
@app.route('/getStatus')
def getStatus(element):
    val = (element.to_dict()).get('status')
    return val

#sets a 5 minute time as to not constantly bother the user with notifications
@app.route('/fivesleep')
def fivesleep():
	time.sleep(5*60)
 
#set a thirty mionute timer to not annoy the user with notifications
@app.route('/thirtysleep')
def thirtysleep():
    time.sleep(30*60*60)
    


### MAIN
# localfriends = makeconnections()
# response = ask_free()
# #not free
# if response == 'no':
# 	not_free()

# #yes free
# elif response == 'yes':
# 	#set busy to false indicating not busy  
# 	update_busy()

# 	#search through database for other friends with yes
# 	available = get_available(localfriends)

# 	#if no one is available
# 	if len(available) == 0:
# 		busy_friend()

# 	#if one friend is available
# 	elif len(available) == 1:
# 		response = single_friend(available[0])
# 			#wait 5 minutes to search again
# 		if response == 'no':
# 			updateStatusF()
# 			fivesleep()
# 			#recall function
# 		elif response == 'yes':
# 			#set users status to yes and compare with friends status
# 			updateStatusT()
# 			#check if available friend is also interested
# 			elementlist = docelements()
# 			for item in elementlist:
# 				#check that friends status
# 				if item[0] == available[0]:
# 					#if they also want to meet up
# 					if getStatus(item[1]):
# 						#link up with those friends
# 						available_friends(available[0])
# 					else:
# 						busy_friend()
# 						#wait 5 minutes before searching again
# 						fivesleep()
# 						#recall function
# 		else:
# 			bad_entry()
# 			#recall function


# 	#if response is greater than one element
# 	else:
# 		#ask if you want to link up with any of the friends
# 		response = multi_friends(available)
# 		#if response is yes
# 		if response == 'yes':
# 			#which friends
# 			updateStatusT()
# 			interested = which_friends(available)
# 			# print(interested)
# 			mutual = match_responses(interested)
# 			#link up with those friends
# 			available_friends(mutual)

# 		elif response == 'no':
# 			#wait a half hour and then re-search
# 			updateStatusF()
# 			thirtysleep()
# 			#recall function
# 		else:
# 			bad_entry()
# 			#recall function

# else:
# 	bad_entry()
# 	#recall function
