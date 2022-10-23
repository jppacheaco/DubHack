import geopy.distance
import geocoder
from firebase_admin import db
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import haversine as hs
g = geocoder.ip('me')

cred = credentials.Certificate('secretkey.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

users_ref = db.collection(u'users')

main_user = db.collection(u'users').document(u'user1')
main_user.update({
    u'location': g.latlng
})

test_user = db.collection(u'users').document(u'user2')
test_user.update({
    u'location': [-80,45]
})

test_user2 = db.collection(u'users').document(u'user3')
test_user2.update({
    u'location': [47.6553,-122.3035]
})

docs = users_ref.stream()

userid = []
attributes = []
friends = []

for doc in docs:
    comp_location = (doc.to_dict()).get('location')
    # comp_dist = hs.haversine(g.latlng,comp_location)
    comp_dist = geopy.distance.geodesic(g.latlng, comp_location).miles
    if comp_dist < 10:
        friends.append(doc.id)
