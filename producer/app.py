from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def generate_data():
    """ Generate random log data """
    log_data = {"log": f"Random number: {random.randint(1, 100)}"}
    print(f"Generated Data: {log_data}",flush=True)  #Ensure immediate printing
    return jsonify(log_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
