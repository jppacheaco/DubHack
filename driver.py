# // the main where we find responses and 
from threading import local
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time
import runRadius
import findfriends

cred = credentials.Certificate('secretkey.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()
users_ref = db.collection(u'users')
docs = users_ref.stream()

def makeconnections():
	#while there are no friends nearby keep searching
	localfriends = []

	while len(localfriends) == 0:
		localfriends = runRadius.nearby(db)
		if len(localfriends) == 0:
			time.sleep(60)

	# print(localfriends)

	#access firestore data
	main_user = db.collection(u'users').document(u'user1')

	response = input("Are you free to hang out?")

	if response == 'no':
		#change your status to false
		main_user.update({
			u'busy': True
		})
		delay = input("How long will you be busy?")
		#find number and unit from delay
		if 'hour' in delay or 'hr' in delay:
			number = filter(str.isdigit, delay)
			total = number*60*60
		if 'minute' in delay or 'min' in delay:
			number = filter(str.isdigit, delay)
			total = number*60
		if 'sec' in delay or 'second' in delay:
			number = filter(str.isdigit, delay)
			total = number
		#wait designated time and then restart
		time.sleep(total)
		makeconnections()

	else:
		#change your status to true
		main_user.update({u'busy': False})
	
		#search through database for other friends with yes
		list = (db, localfriends)
		available = findfriends.findFriends(list)

		#if no one is available
		if len(available == 0):
			print("All of your friends are busy right now")

		#if one friend is available
		elif len(available) == 1:
			response = input("Would you like to do something with" + available)
			if response == 'no':
				#wait 5 minutes to search again
				time.sleep(5*60)
				makeconnections()
			else:
				#set users status to yes and compare with friends status
				main_user.update({u'status': True})

    
		#if response is greater than one element
		else:
			#ask if you want to link up with any of the friends
			response = input("Would you like to do something with any of the following friends " + available + "?")
			#if response is yes
			if response == 'yes':
				#which friends
				interested = input("Who would you like to hang out with from " + available)
				mutual = []
				for doc in docs:
					if doc.id in interested and doc.id in available:
						main_user.update({u'status': True})
						if (doc.to_dict()).get('status'):
							mutual.add(doc.id)
				#link up with those friends
				print(mutual + "is also free!")

			else:
				time.sleep(5*60*60)
				makeconnections()

