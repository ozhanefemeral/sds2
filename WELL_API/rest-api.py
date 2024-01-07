from flask import Flask, jsonify, request
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def CALL_WELL():
    try:
        data = request.get_json()
        SIZE = data["size"]
        SEED = data["seed"]

        if type(SIZE) is not int or SIZE<0:
            return jsonify({"ERROR": "(!) 'size' must be a non-negative integer"}), 400
        if SIZE > 3000000:
            return jsonify({"ERROR": "(!) 'size' must be a non-negative integer below 3000000 :)"}), 400
        if len(SEED) != 0 and len(SEED) != 16:
            return jsonify({"ERROR": "(!) 'seed' must be an array of 16 non-negative integers or empty"}), 400

        ARGS = list(map(str,[SIZE] + SEED))
        response = subprocess.check_output( ["./well"] + ARGS ).decode('utf-8').split()

        return jsonify(response), 200
    
    except KeyError as e:
        return jsonify({"ERROR": f"(!) missing parameter: {e}"}), 400

    except Exception as e:
        return jsonify({"ERROR": f"(!) server error occurred: {e}"}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)