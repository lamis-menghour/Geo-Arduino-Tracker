<<<<<<< HEAD
from flask import Flask, jsonify
from flask_cors import CORS
=======
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
