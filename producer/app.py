from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def generate_data():
    """ Generate random log data """
    log_data = {"log": f"Random number: {random.randint(1, 100)}"}
    print(f"Generated Data: {log_data}")  # Log to container output
    return jsonify(log_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
