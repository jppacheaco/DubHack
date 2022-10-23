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

@app.route('/user_info()')
def user_info():
    id = 'unknown user'
    attributes = []
    for doc in docs:
        if doc.id == 'user1':
            id = doc.id
            attributes = doc.to_dict()
    return (id, attributes)

@app.route('/not_free()')
def not_free():
    		#change your status to falseprint("ERROR: Invalid entry")
		main_user.update({
			u'busy': True
		})
		delay = busy_user()
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
			bad_entry()
		time.sleep(total)
		makeconnections()

@app.route('/ask_free')
def ask_free():
    response = input("Are you free to hang out?")
    return response

@app.route('/busy_user')
def busy_user():
	delay = input("How long will you be busy?")
	return delay

@app.route('/bad_entry')
def bad_entry():
    print("ERROR: Invalid entry")

@app.route('/single_friend')
def single_friend(name):
    response = input("Would you like to do something with " + name + "?")
    return response

@app.route('/busy_friend')
def busy_friend():
    print("Sorry, your friends are busy right now")

@app.route('/multi_friend')
def multi_friends(available):
    response = input("Would you like to do something with any of the following friends " + str(', '.join(available)) + "?")
    return response

@app.route('/which_friends')
def which_friends(available):
    interested = (input("Who would you like to hang out with from " + str(', '.join(available)) + "?")).split(" ")
    return interested

@app.route('/update_busy')
def update_busy():
		main_user.update({
			u'busy': True
		})
  
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
  
@app.route('/findfriends')
def get_available(localfriends):
    list = (db, localfriends)
    available = findfriends.findFriends(list)
    return available

@app.route('/makeconnections')
def makeconnections():
	localfriends = []
	#while there are no friends nearby keep searching every minute
	while len(localfriends) == 0:
		localfriends = runRadius.nearby(db)
		if len(localfriends) == 0:
			time.sleep(60)
   
	return localfriends
	#access firestore data
 
@app.route('/fivesleep')
def fivesleep():
	time.sleep(5*60)

@app.route('/updateStatusT')
def updateStatusT():
    main_user.update({u'status': True})
    
@app.route('/docelements')
def docelements():
    elements = []
    for doc in docs:
        elements.append((doc.id)(doc.get_dict))
    return elements

@app.route('/getStatus')
def getStatus(element):
    val = (element.to_dict()).get('status')
    return val

@app.route('/updateStatusF')
def updateStatusF():
    main_user.update({u'status': False})
    

@app.route('/match_responses')
def match_responses(interested):
	mutual = []
	for doc in docs:
		if doc.id in interested and doc.id in available:
			main_user.update({u'status': True})
			if (doc.to_dict()).get('status'):
				mutual.append(doc.id)
	return mutual
    
@app.route('/thirtysleep')
def thirtysleep():
    time.sleep(30*60*60)
    

### MAIN
localfriends = makeconnections()
response = ask_free()
#not free
if response == 'no':
	not_free()

#yes free
elif response == 'yes':
	#set busy to false indicating not busy
	update_busy()

	#search through database for other friends with yes
	available = get_available(localfriends)

	#if no one is available
	if len(available) == 0:
		busy_friend()

	#if one friend is available
	elif len(available) == 1:
		response = single_friend(available[0])
			#wait 5 minutes to search again
		if response == 'no':
			updateStatusF()
			fivesleep()
			#recall function
		elif response == 'yes':
			#set users status to yes and compare with friends status
			updateStatusT()
			#check if available friend is also interested
			elementlist = docelements()
			for item in elementlist:
				#check that friends status
				if item[0] == available[0]:
					#if they also want to meet up
					if getStatus(item[1]):
						#link up with those friends
						available_friends(available[0])
					else:
						busy_friend()
						#wait 5 minutes before searching again
						fivesleep()
						#recall function
		else:
			bad_entry()
			#recall function


	#if response is greater than one element
	else:
		#ask if you want to link up with any of the friends
		response = multi_friends(available)
		#if response is yes
		if response == 'yes':
			#which friends
			updateStatusT()
			interested = which_friends(available)
			# print(interested)
			mutual = match_responses(interested)
			#link up with those friends
			available_friends(mutual)

		elif response == 'no':
			#wait a half hour and then re-search
			updateStatusF()
			thirtysleep()
			#recall function
		else:
			bad_entry()
			#recall function

else:
	bad_entry()
	#recall function

