from flask import Flask, jsonify
from flask_cors import CORS
from threading import Thread
import json
import time
import os

app = Flask(__name__)
CORS(app)

# Function to periodically update location_data from Arduino
def update_location_data():
    while True:
        # Specify the absolute path to the file
        file_path = os.path.abspath("location_data.json")

        # Check if the file exists
        if os.path.exists(file_path):
            # Read the latest location_data from the file
            with open(file_path, "r") as file:
                location_data = json.load(file)
                print("Location Data:", location_data)
        else:
            print("File not found")

        time.sleep(0.5)

# Start the update_location_data function in a separate thread
update_thread = Thread(target=update_location_data)
update_thread.start()

@app.route("/location", methods=["GET"])
def location():
    # Specify the absolute path to the file
    file_path = os.path.abspath("location_data.json")

    # Check if the file exists
    if os.path.exists(file_path):
        # Read the latest location_data from the file
        with open(file_path, "r") as file:
            location_data = json.load(file)
        return jsonify(location_data)
    else:
        # Return an error response if the file does not exist
        return jsonify({"error": "File not found"})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
