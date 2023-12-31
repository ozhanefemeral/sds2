from flask import Flask, request, jsonify
import NISTtests

app = Flask(__name__)


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


if __name__ == "__main__":
    # for debugging locally
    #app.run(debug=True)
    
    #for production
    app.run(host='0.0.0.0', port=5000)