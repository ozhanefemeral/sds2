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
    - There are some shenanigans with randomExcursionsVariantTest either because of implementation or because of the test itself so you may ignore the p-values at states -9 and 9 thus result 16/18 should be considered that input sequence is random.
    - "pval" == -1 (same for "result" == "-1/y") means that the test was not executed because of too small input sequence.
      
There is also endpoint for each test separately (below is list of them (base url is 'http://localhost:5001'))
 - /frequencyMonobitTest
 - /frequencyTestWithinBlock
 - /runsTest
 - /longestRunOfOnesInABlockTest
 - /binaryMatrixRankTest
 - /discreteFourierTransformTest
 - /nonOverlappingTemplateMatchingTest
 - /overlappingTemplateMatchingTest
 - /maurersUniversalStatisticalTest
 - /serialTest
 - /approximateEntropyTest
 - /cumulativeSumsForwardTest
 - /cumulativeSumsBackwardTest
 - /randomExcursionsTest
 - /randomExcursionsVariantTest

all of them (except randomExcursionsTest and randomExcursionsVariantTest) takes same inputs and returns same outputs here is example documentation of endpoint

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

Below is documentation of randomExcursionsVariantTest (randomExcursionsTest documentation looks preety much the same)

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


Below are tests with times it took to run them in ascending order hence that it is the order in which GUI should call tests (on first 1000000 bits of binary expansion of pi)
 - FrequencyMonobitTest 0.32040977478027344
 - LongestRunOfOnesInABlockTest 0.3401670455932617
 - FrequencyTestWithinBlock 0.4076673984527588
 - RunsTest 0.41521120071411133
 - DiscreteFourierTransformTest 0.5124905109405518
 - MaurersUniversalStatisticalTest 0.5718038082122803
 - RandomExcursionsVariantTest 0.7407591342926025
 - CumulativeSumsForwardTest 0.7692513465881348
 - CumulativeSumsBackwardTest 0.772552490234375
 - RandomExcursionsTest 0.8859479427337646
 - SerialTest 1.5594747066497803
 - BinaryMatrixRankTest 1.7622203826904297
 - NonOverlappingTemplateMatchingTest 2.0884406566619873
 - OverlappingTemplateMatchingTest 2.1745798587799072
 - ApproximateEntropyTest 5.110479831695557