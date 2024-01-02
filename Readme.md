To run api for NIST tests

navigate to working directory
run 'docker build -t nist-tests-api .'
run 'docker run -p 5001:5001 nist-tests-api'

api is hosted on localhost:5001

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
      