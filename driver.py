// the main where we find responses and 

import SwiftUI
import FirebaseCore
import FirebaseFirestore
import FirebaseFirestoreSwift

//create instance of FIRDatabaseReference
var ref: DatabaseReference!

ref = Database.database().reference()

//while friends list response is still empty keep searching
let nearby = findfriends ()
while(nearby.count == 0){
    //keep searching 
    nearby = findfriends ()
}
//now we have found a friend
//check if you are free
print("Are you free to hang out?")
let status = readLine
var freelist
if (status == "Yes" || status = "yes"){
    //search for response in nearby list
    for item in nearby{
        //if they are free 
        freelist.append
    }
    //for all who are also free append to freelist
}
if
//if no 
//if response is single element
    //ask if you want to meet up with that friend
    //if yes, link up
    //if no, set a timer for x amount of time
    // when timer is up, restart at top of file
//if response is greater than one element
    //ask if you want to link up with any of the friends
    //if response is yes
        //which friends 
        //link up with those friends
    //if no 
        //set timer
        //when timer is up, restart at top of file
