//
//  ContentView.swift
//  Around
//
//  Created by JP Pacheaco on 12/24/22.
//

import SwiftUI

struct ContentView: View {
    @ObservedObject var locationManager = LocationManager.shared
    
    var body: some View {
        Group {
            if locationManager.userLocation == nil{
                LocationRequestView()
            }
            else{
                Text("Hello World")
                    .padding()
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
