//
//  ContentView.swift
//  Around
//
<<<<<<< HEAD
//  Created by Avery Le on 12/24/22.
=======
//  Created by JP Pacheaco on 12/24/22.
>>>>>>> 2689bbc7b6a527bedb0697f9073f16cae38c9ac5
//

import SwiftUI

struct ContentView: View {
    @ObservedObject var locationManager = LocationManager.shared
<<<<<<< HEAD
    var body: some View {
        Group {
            if locationManager.userLocation == nil {
                LocationRequestView()
            } else {
                Text("Hello, world")
=======
    
    var body: some View {
        Group {
            if locationManager.userLocation == nil{
                LocationRequestView()
            }
            else{
                Text("Hello World")
>>>>>>> 2689bbc7b6a527bedb0697f9073f16cae38c9ac5
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
