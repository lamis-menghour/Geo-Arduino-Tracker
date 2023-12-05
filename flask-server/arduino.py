# import serial
# import time

# # Open a serial connection to the Arduino
# arduino = serial.Serial("COM5", 9600)

# try:
#     while True:
#         # Read and print the sensor value
#         sensor_value = arduino.readline().decode('utf-8').strip()
#         print("Sensor Value:", sensor_value)

#         # Write the sensor value to a file
#         with open('sensor_value.txt', 'w') as file:
#             file.write(sensor_value)

#         time.sleep(1)

# except KeyboardInterrupt:
#     # Close the serial connection on KeyboardInterrupt (Ctrl+C)
#     arduino.close()
#     print("Serial port closed.")

# --------------------------------------------------------------------------------

import serial
import json
import time

# Open a serial connection to the Arduino
arduino = serial.Serial("COM5", 9600)

try:
    while True:
        # Read and print the sensor value
        sensor_data = arduino.readline().decode('utf-8').strip()
        print("GPS Data:", sensor_data)

        # Split the sensor data into latitude and longitude
        latitude, longitude = map(float, sensor_data.split(','))

        # Create a dictionary with latitude and longitude
        location_data = {"Latitude": latitude, "Longitude": longitude}

        # Write the location data to a JSON file
        with open('location_data.json', 'w') as file:
            json.dump(location_data, file)

        time.sleep(1)

except KeyboardInterrupt:
    # Close the serial connection on KeyboardInterrupt (Ctrl+C)
    arduino.close()
    print("Serial port closed.")
