#include <SoftwareSerial.h>
#include <TinyGPS++.h>

TinyGPSPlus gps;  // Create a TinyGPS++ object to handle GPS data

SoftwareSerial GPSSerial(8, 9);  // RX, TX pins for Neo-6M GPS module (adjust pins as needed)


void setup() {
  Serial.begin(9600);     // Initialize the serial monitor
  GPSSerial.begin(9600);  // Initialize GPS serial communication
}

void loop() {

  while (!gps.location.isValid()) {
    // Keep reading GPS data until a valid fix is obtained
    while (GPSSerial.available()) {
      gps.encode(GPSSerial.read());  // Feed GPS data to TinyGPS++
    }
  }

  // Display GPS data
  // Serial.print("Latitude: ");
  Serial.print(gps.location.lat(), 6);
  Serial.print(",");
  // Serial.print("Longitude: ");
  Serial.print(gps.location.lng(), 6);
}
