<<<<<<< HEAD
=======
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

>>>>>>> 612350d5433bd21565516cf432300dc3ecbf85a0
import serial
import json
import time

# Open a serial connection to the Arduino
<<<<<<< HEAD
arduino = serial.Serial("COM4", 9600)
=======
arduino = serial.Serial("COM5", 9600)
>>>>>>> 612350d5433bd21565516cf432300dc3ecbf85a0

try:
    while True:
        # Read and print the sensor value
<<<<<<< HEAD
        sensor_data = arduino.readline().decode("utf-8").strip()
        print("GPS Data:", sensor_data)

        # Split the sensor data into latitude and longitude
        longitude, latitude = map(float, sensor_data.split(","))

        # Create a dictionary with latitude and longitude
        location_data = {"longitude": longitude, "latitude": latitude}

        # Write the location data to a JSON file
        with open("location_data.json", "w") as file:
=======
        sensor_data = arduino.readline().decode('utf-8').strip()
        print("GPS Data:", sensor_data)

        # Split the sensor data into latitude and longitude
        latitude, longitude = map(float, sensor_data.split(','))

        # Create a dictionary with latitude and longitude
        location_data = {"Latitude": latitude, "Longitude": longitude}

        # Write the location data to a JSON file
        with open('location_data.json', 'w') as file:
>>>>>>> 612350d5433bd21565516cf432300dc3ecbf85a0
            json.dump(location_data, file)

        time.sleep(1)

except KeyboardInterrupt:
    # Close the serial connection on KeyboardInterrupt (Ctrl+C)
    arduino.close()
    print("Serial port closed.")
