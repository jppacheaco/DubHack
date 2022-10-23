#return the list of friends that are in the radius and not busy

#
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#access firestore data
cred = credentials.Certificate('secretkey.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()
users_ref = db.collection(u'users')
docs = users_ref.stream()

busylist = []
# statuslist = []

#find which friends are busy
for doc in docs:
    busy = (doc.to_dict()).get('busy')
    busylist.append((doc.id, busy))
    # status = (doc.to_dict()).get('status')
    # statuslist.append((doc.id, status))


def findFriends(friendsnear):
    friendlist = []
    for item in busylist:
        #if nearby friends are not busy return them as an option
        if item[1] == False:
            friendlist.append(item[0])
        #if nearby friends busy status is null
    return friendlist
