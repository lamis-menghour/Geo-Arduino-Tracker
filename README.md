# Geo-Arduino-Tracker

Objective: 
This project builds a simple system to track the real-time location of an Arduino board equipped with a NEO-6M GPS module. GPS data is streamed and automatically visualized on a map website, offering instant insight into the tracked object's position.
The Arduino consistently reads data from the sensor, Python manages communication with the Arduino, and Flask delivers this data to the React frontend for display. 

Details:

1. Arduino:
-	Wrote an Arduino script (arduino_GPS.ino) to read data from the GPS Module. 

2. Python:
-	Created a Python script (arduino.py) to continuously read the sensor value from the Arduino via serial communication.
-	The script writes the sensor value to a JSON file (location_data.json) for sharing data with other applications.

3. Flask Web Server: 
-	Implemented a Flask web server (server.py) with an endpoint (/location) to serve the latest sensor value.
-	Used a separate thread to periodically update the sensor value from the Arduino script.

4. React: 
-	Developed a React component (App.js) to fetch and display the sensor value from the Flask web server.
-	Utilized useEffect to initiate the fetch operation on component mount and whenever the sensor value changes.
-	Incorporated conditional rendering to handle loading states.
