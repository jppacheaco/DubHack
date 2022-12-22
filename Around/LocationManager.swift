//
//  LocationManager.swift
//  DubProj
//
//  Created by JP Pacheaco on 12/20/22.
//


import Foundation
import CoreLocation

class LocationManager: NSObject, ObservableObject{
    private let manager = CLLocationManager()
    //published because if lation not allowed we get access then take them back to home screen(want to be able to listen to changes)
    @Published var userLocation: CLLocation?
    //allow us to use this class across the app
    static let shared = LocationManager()
    
    override init(){
        super.init()
        manager.delegate = self
        manager.desiredAccuracy = kCLLocationAccuracyBest
        manager.startUpdatingLocation()
    }
    
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
        @unknown default:
            break
        }
    }
    //when we recieve the users location
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        guard let location = locations.last else{return}
        self.userLocation = location
    }
}
