import geopy.distance
import geocoder

def nearby(db):
    
    g = geocoder.ip('me')

    users_ref = db.collection(u'users')

    main_user = db.collection(u'users').document(u'user1')
    main_user.update({
        u'location': g.latlng
    })

    docs = users_ref.stream()

    friends = []

    for doc in docs:
        comp_location = (doc.to_dict()).get('location')
        comp_dist = geopy.distance.geodesic(g.latlng, comp_location).miles
        if comp_dist < 10:
            if doc.id != 'user1':
                friends.append(doc.id)
    
    return friends
