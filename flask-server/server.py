<<<<<<< HEAD
from flask import Flask, jsonify
from flask_cors import CORS
=======
# # from flask import Flask

# # app = Flask(__name__)

# # @app.route("/")

# # # def sensor():
# # #     return {"sensor_value" : sensor_value}
# # def home():
# #     return 'Hello, World!'

# # if __name__ == "__main__":
# #     app.run(debug=True)

# # -------------------------
# from flask import Flask, jsonify
# from threading import Thread
# import time

# app = Flask(__name__)

# # Function to periodically update sensor_value from Arduino
# def update_sensor_value():
#     while True:
#         with open('sensor_value.txt', 'r') as file:
#             sensor_value = file.read().strip()
#             file.close()
#         time.sleep(0.5)

# # Start the update_sensor_value function in a separate thread
# update_thread = Thread(target=update_sensor_value)
# update_thread.start()

# @app.route("/sensor")
# def sensor():
#     # Return the latest sensor_value 
#     with open('sensor_value.txt', 'r') as file:
#         sensor_value = file.read().strip()
#         file.close()
#     # return jsonify({"sensor_value": sensor_value})
#     return sensor_value

# if __name__ == "__main__":
#     app.run(debug=True)

# --------------------------------------------------------------------------------
from flask import Flask, jsonify
>>>>>>> 612350d5433bd21565516cf432300dc3ecbf85a0
from threading import Thread
import json
import time
import os

app = Flask(__name__)
<<<<<<< HEAD
CORS(app)

=======
>>>>>>> 612350d5433bd21565516cf432300dc3ecbf85a0

# Function to periodically update location_data from Arduino
def update_location_data():
    while True:
        # Specify the absolute path to the file
<<<<<<< HEAD
        file_path = os.path.abspath("location_data.json")

        # Check if the file exists
        if os.path.exists(file_path):
            # Read the latest location_data from the file
            with open(file_path, "r") as file:
=======
        file_path = os.path.abspath('location_data.json')
        
        # Check if the file exists
        if os.path.exists(file_path):
            # Read the latest location_data from the file
            with open(file_path, 'r') as file:
>>>>>>> 612350d5433bd21565516cf432300dc3ecbf85a0
                location_data = json.load(file)
            print("Location Data:", location_data)
        else:
            print("File not found")
<<<<<<< HEAD

        time.sleep(0.5)


=======
        
        time.sleep(0.5)

>>>>>>> 612350d5433bd21565516cf432300dc3ecbf85a0
# Start the update_location_data function in a separate thread
update_thread = Thread(target=update_location_data)
update_thread.start()

<<<<<<< HEAD

@app.route("/location", methods=["GET"])
def location():
    # Specify the absolute path to the file
    file_path = os.path.abspath("location_data.json")

    # Check if the file exists
    if os.path.exists(file_path):
        # Read the latest location_data from the file
        with open(file_path, "r") as file:
=======
@app.route("/location")
def location():
    # Specify the absolute path to the file
    file_path = os.path.abspath('location_data.json')
    
    # Check if the file exists
    if os.path.exists(file_path):
        # Read the latest location_data from the file
        with open(file_path, 'r') as file:
>>>>>>> 612350d5433bd21565516cf432300dc3ecbf85a0
            location_data = json.load(file)
        return jsonify(location_data)
    else:
        # Return an error response if the file does not exist
        return jsonify({"error": "File not found"})

<<<<<<< HEAD

if __name__ == "__main__":
    app.run(port=5000, debug=True)
=======
if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> 612350d5433bd21565516cf432300dc3ecbf85a0
