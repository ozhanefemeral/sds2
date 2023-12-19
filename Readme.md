To run api for McLaren-Marsaglia and Bays-Durham algorithms
1. navigate to working directory 'MM-BD-API'
2. run 'docker build -t algorithms-mm-bd-api .'
3. run 'docker run -p 5000:5000 algorithms-mm-bd-api'


api is hosted on localhost:5000

api has 4 endpoints which all accepts POST requests with json body theirs specification goes as follow:
 - /algorithm_B_with_data:
    Execute Algorithm B on the provided input.

    Endpoint: /algorithm_B
    Method: POST

    Parameters:
    - X (list): The input list of integers.
    - k (int): The size of the initial subset used by the algorithm.
    - mod_pow (int): The power for 2^mod, where mod is the modulus used by the algorithm.
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
 - /alogrithm_B_without_data:
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
 - /algorithm_M_with_data:
    Execute Algorithm M on the provided input data.

    Endpoint: /algorithm_M_with_data
    Method: POST

    Parameters:
    - X (list): The input list of integers for Algorithm M.
    - Y (list): The input list of integers for Algorithm M.
    - k (int): The size of the initial subset used by Algorithm M.
    - mod_Y_pow (int): The power for 2^mod_Y, where mod_Y is the modulus used by Algorithm M.
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
 - /alogrithm_M_without_data:
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

