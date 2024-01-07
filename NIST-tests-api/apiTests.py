import requests
import unittest
global pi_list
global response

class TestTesterClass(unittest.TestCase):

    def test_frequency_monobit_test_against_pi(self):
        pval = response["frequencyMonobitTest"]["pval"]
        self.assertEqual(round(pval, 6), 0.578211)
    def test_frequency_test_within_block_agains_pi(self):
        pval = response["frequencyTestWithinBlock"]["pval"]
        self.assertEqual(round(pval, 6), 0.380615)
    def test_runs_test_against_pi(self):
        pval = response["runsTest"]["pval"]
        self.assertEqual(round(pval, 6), 0.419268)
    def test_longest_run_ones_in_a_block_test_against_pi(self):
        pval = response["longestRunOfOnesInABlockTest"]["pval"]
        self.assertEqual(round(pval, 6), 0.024390)
    def test_binary_matrix_rank_test_against_pi(self):
        pval = response["binaryMatrixRankTest"]["pval"]
        self.assertEqual(round(pval, 3), 0.084)
    def test_discrete_fourier_transform_test_against_pi(self):
        pval = response["discreteFourierTransformTest"]["pval"]
        self.assertEqual(round(pval, 6), 0.010186)
    def test_non_overlapping_template_matching_test_against_pi(self):
        pval = response["nonOverlappingTemplateMatchingTest"]["pval"]
        self.assertEqual(round(pval, 6), 0.165757)
    def test_overlapping_template_matching_test_against_pi(self):
        pval = response["overlappingTemplateMatchingTest"]["pval"]
        self.assertEqual(round(pval, 6), 0.296897)
    def test_maurers_universal_test_against_pi(self):
        pval = response["maurersUniversalStatisticalTest"]["pval"]
        self.assertEqual(round(pval, 6), 0.669012)
    def test_serial_test_against_pi(self):
        pval = response["serialTest"]["pval"]
        self.assertEqual(round(pval, 6), 0.143005)
    def test_approximate_entropy_test_against_pi(self):
        pval = response["approximateEntropyTest"]["pval"]
        self.assertEqual(round(pval, 6), 0.361595)
    def test_cumulative_sums_forward_test_against_pi(self):
        pval = response["cumulativeSumsForwardTest"]["pval"]
        self.assertEqual(round(pval, 6), 0.628308)
    def test_cumulative_sums_backward_test_against_pi(self):
        pval = response["cumulativeSumsBackwardTest"]["pval"]
        self.assertEqual(round(pval, 6), 0.663369)
    def test_random_excursions_test_pvals_against_pi(self):
        pval = response["randomExcursionsTest"]["pval"]
        self.assertEqual(round(pval['1'], 6), 0.844143)
    def test_random_excursions_test_result_against_pi(self):
        result = response["randomExcursionsTest"]["result"]
        self.assertEqual(result, "8/8")
    def test_random_excursions_variant_test_pvals_against_pi(self):
        pval = response["randomExcursionsVariantTest"]["pval"]
        self.assertEqual(round(pval['-1'], 6), 0.760966)
    def test_random_excursions_variant_test_result_against_pi(self):
        result = response["randomExcursionsVariantTest"]["result"]
        self.assertEqual(result, "16/18")


if __name__ == "__main__":
    pi_file = open("data.pi", "r")
    pi_str = pi_file.read()
    pi_str = pi_str.replace("\n", "")
    pi_str = pi_str.replace(" ", "")
    pi_list = [int(i) for i in pi_str]
    pi_list = pi_list[:1000000]
    response = requests.post(
    "http://127.0.0.1:5001/testRandomnessWithNISTPakcage",
    json={
        "sequence": pi_list
    })

    response = response.json()
    unittest.main()