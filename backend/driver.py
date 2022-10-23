#the main where we find responses and 
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time
import re

#helper files
import backend.runRadius as runRadius
import backend.findfriends as findfriends


cred = credentials.Certificate('secretkey.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()
users_ref = db.collection(u'users')
docs = users_ref.stream()

def makeconnections():
	localfriends = []
	available = []

	#while there are no friends nearby keep searching every minute
	while len(localfriends) == 0:
		localfriends = runRadius.nearby(db)
		if len(localfriends) == 0:
			time.sleep(60)

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
			print("ERROR: Invalid entry. We'll ask again. Please enter a number and time unit (ex. 10 min")
		time.sleep(total)
		makeconnections()

	elif response == 'yes':
		#set busy to false indicating not busy
		main_user.update({u'busy': False})
	
		#search through database for other friends with yes
		list = (db, localfriends)
		available = findfriends.findFriends(list)

		#if no one is available
		if len(available) == 0:
			print("All of your friends are busy right now")

		#if one friend is available
		elif len(available) == 1:
			response = input("Would you like to do something with " + str(available[0]) + "?")
			if response == 'no':
				#wait 5 minutes to search again
				time.sleep(5*60)
				makeconnections()
			elif response == 'yes':
				#set users status to yes and compare with friends status
				main_user.update({u'status': True})
				#check if available friend is also interested
				for doc in docs:
					#check that friends status
					if doc.id == available[0]:
						#if they also want to meet up
						if (doc.to_dict()).get('status'):
							#link up with those friends
							print(str(available[0]) + " is also free!")
						else:
							print("Sorry, your friend is busy at the moment.")
							#wait 5 minutes before searching again
							time.sleep(5*60*60)
							makeconnections()
			else:
				print("ERROR: Invalid response")
				makeconnections()

    
		#if response is greater than one element
		else:
			#ask if you want to link up with any of the friends
			response = input("Would you like to do something with any of the following friends " + str(', '.join(available)) + "?")
			#if response is yes
			if response == 'yes':
				#which friends
				interested = (input("Who would you like to hang out with from " + str(', '.join(available)) + "?")).split(" ")
				# print(interested)
				mutual = []
				for doc in docs:
					if doc.id in interested and doc.id in available:
						main_user.update({u'status': True})
						if (doc.to_dict()).get('status'):
							mutual.append(doc.id)
				#link up with those friends
				i = 1
				for friend in mutual:
					if len(mutual) == i:
						if len(mutual) == 1:
							print(friend + " is free to hang out!")
						elif len(mutual) == 2:
							print(" and " + mutual[1] + " are free to hang out")
						else:
							print(",and " + friend, end = "")
					else:
						i += 1
						print(friend, end = "")
				print(" are also free!", end = "")

			elif response == 'no':
				#wait a half hour and then re-search
				time.sleep(30*60*60)
				makeconnections()
	
			else:
				print("ERROR: Invalid response")
				makeconnections()
	else:
		print("ERROR: Invalid response")
		makeconnections()

makeconnections()
