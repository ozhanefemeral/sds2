

import time
import unittest

import requests

class TestTesterClass(unittest.TestCase):

    def testFrequencyMonobitTestEndpoint(self):
        start = time.time()
        response = requests.post("http://127.0.0.1:5001/frequencyMonobitTest", json={"sequence": pi_list})
        end = time.time()
        pval = response.json()["pval"]
        result = response.json()["result"]
        self.assertEqual(round(pval, 6), 0.578211)
        self.assertEqual(result, "1/1")
        print("testFrequencyMonobitTestEndpoint:", end - start)
    
    def testFrequencyTestWithinBlockEndpoint(self):
        start = time.time()
        response = requests.post("http://127.0.0.1:5001/frequencyTestWithinBlock", json={"sequence": pi_list})
        end = time.time()
        pval = response.json()["pval"]
        result = response.json()["result"]
        self.assertEqual(round(pval, 6), 0.380615)
        self.assertEqual(result, "1/1")
        print("testFrequencyTestWithinBlockEndpoint:", end - start)
    
    def testRunsTestEndpoint(self):
        start = time.time()
        response = requests.post("http://127.0.0.1:5001/runsTest", json={"sequence": pi_list})
        end = time.time()
        pval = response.json()["pval"]
        result = response.json()["result"]
        self.assertEqual(round(pval, 6), 0.419268)
        self.assertEqual(result, "1/1")
        print("testRunsTestEndpoint:", end - start)

    def testLongestRunOfOnesInABlockTestEndpoint(self):
        start = time.time()
        response = requests.post("http://127.0.0.1:5001/longestRunOfOnesInABlockTest", json={"sequence": pi_list})
        end = time.time()
        pval = response.json()["pval"]
        result = response.json()["result"]
        self.assertEqual(round(pval, 6), 0.024390)
        self.assertEqual(result, "1/1")
        print("testLongestRunOfOnesInABlockTestEndpoint:", end - start)

    def testBinaryMatrixRankTestEndpoint(self):
        start = time.time()
        response = requests.post("http://127.0.0.1:5001/binaryMatrixRankTest", json={"sequence": pi_list})
        end = time.time()
        pval = response.json()["pval"]
        result = response.json()["result"]
        self.assertEqual(round(pval, 3), 0.084)
        self.assertEqual(result, "1/1")
        print("testBinaryMatrixRankTestEndpoint:", end - start)

    def testDiscreteFourierTransformTestEndpoint(self):
        start = time.time()
        response = requests.post("http://127.0.0.1:5001/discreteFourierTransformTest", json={"sequence": pi_list})
        end = time.time()
        pval = response.json()["pval"]
        result = response.json()["result"]
        self.assertEqual(round(pval, 6), 0.010186)
        self.assertEqual(result, "1/1")
        print("testDiscreteFourierTransformTestEndpoint:", end - start)

    def testNonOverlappingTemplateMatchingTestEndpoint(self):
        start = time.time()
        response = requests.post("http://127.0.0.1:5001/nonOverlappingTemplateMatchingTest", json={"sequence": pi_list})
        end = time.time()
        pval = response.json()["pval"]
        result = response.json()["result"]
        self.assertEqual(round(pval, 6), 0.165757)
        self.assertEqual(result, "1/1")
        print("testNonOverlappingTemplateMatchingTestEndpoint:", end - start)

    def testOverlappingTemplateMatchingTestEndpoint(self):
        start = time.time()
        response = requests.post("http://127.0.0.1:5001/overlappingTemplateMatchingTest", json={"sequence": pi_list})
        end = time.time()
        pval = response.json()["pval"]
        result = response.json()["result"]
        self.assertEqual(round(pval, 6), 0.296897)
        self.assertEqual(result, "1/1")
        print("testOverlappingTemplateMatchingTestEndpoint:", end - start)

    def testMaurersUniversalStatisticalTestEndpoint(self):
        start = time.time()
        response = requests.post("http://127.0.0.1:5001/maurersUniversalStatisticalTest", json={"sequence": pi_list})
        end = time.time()
        pval = response.json()["pval"]
        result = response.json()["result"]
        self.assertEqual(round(pval, 6), 0.669012)
        self.assertEqual(result, "1/1")
        print("testMaurersUniversalStatisticalTestEndpoint:", end - start)

    def testSerialTestEndpoint(self):
        start = time.time()
        response = requests.post("http://127.0.0.1:5001/serialTest", json={"sequence": pi_list})
        end = time.time()
        pval = response.json()["pval"]
        result = response.json()["result"]
        self.assertEqual(round(pval, 6), 0.143005)
        self.assertEqual(result, "1/1")
        print("testSerialTestEndpoint:", end - start)

    def testApproximateEntropyTestEndpoint(self):
        start = time.time()
        response = requests.post("http://127.0.0.1:5001/approximateEntropyTest", json={"sequence": pi_list})
        end = time.time()
        pval = response.json()["pval"]
        result = response.json()["result"]
        self.assertEqual(round(pval, 6), 0.361595)
        self.assertEqual(result, "1/1")
        print("testApproximateEntropyTestEndpoint:", end - start)
    
    def testCumulativeSumsForwardTestEndpoint(self):
        start = time.time()
        response = requests.post("http://127.0.0.1:5001/cumulativeSumsForwardTest", json={"sequence": pi_list})
        end = time.time()
        pval = response.json()["pval"]
        result = response.json()["result"]
        self.assertEqual(round(pval, 6), 0.628308)
        self.assertEqual(result, "1/1")
        print("testCumulativeSumsForwardTestEndpoint:", end - start)

    def testCumulativeSumsBackwardTestEndpoint(self):
        start = time.time()
        response = requests.post("http://127.0.0.1:5001/cumulativeSumsBackwardTest", json={"sequence": pi_list})
        end = time.time()
        pval = response.json()["pval"]
        result = response.json()["result"]
        self.assertEqual(round(pval, 6), 0.663369)
        self.assertEqual(result, "1/1")
        print("testCumulativeSumsBackwardTestEndpoint:", end - start)

    def testRandomExcursionsTestEndpoint(self):
        start = time.time()
        response = requests.post("http://127.0.0.1:5001/randomExcursionsTest", json={"sequence": pi_list})
        end = time.time()
        pval = response.json()["pval"]
        result = response.json()["result"]
        self.assertEqual(round(pval['1'], 6), 0.844143)
        self.assertEqual(result, "8/8")
        print("testRandomExcursionsTestEndpoint:", end - start)

    def testRandomExcursionsVariantTestEndpoint(self):
        start = time.time()
        response = requests.post("http://127.0.0.1:5001/randomExcursionsVariantTest", json={"sequence": pi_list})
        end = time.time()
        pval = response.json()["pval"]
        result = response.json()["result"]
        self.assertEqual(round(pval['-1'], 6), 0.760966)
        self.assertEqual(result, "16/18")
        print("testRandomExcursionsVariantTestEndpoint:", end - start)
    



if __name__ == '__main__':
    pi_file = open("data.pi", "r")
    pi_str = pi_file.read()
    pi_str = pi_str.replace("\n", "")
    pi_str = pi_str.replace(" ", "")
    pi_list = [int(i) for i in pi_str]
    pi_list = pi_list[:1000000]
    try:
        response = requests.post("http://127.0.0.1:5001/frequencyMonobitTest", json={"sequence": pi_list})
    except requests.exceptions.ConnectionError:
        print("Server is not running")
        exit()
    unittest.main()