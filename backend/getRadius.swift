import CoreLocation
import MapKit


// Create a CLLocationManager and assign a delegate
let long = 0.0
let lat = 0.0
let locationManager = CLLocationManager()
locationManager.delegate = self

// Request a user’s location once
locationManager.requestLocation()

func locationManager(
    _ manager: CLLocationManager,
    didUpdateLocations locations: [CLLocation]
) {
    if let location = locations.first {
        lat = location.coordinate.latitude
        long = location.coordinate.longitude
        // Handle location update
    }
}
func locationManager(
    _ manager: CLLocationManager,
    didFailWithError error: Error
) {
    // Handle failure to get a user’s location
}
var coordinates = (long, lat)

print(coordinates)
