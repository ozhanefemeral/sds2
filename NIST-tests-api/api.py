from flask import Flask, request, jsonify
import NISTtests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/testRandomnessWithNISTPakcage", methods=["POST"])
def testRandomnessWithNISTPakcage():
    """
    Execute NIST tests on the provided input data.

    Endpoint: /testRandomnessWithNISTPakcage
    Method: POST

    Parameters:
    - sequence (list/str): The input list/str of bits for NIST tests.

    Returns:
    - 200 OK: Returns a JSON response with the shuffled result.
      {
        "success": true,
        "message": "Tests from NIST package executed successfully",
        "frequencyMonobitTest": {"pval": float, "result": "0/1"},
        "frequencyTestWithinBlock": {"pval": float, "result": "0/1"},
        "runsTest": {"pval": float, "result": "0/1"},
        "longestRunOfOnesInABlockTest": {"pval": float, "result": "0/1"},
        "binaryMatrixRankTest": {"pval": float, "result": "0/1"},
        "discreteFourierTransformTest": {"pval": float, "result": "0/1"},
        "nonOverlappingTemplateMatchingTest": {"pval": float, "result": "0/1"},
        "overlappingTemplateMatchingTest": {"pval": float, "result": "0/1"},
        "maurersUniversalStatisticalTest": {"pval": float, "result": "0/1"},
        "serialTest": {"pval": float, "result": "0/1"},
        "approximateEntropyTest": {"pval": float, "result": "0/1"},
        "cumulativeSumsForwardTest": {"pval": float, "result": "0/1"},
        "cumulativeSumsBackwardTest": {"pval": float, "result": "0/1"},
        "randomExcursionsTest": {"pval": {"state1": float, "state2": float, ...}, "result": "0/8"},
        "randomExcursionsVariantTest": {"pval": {"state1": float, "state2": float, ...}, "result": "0/18"}
    }

    - 400 Bad Request: Returns a JSON response if there are missing or invalid parameters.
      {
        "error": "Missing required parameter: parameter_name"
      }

    - 500 Internal Server Error: Returns a JSON response if an unexpected error occurs.
      {
        "error": "An error occurred: error_message"
      }
      
      Notes:
        - The "result" field for each test is a string of the form "x/y", where x is the number of tests passed and y is the total number of tests.
        - The "pval" field for each test except randomExcursionsTest and randomExcursionsVariantTest is a float representing the p-value of the test.
        - The "pval" field for randomExcursionsTest and randomExcursionsVariantTest is a dictionary mapping each state to its p-value.
        - There are some shenanigans with randomExcursionsVariantTest either because of implementation or becouse of the test itself so you may ignore the p-values at states -9 and 9 thus result 16/18 should be considered that input sequence is random.
        - "pval" == -1 (same for "result" == "-1/y") means that the test was not executed because of too small input sequence.
      """
    
    try:
        json_data = request.get_json()
        data = json_data["sequence"]
        if type(data) == str:
            data = [int(i) for i in data]
        tester = NISTtests.Tester(data)
        response_data = {
            "success": True,
            "message": "Tests from NIST package executed successfully",
        }
        try:
            pval, result = tester.frequencyMonobitTest()
            result = 1 if result else 0
        except ValueError:
            pval, result = -1, -1
        response_data["frequencyMonobitTest"] = {"pval": pval, "result": f"{result}/1"}
        
        try:
            pval, result = tester.frequencyTestWithinBlock()
            result = 1 if result else 0
        except ValueError:
            pval, result = -1, -1
        response_data["frequencyTestWithinBlock"] = {"pval": pval, "result": f"{result}/1"}
        
        try:
            pval, result = tester.runsTest()
            result = 1 if result else 0
        except ValueError:
            pval, result = -1, -1
        response_data["runsTest"] = {"pval": pval, "result": f"{result}/1"}
        
        try:
            pval, result = tester.longestRunOfOnesInABlockTest()
            result = 1 if result else 0
        except ValueError:
            pval, result = -1, -1
        response_data["longestRunOfOnesInABlockTest"] = {"pval": pval, "result": f"{result}/1"}
        
        try:
            pval, result = tester.binaryMatrixRankTest()
            result = 1 if result else 0
        except ValueError:
            pval, result = -1, -1
        response_data["binaryMatrixRankTest"] = {"pval": pval, "result": f"{result}/1"}
        
        try:
            pval, result = tester.discreteFourierTransformTest()
            result = 1 if result else 0
        except ValueError:
            pval, result = -1, -1
        response_data["discreteFourierTransformTest"] = {"pval": pval, "result": f"{result}/1"}
        
        try:
            pval, result = tester.nonOverlappingTemplateMatchingTest()
            result = 1 if result else 0
        except ValueError:
            pval, result = -1, -1
        response_data["nonOverlappingTemplateMatchingTest"] = {"pval": pval, "result": f"{result}/1"}
        
        try:
            pval, result = tester.overlappingTemplateMatchingTest()
            result = 1 if result else 0
        except ValueError:
            pval, result = -1, -1
        response_data["overlappingTemplateMatchingTest"] = {"pval": pval, "result": f"{result}/1"}
        
        try:
            pval, result = tester.maurersUniversalStatisticalTest()
            result = 1 if result else 0
        except ValueError:
            pval, result = -1, -1
        response_data["maurersUniversalStatisticalTest"] = {"pval": pval, "result": f"{result}/1"}
        
        try:
            pval, result = tester.serialTest()
            result = 1 if result else 0
        except ValueError:
            pval, result = -1, -1
        response_data["serialTest"] = {"pval": pval, "result": f"{result}/1"}
        
        try:
            pval, result = tester.approximateEntropyTest()
            result = 1 if result else 0
        except ValueError:
            pval, result = -1, -1
        response_data["approximateEntropyTest"] = {"pval": pval, "result": f"{result}/1"}
        
        try:
            pval, result = tester.cumulativeSumsForwardTest()
            result = 1 if result else 0
        except ValueError:
            pval, result = -1, -1
        response_data["cumulativeSumsForwardTest"] = {"pval": pval, "result": f"{result}/1"}
        
        try:
            pval, result = tester.cumulativeSumsBackwardTest()
            result = 1 if result else 0
        except ValueError:
            pval, result = -1, -1
        response_data["cumulativeSumsBackwardTest"] = {"pval": pval, "result": f"{result}/1"}
        
        try:
            pval = tester.randomExcursionsTest()
        except ValueError:
            pval = -1
        result = 0
        for key, value in pval.items():
            if value >= 0.01:
                result += 1
        response_data["randomExcursionsTest"] = {"pval": pval, "result": f"{result}/8"}
        
        try:
            pval = tester.randomExcursionsVariantTest()
        except ValueError:
            pval = -1
        result = 0
        for key, value in pval.items():
            if value >= 0.01:
                result += 1
        response_data["randomExcursionsVariantTest"] = {"pval": pval, "result": f"{result}/18"}

        return jsonify(response_data), 200

    except KeyError as e:
        return jsonify({"error": f"Missing required parameter: {str(e)}"}), 400

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route("/frequencyMonobitTest", methods=["POST"])
def frequencyMonobitTestEndpoint():
    """
    Execute the frequency monobit test on the provided input data.

    Endpoint: /frequencyMonobitTest
    Method: POST

    Parameters:
    - sequence (list/str): The input list/str of bits for the test.

    Returns:
    - 200 OK: Returns a JSON response with the test result.
      {
        "success": true,
        "message": "Frequency monobit test executed successfully",
        "pval": float,
        "result": "0/1"
      }

    - 400 Bad Request: Returns a JSON response if there are missing or invalid parameters.
      {
        "error": "Missing required parameter: parameter_name"
      }

    - 500 Internal Server Error: Returns a JSON response if an unexpected error occurs.
      {
        "error": "An error occurred: error_message"
      }
      
      Notes:
        - The "result" field is a string of the form "x/y", where x is the number of tests passed and y is the total number of tests.
        - "pval" == -1 (same for "result" == "-1/y") means that the test was not executed because of too small input sequence.
      """
    
    try:
        json_data = request.get_json()
        data = json_data["sequence"]
        if type(data) == str:
            data = [int(i) for i in data]
        tester = NISTtests.Tester(data)
        response_data = {
            "success": True,
            "message": "Frequency monobit test executed successfully",
        }
        try:
            pval, result = tester.frequencyMonobitTest()
            result = 1 if result else 0
        except ValueError:
            pval, result = -1, -1
        response_data["pval"] = pval
        response_data["result"] = f"{result}/1"
        return jsonify(response_data), 200

    except KeyError as e:
        return jsonify({"error": f"Missing required parameter: {str(e)}"}), 400

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    
@app.route("/frequencyTestWithinBlock", methods=["POST"])
def frequencyTestWithinBlockEndpoint():
    """
    Execute the frequency test within a block on the provided input data.

    Endpoint: /frequencyTestWithinBlock
    Method: POST

    Parameters:
    - sequence (list/str): The input list/str of bits for the test.

    Returns:
    - 200 OK: Returns a JSON response with the test result.
      {
        "success": true,
        "message": "Frequency test within a block executed successfully",
        "pval": float,
        "result": "0/1"
      }

    - 400 Bad Request: Returns a JSON response if there are missing or invalid parameters.
      {
        "error": "Missing required parameter: parameter_name"
      }

    - 500 Internal Server Error: Returns a JSON response if an unexpected error occurs.
      {
        "error": "An error occurred: error_message"
      }
      
      Notes:
        - The "result" field is a string of the form "x/y", where x is the number of tests passed and y is the total number of tests.
        - "pval" == -1 (same for "result" == "-1/y") means that the test was not executed because of too small input sequence.
      """
    
    try:
        json_data = request.get_json()
        data = json_data["sequence"]
        if type(data) == str:
            data = [int(i) for i in data]
        tester = NISTtests.Tester(data)
        response_data = {
            "success": True,
            "message": "Frequency test within a block executed successfully",
        }
        try:
            pval, result = tester.frequencyTestWithinBlock()
            result = 1 if result else 0
        except ValueError:
            pval, result = -1, -1
        response_data["pval"] = pval
        response_data["result"] = f"{result}/1"
        return jsonify(response_data), 200

    except KeyError as e:
        return jsonify({"error": f"Missing required parameter: {str(e)}"}), 400

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route("/runsTest", methods=["POST"])
def runsTestEndpoint():
    """
    Execute the runs test on the provided input data.

    Endpoint: /runsTest
    Method: POST

    Parameters:
    - sequence (list/str): The input list/str of bits for the test.

    Returns:
    - 200 OK: Returns a JSON response with the test result.
      {
        "success": true,
        "message": "Runs test executed successfully",
        "pval": float,
        "result": "0/1"
      }

    - 400 Bad Request: Returns a JSON response if there are missing or invalid parameters.
      {
        "error": "Missing required parameter: parameter_name"
      }

    - 500 Internal Server Error: Returns a JSON response if an unexpected error occurs.
      {
        "error": "An error occurred: error_message"
      }
      
      Notes:
        - The "result" field is a string of the form "x/y", where x is the number of tests passed and y is the total number of tests.
        - "pval" == -1 (same for "result" == "-1/y") means that the test was not executed because of too small input sequence.
      """
    
    try:
        json_data = request.get_json()
        data = json_data["sequence"]
        if type(data) == str:
            data = [int(i) for i in data]
        tester = NISTtests.Tester(data)
        response_data = {
            "success": True,
            "message": "Runs test executed successfully",
        }
        try:
            pval, result = tester.runsTest()
            result = 1 if result else 0
        except ValueError:
            pval, result = -1, -1
        response_data["pval"] = pval
        response_data["result"] = f"{result}/1"
        return jsonify(response_data), 200

    except KeyError as e:
        return jsonify({"error": f"Missing required parameter: {str(e)}"}), 400

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    
@app.route("/longestRunOfOnesInABlockTest", methods=["POST"])
def longestRunOfOnesInABlockTestEndpoint():
    """
    Execute the longest run of ones in a block test on the provided input data.

    Endpoint: /longestRunOfOnesInABlockTest
    Method: POST

    Parameters:
    - sequence (list/str): The input list/str of bits for the test.

    Returns:
    - 200 OK: Returns a JSON response with the test result.
      {
        "success": true,
        "message": "Longest run of ones in a block test executed successfully",
        "pval": float,
        "result": "0/1"
      }

    - 400 Bad Request: Returns a JSON response if there are missing or invalid parameters.
      {
        "error": "Missing required parameter: parameter_name"
      }

    - 500 Internal Server Error: Returns a JSON response if an unexpected error occurs.
      {
        "error": "An error occurred: error_message"
      }
      
      Notes:
        - The "result" field is a string of the form "x/y", where x is the number of tests passed and y is the total number of tests.
        - "pval" == -1 (same for "result" == "-1/y") means that the test was not executed because of too small input sequence.
      """
    
    try:
        json_data = request.get_json()
        data = json_data["sequence"]
        if type(data) == str:
            data = [int(i) for i in data]
        tester = NISTtests.Tester(data)
        response_data = {
            "success": True,
            "message": "Longest run of ones in a block test executed successfully",
        }
        try:
            pval, result = tester.longestRunOfOnesInABlockTest()
            result = 1 if result else 0
        except ValueError:
            pval, result = -1, -1
        response_data["pval"] = pval
        response_data["result"] = f"{result}/1"
        return jsonify(response_data), 200

    except KeyError as e:
        return jsonify({"error": f"Missing required parameter: {str(e)}"}), 400

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    
@app.route("/binaryMatrixRankTest", methods=["POST"])
def binaryMatrixRankTestEndpoint():
    """
    Execute the binary matrix rank test on the provided input data.

    Endpoint: /binaryMatrixRankTest
    Method: POST

    Parameters:
    - sequence (list/str): The input list/str of bits for the test.

    Returns:
    - 200 OK: Returns a JSON response with the test result.
      {
        "success": true,
        "message": "Binary matrix rank test executed successfully",
        "pval": float,
        "result": "0/1"
      }

    - 400 Bad Request: Returns a JSON response if there are missing or invalid parameters.
      {
        "error": "Missing required parameter: parameter_name"
      }

    - 500 Internal Server Error: Returns a JSON response if an unexpected error occurs.
      {
        "error": "An error occurred: error_message"
      }
      
      Notes:
        - The "result" field is a string of the form "x/y", where x is the number of tests passed and y is the total number of tests.
        - "pval" == -1 (same for "result" == "-1/y") means that the test was not executed because of too small input sequence.
      """
    
    try:
        json_data = request.get_json()
        data = json_data["sequence"]
        if type(data) == str:
            data = [int(i) for i in data]
        tester = NISTtests.Tester(data)
        response_data = {
            "success": True,
            "message": "Binary matrix rank test executed successfully",
        }
        try:
            pval, result = tester.binaryMatrixRankTest()
            result = 1 if result else 0
        except ValueError:
            pval, result = -1, -1
        response_data["pval"] = pval
        response_data["result"] = f"{result}/1"
        return jsonify(response_data), 200

    except KeyError as e:
        return jsonify({"error": f"Missing required parameter: {str(e)}"}), 400

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    
@app.route("/discreteFourierTransformTest", methods=["POST"])
def discreteFourierTransformTestEndpoint():
    """
    Execute the discrete Fourier transform test on the provided input data.

    Endpoint: /discreteFourierTransformTest
    Method: POST

    Parameters:
    - sequence (list/str): The input list/str of bits for the test.

    Returns:
    - 200 OK: Returns a JSON response with the test result.
      {
        "success": true,
        "message": "Discrete Fourier transform test executed successfully",
        "pval": float,
        "result": "0/1"
      }

    - 400 Bad Request: Returns a JSON response if there are missing or invalid parameters.
      {
        "error": "Missing required parameter: parameter_name"
      }

    - 500 Internal Server Error: Returns a JSON response if an unexpected error occurs.
      {
        "error": "An error occurred: error_message"
      }
      
      Notes:
        - The "result" field is a string of the form "x/y", where x is the number of tests passed and y is the total number of tests.
        - "pval" == -1 (same for "result" == "-1/y") means that the test was not executed because of too small input sequence.
      """
    
    try:
        json_data = request.get_json()
        data = json_data["sequence"]
        if type(data) == str:
            data = [int(i) for i in data]
        tester = NISTtests.Tester(data)
        response_data = {
            "success": True,
            "message": "Discrete Fourier transform test executed successfully",
        }
        try:
            pval, result = tester.discreteFourierTransformTest()
            result = 1 if result else 0
        except ValueError:
            pval, result = -1, -1
        response_data["pval"] = pval
        response_data["result"] = f"{result}/1"
        return jsonify(response_data), 200

    except KeyError as e:
        return jsonify({"error": f"Missing required parameter: {str(e)}"}), 400

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route("/nonOverlappingTemplateMatchingTest", methods=["POST"])
def nonOverlappingTemplateMatchingTestEndpoint():
    """
    Execute the non overlapping template matching test on the provided input data.

    Endpoint: /nonOverlappingTemplateMatchingTest
    Method: POST

    Parameters:
    - sequence (list/str): The input list/str of bits for the test.

    Returns:
    - 200 OK: Returns a JSON response with the test result.
      {
        "success": true,
        "message": "Non overlapping template matching test executed successfully",
        "pval": float,
        "result": "0/1"
      }
      
      Notes:
        - The "result" field is a string of the form "x/y", where x is the number of tests passed and y is the total number of tests.
        - "pval" == -1 (same for "result" == "-1/y") means that the test was not executed because of too small input sequence or template.
      """
    
    try:
        json_data = request.get_json()
        data = json_data["sequence"]
        if type(data) == str:
            data = [int(i) for i in data]
        tester = NISTtests.Tester(data)
        response_data = {
            "success": True,
            "message": "Non overlapping template matching test executed successfully",
        }
        try:
            pval, result = tester.nonOverlappingTemplateMatchingTest()
            result = 1 if result else 0
        except ValueError:
            pval, result = -1, -1
        except IndexError:
            pval, result = -1, -1
        response_data["pval"] = pval
        response_data["result"] = f"{result}/1"
        return jsonify(response_data), 200
    
    except KeyError as e:
        return jsonify({"error": f"Missing required parameter: {str(e)}"}), 400
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route("/overlappingTemplateMatchingTest", methods=["POST"])
def overlappingTemplateMatchingTestEndpoint():
    """
    Execute the overlapping template matching test on the provided input data.

    Endpoint: /overlappingTemplateMatchingTest
    Method: POST

    Parameters:
    - sequence (list/str): The input list/str of bits for the test.

    Returns:
    - 200 OK: Returns a JSON response with the test result.
      {
        "success": true,
        "message": "Overlapping template matching test executed successfully",
        "pval": float,
        "result": "0/1"
      }
      
      Notes:
        - The "result" field is a string of the form "x/y", where x is the number of tests passed and y is the total number of tests.
        - "pval" == -1 (same for "result" == "-1/y") means that the test was not executed because of too small input sequence or template.
      """
    
    try:
        json_data = request.get_json()
        data = json_data["sequence"]
        if type(data) == str:
            data = [int(i) for i in data]
        tester = NISTtests.Tester(data)
        response_data = {
            "success": True,
            "message": "Overlapping template matching test executed successfully",
        }
        try:
            pval, result = tester.overlappingTemplateMatchingTest()
            result = 1 if result else 0
        except ValueError:
            pval, result = -1, -1
        except IndexError:
            pval, result = -1, -1
        response_data["pval"] = pval
        response_data["result"] = f"{result}/1"
        return jsonify(response_data), 200
    
    except KeyError as e:
        return jsonify({"error": f"Missing required parameter: {str(e)}"}), 400
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route("/maurersUniversalStatisticalTest", methods=["POST"])
def maurersUniversalStatisticalTestEndpoint():
    """
    Execute the Maurer's universal statistical test on the provided input data.

    Endpoint: /maurersUniversalStatisticalTest
    Method: POST

    Parameters:
    - sequence (list/str): The input list/str of bits for the test.

    Returns:
    - 200 OK: Returns a JSON response with the test result.
      {
        "success": true,
        "message": "Maurer's universal statistical test executed successfully",
        "pval": float,
        "result": "0/1"
      }
      
      Notes:
        - The "result" field is a string of the form "x/y", where x is the number of tests passed and y is the total number of tests.
        - "pval" == -1 (same for "result" == "-1/y") means that the test was not executed because of too small block size or input sequence.
      """
    
    try:
        json_data = request.get_json()
        data = json_data["sequence"]
        if type(data) == str:
            data = [int(i) for i in data]
        tester = NISTtests.Tester(data)
        response_data = {
            "success": True,
            "message": "Maurer's universal statistical test executed successfully",
        }
        try:
            pval, result = tester.maurersUniversalStatisticalTest()
            result = 1 if result else 0
        except ValueError:
            pval, result = -1, -1
        except IndexError:
            pval, result = -1, -1
        response_data["pval"] = pval
        response_data["result"] = f"{result}/1"
        return jsonify(response_data), 200
    
    except KeyError as e:
        return jsonify({"error": f"Missing required parameter: {str(e)}"}), 400
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route("/serialTest", methods=["POST"])
def serialTestEndpoint():
    """
    Execute the serial test on the provided input data.

    Endpoint: /serialTest
    Method: POST

    Parameters:
    - sequence (list/str): The input list/str of bits for the test.

    Returns:
    - 200 OK: Returns a JSON response with the test result.
      {
        "success": true,
        "message": "Serial test executed successfully",
        "pval": float,
        "result": "0/1"
      }
      
      Notes:
        - The "result" field is a string of the form "x/y", where x is the number of tests passed and y is the total number of tests.
        - "pval" == -1 (same for "result" == "-1/y") means that the test was not executed because of too small block size or input sequence.
      """
    
    try:
        json_data = request.get_json()
        data = json_data["sequence"]
        if type(data) == str:
            data = [int(i) for i in data]

        tester = NISTtests.Tester(data)
        response_data = {
            "success": True,
            "message": "Serial test executed successfully",
        }
        try:
            pval, result = tester.serialTest()
            result = 1 if result else 0
        except ValueError:
            pval, result = -1, -1
        except IndexError:
            pval, result = -1, -1
        response_data["pval"] = pval
        response_data["result"] = f"{result}/1"
        return jsonify(response_data), 200
    
    except KeyError as e:
        return jsonify({"error": f"Missing required parameter: {str(e)}"}), 400
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    
@app.route("/approximateEntropyTest", methods=["POST"])
def approximateEntropyTestEndpoint():
    """
    Execute the approximate entropy test on the provided input data.

    Endpoint: /approximateEntropyTest
    Method: POST

    Parameters:
    - sequence (list/str): The input list/str of bits for the test.

    Returns:
    - 200 OK: Returns a JSON response with the test result.
      {
        "success": true,
        "message": "Approximate entropy test executed successfully",
        "pval": float,
        "result": "0/1"
      }
      
      Notes:
        - The "result" field is a string of the form "x/y", where x is the number of tests passed and y is the total number of tests.
      """
    
    try:
        json_data = request.get_json()
        data = json_data["sequence"]
        if type(data) == str:
            data = [int(i) for i in data]

        tester = NISTtests.Tester(data)
        response_data = {
            "success": True,
            "message": "Approximate entropy test executed successfully",
        }
        try:
            pval, result = tester.approximateEntropyTest()
            result = 1 if result else 0
        except ValueError:
            pval, result = -1, -1
        except IndexError:
            pval, result = -1, -1
        response_data["pval"] = pval
        response_data["result"] = f"{result}/1"
        return jsonify(response_data), 200
    
    except KeyError as e:
        return jsonify({"error": f"Missing required parameter: {str(e)}"}), 400
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route("/cumulativeSumsForwardTest", methods=["POST"])
def cumulativeSumsForwardTestEndpoint():
    """
    Execute the cumulative sums forward test on the provided input data.

    Endpoint: /cumulativeSumsForwardTest
    Method: POST

    Parameters:
    - sequence (list/str): The input list/str of bits for the test.

    Returns:
    - 200 OK: Returns a JSON response with the test result.
      {
        "success": true,
        "message": "Cumulative sums forward test executed successfully",
        "pval": float,
        "result": "0/1"
      }
      
      Notes:
        - The "result" field is a string of the form "x/y", where x is the number of tests passed and y is the total number of tests.
      """
    
    try:
        json_data = request.get_json()
        data = json_data["sequence"]
        if type(data) == str:
            data = [int(i) for i in data]

        tester = NISTtests.Tester(data)
        response_data = {
            "success": True,
            "message": "Cumulative sums forward test executed successfully",
        }
        try:
            pval, result = tester.cumulativeSumsForwardTest()
            result = 1 if result else 0
        except ValueError:
            pval, result = -1, -1
        except IndexError:
            pval, result = -1, -1
        response_data["pval"] = pval
        response_data["result"] = f"{result}/1"
        return jsonify(response_data), 200
    
    except KeyError as e:
        return jsonify({"error": f"Missing required parameter: {str(e)}"}), 400
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    
@app.route("/cumulativeSumsBackwardTest", methods=["POST"])
def cumulativeSumsBackwardTestEndpoint():
    """
    Execute the cumulative sums backward test on the provided input data.

    Endpoint: /cumulativeSumsBackwardTest
    Method: POST

    Parameters:
    - sequence (list/str): The input list/str of bits for the test.
    
    Returns:
    - 200 OK: Returns a JSON response with the test result.
      {
        "success": true,
        "message": "Cumulative sums backward test executed successfully",
        "pval": float,
        "result": "0/1"
      }
      
      Notes:
        - The "result" field is a string of the form "x/y", where x is the number of tests passed and y is the total number of tests.
      """
    
    try:
        json_data = request.get_json()
        data = json_data["sequence"]
        if type(data) == str:
            data = [int(i) for i in data]

        tester = NISTtests.Tester(data)
        response_data = {
            "success": True,
            "message": "Cumulative sums backward test executed successfully",
        }
        try:
            pval, result = tester.cumulativeSumsBackwardTest()
            result = 1 if result else 0
        except ValueError:
            pval, result = -1, -1
        except IndexError:
            pval, result = -1, -1
        response_data["pval"] = pval
        response_data["result"] = f"{result}/1"
        return jsonify(response_data), 200
    
    except KeyError as e:
        return jsonify({"error": f"Missing required parameter: {str(e)}"}), 400
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    
@app.route("/randomExcursionsTest", methods=["POST"])
def randomExcursionsTestEndpoint():
    """
    Execute the random excursions test on the provided input data.

    Endpoint: /randomExcursionsTest
    Method: POST

    Parameters:
    - sequence (list/str): The input list/str of bits for the test.
    
    Returns:
    - 200 OK: Returns a JSON response with the test result.
      {
        "success": true,
        "message": "Random excursions test executed successfully",
        "pval": {"state1": float, "state2": float, ...},
        "result": "0/8"
      }
      
      Notes:
        - The "result" field is a string of the form "x/y", where x is the number of states with p-value >= 0.01 and y is the total number of states.
        - The "pval" field is a dictionary mapping each state to its p-value.
        - "pval" == -1 (same for "result" == "-1/y") means that the test was not executed because of too small input sequence.
      """
    
    try:
        json_data = request.get_json()
        data = json_data["sequence"]
        if type(data) == str:
            data = [int(i) for i in data]

        tester = NISTtests.Tester(data)
        response_data = {
            "success": True,
            "message": "Random excursions test executed successfully",
        }
        try:
            pval = tester.randomExcursionsTest()
        except ValueError:
            pval = -1
        result = 0
        for key, value in pval.items():
            if value >= 0.01:
                result += 1
        response_data["pval"] = pval
        response_data["result"] = f"{result}/8"
        return jsonify(response_data), 200
    
    except KeyError as e:
        return jsonify({"error": f"Missing required parameter: {str(e)}"}), 400
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    
@app.route("/randomExcursionsVariantTest", methods=["POST"])
def randomExcursionsVariantTestEndpoint():
    """
    Execute the random excursions variant test on the provided input data.

    Endpoint: /randomExcursionsVariantTest
    Method: POST

    Parameters:
    - sequence (list/str): The input list/str of bits for the test.
    
    Returns:
    - 200 OK: Returns a JSON response with the test result.
      {
        "success": true,
        "message": "Random excursions variant test executed successfully",
        "pval": {"state1": float, "state2": float, ...},
        "result": "0/18"
      }
      
      Notes:
        - The "result" field is a string of the form "x/y", where x is the number of states with p-value >= 0.01 and y is the total number of states.
        - The "pval" field is a dictionary mapping each state to its p-value.
        - "pval" == -1 (same for "result" == "-1/y") means that the test was not executed because of too small input sequence.
      """
    
    try:
        json_data = request.get_json()
        data = json_data["sequence"]
        if type(data) == str:
            data = [int(i) for i in data]

        tester = NISTtests.Tester(data)
        response_data = {
            "success": True,
            "message": "Random excursions variant test executed successfully",
        }
        try:
            pval = tester.randomExcursionsVariantTest()
        except ValueError:
            pval = -1
        result = 0
        for key, value in pval.items():
            if value >= 0.01:
                result += 1
        response_data["pval"] = pval
        response_data["result"] = f"{result}/18"
        return jsonify(response_data), 200
    
    except KeyError as e:
        return jsonify({"error": f"Missing required parameter: {str(e)}"}), 400
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    # for debugging locally
    #app.run(debug=True)
    
    #for production
    app.run(host='0.0.0.0', port=5001)