#return the list of friends that are in the radius and not busy

def findFriends(list):
    db = list[0]
    localfriends = list[1]
    users_ref = db.collection(u'users')
    docs = users_ref.stream()

    busylist = []

    #find which friends are busy
    for doc in docs:
        if doc.id in localfriends:
            busy = (doc.to_dict()).get('busy')
            busylist.append((doc.id, busy))

    friendlist = []
    for item in busylist:
        #if nearby friends are not busy return them as an option
        if item[1] == False:
            friendlist.append(item[0])
        #if nearby friends busy status is null
    return friendlist
