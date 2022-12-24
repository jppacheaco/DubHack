//
//  getRadius.swift
//  Around2.0
//
//  Created by JP Pacheaco on 12/22/22.
//

import CoreLocation
import SwiftUI

func inRadius()-> Array<Any>{
    
    @ObservedObject var manager = LocationManager.shared
    
    
    let current = manager.userLocation
    
    let f1 = CLLocation(latitude: 27.654, longitude: 26.784)
    let f2 = CLLocation(latitude: 27.654, longitude: 26.784)
    let f3 = CLLocation(latitude: 27.654, longitude: 26.784)
    
    let locations = [CLLocation](arrayLiteral: f1, f2, f3)
    
    var closeBy = [CLLocation]()
    
    for item in locations{
        let meters = current!.distance(from: item)
        if meters < 100{
            closeBy.append(item)
        }
    }
    
    return closeBy
                
}
