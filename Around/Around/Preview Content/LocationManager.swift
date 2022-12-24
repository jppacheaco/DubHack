//
//  LocationManager.swift
<<<<<<< HEAD
//  Around
//
//  Created by Avery Le on 12/24/22.
//

import CoreLocation

class LocationManager: NSObject, ObservableObject {
    private let manager = CLLocationManager()
    @Published var userLocation: CLLocation?
    static let shared = LocationManager()
    
    override init() {
=======
//  DubProj
//
//  Created by JP Pacheaco on 12/20/22.
//

import CoreLocation
//making it an observable object makes lets it know it is going to be listened to
//this way in other files we can 'observe' it
class LocationManager: NSObject, ObservableObject{
    private let manager = CLLocationManager()
    //published because if lation not allowed we get access then take them back to home screen(want to be able to listen to changes)
    @Published var userLocation: CLLocation?
    //allow us to use this class across the app
    static let shared = LocationManager()
    
    override init(){
>>>>>>> 2689bbc7b6a527bedb0697f9073f16cae38c9ac5
        super.init()
        manager.delegate = self
        manager.desiredAccuracy = kCLLocationAccuracyBest
        manager.startUpdatingLocation()
    }
    
<<<<<<< HEAD
    func requestLocation() {
        manager.requestWhenInUseAuthorization()
    }
}

extension LocationManager: CLLocationManagerDelegate  {
    func locationManager(_ manager: CLLocationManager, didChangeAuthorization status: CLAuthorizationStatus) {
    
        switch status {
        case .notDetermined:
            print("DEBUG: not determined")
        case .restricted:
            print("DEBUG: restricted")
        case .denied:
            print("DEBUG: denied")
        case .authorizedAlways:
            print("DEBUG: always allow")
        case .authorizedWhenInUse:
            print("DEBUG: allow when in use")
=======
    func requestLocation(){
        //if we do always on then it is more taxing on device
        //for our app we need it so that it prompts when there is someone nearby
        //may change functionality of app so that we dont need always on
        manager.requestAlwaysAuthorization()
    }
}
//conform to a protocol
extension LocationManager: CLLocationManagerDelegate{
    //status starts as undetermined, changes if the all access and thats when this func is called
    func locationManager(_ manager: CLLocationManager, didChangeAuthorization status: CLAuthorizationStatus) {
        
        switch status {
            
        case .notDetermined:
            print("Location access: UNDETERMINED")
        case .restricted:
            print("Location access: RESTRICTED")
        case .denied:
            print("Location access: DENIED")
        case .authorizedAlways:
            print("Location access: ALWAYS")
        case .authorizedWhenInUse:
            print("Location access: WHEN IN USE")
        case .authorized:
            print("Location access: AUTHORIZED")
>>>>>>> 2689bbc7b6a527bedb0697f9073f16cae38c9ac5
        @unknown default:
            break
        }
    }
<<<<<<< HEAD
    
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        guard let location = locations.last else {return}
=======
    //when we recieve the users location
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        guard let location = locations.last else{return}
>>>>>>> 2689bbc7b6a527bedb0697f9073f16cae38c9ac5
        self.userLocation = location
    }
}
