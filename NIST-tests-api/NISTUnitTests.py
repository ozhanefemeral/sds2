import unittest

from NISTtests import Tester

global pi_list

class TestTesterClass(unittest.TestCase):



    def test_valid_input(self):
        # Test that the class initializes properly with valid input
        valid_input = [0, 1] * 10000
        tester_instance = Tester(valid_input)
        self.assertIsNotNone(tester_instance)

    def test_invalid_input_values(self):
        # Test that ValueError is raised for invalid input values
        invalid_input = [2, 0, 1, 1]
        with self.assertRaises(ValueError):
            Tester(invalid_input)

    def test_invalid_input_length(self):
        # Test that ValueError is raised for input with less than 20000 elements
        short_input = [0, 1] * 9999
        with self.assertRaises(ValueError):
            Tester(short_input)


    def test_frequency_monobit_test_against_pi(self):
        # Test the frequencyMonobitTest method
        # You might want to create test cases for both True and False outcomes
        tester_instance = Tester(pi_list, debug=True)
        pval, _ = tester_instance.frequencyMonobitTest()
        self.assertEqual(round(pval, 6), 0.578211)


    def test_frequency_test_within_block_agains_pi(self):
        # Test the frequencyTestWithinBlock method
        # You might want to create test cases for both True and False outcomes
        tester_instance = Tester(pi_list, debug=True)
        pval, _ = tester_instance.frequencyTestWithinBlock(128)
        self.assertEqual(round(pval, 6), 0.380615)
    
    def test_runs_test_against_pi(self):
        # Test the runsTest method
        # You might want to create test cases for both True and False outcomes
        tester_instance = Tester(pi_list, debug=True)
        pval, _ = tester_instance.runsTest()
        self.assertEqual(round(pval, 6), 0.419268)

    def test_longest_run_ones_in_a_block_test_against_pi(self):
        # Test the longestRunOnesInABlockTest method
        # You might want to create test cases for both True and False outcomes
        tester_instance = Tester(pi_list, debug=True)
        pval, _ = tester_instance.longestRunOfOnesInABlockTest()
        self.assertEqual(round(pval, 6), 0.024390)


    def test_binary_matrix_rank_test_against_pi(self):
        tester_instance = Tester(pi_list, debug=True)
        pval, _ = tester_instance.binaryMatrixRankTest()
        self.assertEqual(round(pval, 3), 0.084)

    def test_discrete_fourier_transform_test_against_pi(self):
        # Test the discreteFourierTransformTest method
        # You might want to create test cases for both True and False outcomes
        tester_instance = Tester(pi_list, debug=True)
        pval, _ = tester_instance.discreteFourierTransformTest()
        self.assertEqual(round(pval, 6), 0.010186)

    def test_non_overlapping_template_matching_test_against_pi(self):
        tester_instance = Tester(pi_list, debug=True)
        pval, _ = tester_instance.nonOverlappingTemplateMatchingTest()
        self.assertEqual(round(pval, 6), 0.165757)
    
    def test_overlapping_template_matching_test_against_pi(self):
        tester_instance = Tester(pi_list, debug=True)
        pval, result = tester_instance.overlappingTemplateMatchingTest()
        self.assertEqual(round(pval, 6), 0.296897)

    def test_maurers_universal_test_against_pi(self):
        tester_instance = Tester(pi_list, debug=True)
        pval, result = tester_instance.maurersUniversalStatisticalTest()
        self.assertEqual(round(pval, 6), 0.669012)

    def test_serial_test_against_pi(self):
        tester_instance = Tester(pi_list, debug=True)
        pval, result = tester_instance.serialTest()
        self.assertEqual(round(pval, 6), 0.143005)
    
    def test_approximate_entropy_test(self):
        tester_instance = Tester(pi_list, debug=True)
        pval, _ = tester_instance.approximateEntropyTest()
        self.assertEqual(round(pval, 6), 0.361595)
    
    def test_cumulative_sums_forward(self):
        tester_instance = Tester(pi_list, debug=True)
        pval, result = tester_instance.cumulativeSumsForwardTest()
        self.assertEqual(round(pval, 6), 0.628308)
    
    def test_cumulative_sums_backward(self):
        tester_instance = Tester(pi_list, debug=True)
        pval, result = tester_instance.cumulativeSumsBackwardTest()
        self.assertEqual(round(pval, 6), 0.663369)
    
    def test_random_excursions_test(self):
        tester_instance = Tester(pi_list, debug=True)
        pval = tester_instance.randomExcursionsTest()
        self.assertEqual(round(pval[1], 6), 0.844143)
    
    def test_random_excursions_variance_test(self):
        tester_instance = Tester(pi_list, debug=True)
        pval = tester_instance.randomExcursionsVariantTest()
        self.assertEqual(round(pval[-1], 6), 0.760966)










        
        

if __name__ == '__main__':

    pi_file = open("data.pi", "r")
    pi_str = pi_file.read()
    pi_str = pi_str.replace("\n", "")
    pi_str = pi_str.replace(" ", "")
    pi_list = [int(i) for i in pi_str]
    pi_list = pi_list[:1000000]
    unittest.main()