import serial
import json
import time

# Open a serial connection to the Arduino
arduino = serial.Serial("COM4", 9600)


try:
    while True:
        # Read and print the sensor value
        sensor_data = arduino.readline().decode("utf-8").strip()
        print("GPS Data:", sensor_data)

        # Split the sensor data into latitude and longitude
        longitude, latitude = map(float, sensor_data.split(","))

        # Create a dictionary with latitude and longitude
        location_data = {"longitude": longitude, "latitude": latitude}

        # Write the location data to a JSON file
        with open("location_data.json", "w") as file:
            json.dump(location_data, file)

        time.sleep(1)

except KeyboardInterrupt:
    # Close the serial connection on KeyboardInterrupt (Ctrl+C)
    arduino.close()
    print("Serial port closed.")
