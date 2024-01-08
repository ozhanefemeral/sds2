from algorithms import linear_congruential_generator, shuffle_by_algorithm_B_with_Iterator, shuffle_by_algorithm_M, shuffle_by_algorithm_B, shuffle_by_algorithm_M_with_Iterator
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)

CORS(app)
    
@app.route("/algorithm_M_with_data", methods=["POST"])
def algorithm_M():
    """
    Execute Algorithm M on the provided input data.

    Endpoint: /algorithm_M_with_data
    Method: POST

    Parameters:
    - X (list): The input list of integers for Algorithm M.
    - Y (list): The input list of integers for Algorithm M.
    - k (int): The size of the initial subset used by Algorithm M.
    - n (int): The number of iterations to perform.

    Returns:
    - 200 OK: Returns a JSON response with the shuffled result.
      {
        "success": true,
        "message": "Algorithm M executed successfully",
        "result": [shuffled_data]
      }

    - 400 Bad Request: Returns a JSON response if there are missing or invalid parameters.
      {
        "error": "Missing required parameter: parameter_name"
      }

    - 500 Internal Server Error: Returns a JSON response if an unexpected error occurs.
      {
        "error": "An error occurred: error_message"
      }
    """
    try:
        json_data = request.get_json()
        X = json_data["X"]
        Y = json_data["Y"]
        k = json_data["k"]
        n = json_data["n"]
        result = shuffle_by_algorithm_M(X, Y, k, n)

        response_data = {
            "success": True,
            "message": "Algorithm M executed successfully",
            "result": result
        }

        return jsonify(response_data), 200

    except KeyError as e:
        return jsonify({"error": f"Missing required parameter: {str(e)}"}), 400

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    

@app.route("/algorithm_B_with_data", methods=["POST"])
def algorithm_B():
    """
    Execute Algorithm B on the provided input.

    Endpoint: /algorithm_B
    Method: POST

    Parameters:
    - X (list): The input list of integers.
    - k (int): The size of the initial subset used by the algorithm.
    - n (int): The number of iterations to perform.

    Returns:
    - 200 OK: Returns a JSON response with the shuffled result.
      {
        "success": true,
        "message": "Algorithm B executed successfully",
        "result": [shuffled_data]
      }

    - 400 Bad Request: Returns a JSON response if there are missing or invalid parameters.
      {
        "error": "Missing required parameter: parameter_name"
      }

    - 500 Internal Server Error: Returns a JSON response if an unexpected error occurs.
      {
        "error": "An error occurred: error_message"
      }
    """
    try:
        json_data = request.get_json()
        X = json_data["X"]
        k = json_data["k"]
        n = json_data["n"]
        result = shuffle_by_algorithm_B(X, k, n)

        response_data = {
            "success": True,
            "message": "Algorithm B executed successfully",
            "result": result
        }

        return jsonify(response_data), 200

    except KeyError as e:
        return jsonify({"error": f"Missing required parameter: {str(e)}"}), 400

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    

@app.route("/algorithm_M_without_data", methods=["POST"])

def algorithm_M_without_data():
    """
    Execute Algorithm M without providing input data directly. Instead, the algorithm is driven by the provided parameters to generate sequences using linear congruential generators.

    Endpoint: /algorithm_M_without_data
    Method: POST

    Parameters:
    - aX (int): Multiplier for the linear congruential generator of sequence X.
    - cX (int): Increment for the linear congruential generator of sequence X.
    - mX (int): Modulus for the linear congruential generator of sequence X. mX will be 2^mX.
    - seedX (int): Seed value for the linear congruential generator of sequence X.

    - aY (int): Multiplier for the linear congruential generator of sequence Y.
    - cY (int): Increment for the linear congruential generator of sequence Y.
    - mY (int): Modulus for the linear congruential generator of sequence Y. mY will be 2^mY.
    - seedY (int): Seed value for the linear congruential generator of sequence Y.

    - k (int): The size of the initial subset used by Algorithm M.
    - n (int): The number of iterations to perform.

    Returns:
    - 200 OK: Returns a JSON response with the shuffled result.
      {
        "success": true,
        "message": "Algorithm M executed successfully",
        "result": [shuffled_data]
      }

    - 400 Bad Request: Returns a JSON response if there are missing or invalid parameters.
      {
        "error": "Missing required parameter: parameter_name"
      }

    - 500 Internal Server Error: Returns a JSON response if an unexpected error occurs.
      {
        "error": "An error occurred: error_message"
      }
    """
        
    try:
        json_data = request.get_json()
        aX = json_data["aX"]
        cX = json_data["cX"]
        mX = json_data["mX"]
        mX = 2**mX
        seedX = json_data["seedX"]

        aY = json_data["aY"]
        cY = json_data["cY"]
        mY = json_data["mY"]
        mY = 2**mY
        seedY = json_data["seedY"]
        
        x_gen = linear_congruential_generator(mX, aX, cX, seedX)
        y_gen = linear_congruential_generator(mY, aY, cY, seedY)



        k = json_data["k"]
        n = json_data["n"]
        result = shuffle_by_algorithm_M_with_Iterator(x_gen, y_gen, k, mY, n)

        response_data = {
            "success": True,
            "message": "Algorithm M executed successfully",
            "result": result
        }

        return jsonify(response_data), 200

    except KeyError as e:
        return jsonify({"error": f"Missing required parameter: {str(e)}"}), 400
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    

@app.route("/algorithm_B_without_data", methods=["POST"])
def algorithm_B_without_data():
    """
    Execute Algorithm B without providing input data directly. Instead, the algorithm is driven by the provided parameters to generate a sequence using a linear congruential generator.

    Endpoint: /algorithm_B_without_data
    Method: POST

    Parameters:
    - aX (int): Multiplier for the linear congruential generator of sequence X.
    - cX (int): Increment for the linear congruential generator of sequence X.
    - mX (int): Modulus for the linear congruential generator of sequence X. mX will be 2^mX.
    - seedX (int): Seed value for the linear congruential generator of sequence X.

    - k (int): The size of the initial subset used by Algorithm B.
    - n (int): The number of iterations to perform.

    Returns:
    - 200 OK: Returns a JSON response with the shuffled result.
      {
        "success": true,
        "message": "Algorithm B executed successfully",
        "result": [shuffled_data]
      }

    - 400 Bad Request: Returns a JSON response if there are missing or invalid parameters.
      {
        "error": "Missing required parameter: parameter_name"
      }

    - 500 Internal Server Error: Returns a JSON response if an unexpected error occurs.
      {
        "error": "An error occurred: error_message"
      }
    """
        
    try:
        json_data = request.get_json()
        aX = json_data["aX"]
        cX = json_data["cX"]
        mX = json_data["mX"]
        mX = 2**mX
        seedX = json_data["seedX"]

        x_gen = linear_congruential_generator(mX, aX, cX, seedX)

        k = json_data["k"]
        n = json_data["n"]
        result = shuffle_by_algorithm_B_with_Iterator(x_gen, k, mX, n)

        response_data = {
            "success": True,
            "message": "Algorithm B executed successfully",
            "result": result
        }

        return jsonify(response_data), 200

    except KeyError as e:
        return jsonify({"error": f"Missing required parameter: {str(e)}"}), 400
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


if __name__ == "__main__":
    # for debugging locally
    #app.run(debug=True)
    
    #for production
    app.run(host='0.0.0.0', port=5002)




