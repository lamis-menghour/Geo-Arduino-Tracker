#include <SoftwareSerial.h>
#include <TinyGPS++.h>

TinyGPSPlus gps;  // Create a TinyGPS++ object to handle GPS data
<<<<<<< HEAD
SoftwareSerial GPSSerial(8, 9);  // RX, TX pins for Neo-6M GPS module (adjust pins as needed)

=======

SoftwareSerial GPSSerial(8, 9);  // RX, TX pins for Neo-6M GPS module (adjust pins as needed)


>>>>>>> 612350d5433bd21565516cf432300dc3ecbf85a0
void setup() {
  Serial.begin(9600);     // Initialize the serial monitor
  GPSSerial.begin(9600);  // Initialize GPS serial communication
}

void loop() {
<<<<<<< HEAD
=======

>>>>>>> 612350d5433bd21565516cf432300dc3ecbf85a0
  while (!gps.location.isValid()) {
    // Keep reading GPS data until a valid fix is obtained
    while (GPSSerial.available()) {
      gps.encode(GPSSerial.read());  // Feed GPS data to TinyGPS++
    }
  }
<<<<<<< HEAD
  // Display GPS data
  // Serial.print("Longitude: ");
  Serial.print(gps.location.lng(), 6);
  Serial.print(",");
  // Serial.print("Latitude: ");
  Serial.println(gps.location.lat(), 6);
=======

  // Display GPS data
  // Serial.print("Latitude: ");
  Serial.print(gps.location.lat(), 6);
  Serial.print(",");
  // Serial.print("Longitude: ");
  Serial.print(gps.location.lng(), 6);
>>>>>>> 612350d5433bd21565516cf432300dc3ecbf85a0
}
