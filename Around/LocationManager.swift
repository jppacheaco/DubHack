//
//  LocationManager.swift
//  Around
//
//  Created by JP Pacheaco on 12/20/22.
//

import Foundation
import CoreLocation

class LocationManager: NSObject, CLLocationManagerDelegate{
    static let shared = LocationManager()
    
    let manager = CLLocationManager()
    
    public func getUserLocation(completion: @escaping ((CLLocation)->Void)){
        manager.requestAlwaysAuthorization()
        manager.delegate = self
        manager.startUpdatingLocation()
        
        func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]){
            guard let location = locations.first else{
                return
            }
            completion?(location)
            manager.stopUpdatingLocation()
        }
    }
        
}
