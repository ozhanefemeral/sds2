import requests
from algorithms import linear_congruential_generator, shuffle_by_algorithm_M


X_gen = linear_congruential_generator(2**32, 2891336453, 3124392467, 4232434)
Y_gen = linear_congruential_generator(2**32, 29943829, 57894311, 47198023)

first_1000000_X = []
first_1000000_X_bits = []
while len(first_1000000_X_bits) < 200000:
    x = next(X_gen)
    first_1000000_X.append(x)
    x_bits = bin(x)[2:]
    first_1000000_X_bits += [int(bit) for bit in x_bits]
print(len(first_1000000_X))

first_1000000_Y = []
first_1000000_Y_bits = []
while len(first_1000000_Y_bits) < 200000:
    y = next(Y_gen)
    first_1000000_Y.append(y)
    y_bits = bin(y)[2:]
    first_1000000_Y_bits += [int(bit) for bit in y_bits]

print(len(first_1000000_Y))


tests = ['frequencyMonobitTest', 'frequencyTestWithinBlock', 'runsTest', 'longestRunOfOnesInABlockTest', 'binaryMatrixRankTest', 'discreteFourierTransformTest', 'nonOverlappingTemplateMatchingTest', 
'overlappingTemplateMatchingTest', 'maurersUniversalStatisticalTest', 'serialTest', 'approximateEntropyTest', 'cumulativeSumsForwardTest', 'cumulativeSumsBackwardTest', 'randomExcursionsTest', 'randomExcursionsVariantTest']
X_gen_results = {}
X_gen_results['randomExcursionsTest'] = []
X_gen_results['randomExcursionsVariantTest'] = []
Y_gen_results = {}
Y_gen_results['randomExcursionsTest'] = []
Y_gen_results['randomExcursionsVariantTest'] = []
for test in tests:
    response = requests.post("http://localhost:5001/" + test, json={"sequence": first_1000000_X_bits})
    if test == 'randomExcursionsTest' or test == 'randomExcursionsVariantTest':
            for key, value in response.json()['pval'].items():
                X_gen_results[test].append(round(value, 6))
    else:
        pval = round(response.json()['pval'], 6)
        X_gen_results[test] = pval
    response = requests.post("http://localhost:5001/" + test, json={"sequence": first_1000000_Y_bits})
    if test == 'randomExcursionsTest' or test == 'randomExcursionsVariantTest':
            for key, value in response.json()['pval'].items():
                Y_gen_results[test].append(round(value, 6))
    else:
        pval = round(response.json()['pval'], 6)
        Y_gen_results[test] = pval

shuffled_result_bits = []
shuffled_result = shuffle_by_algorithm_M(first_1000000_X, first_1000000_Y, 100, 2**32, 1000000)
i = 0
while len(shuffled_result_bits) < 200000:
    x = shuffled_result[i]
    x_bits = bin(x)[2:]
    shuffled_result_bits += [int(bit) for bit in x_bits]
    i += 1
print(i)

shuffled_gen_results = {}
shuffled_gen_results['randomExcursionsTest'] = []
shuffled_gen_results['randomExcursionsVariantTest'] = []
for test in tests:
    response = requests.post("http://localhost:5001/" + test, json={"sequence": shuffled_result_bits})
    if test == 'randomExcursionsTest' or test == 'randomExcursionsVariantTest':
            for key, value in response.json()['pval'].items():
                shuffled_gen_results[test].append(round(value, 6))
    else:
        pval = round(response.json()['pval'], 6)
        shuffled_gen_results[test] = pval

     
#print all results sorted by testname according to tests list


sorted_X_gen_results = {test: X_gen_results[test] for test in tests}
print(sorted_X_gen_results)
sorted_Y_gen_results = {test: Y_gen_results[test] for test in tests}
print(sorted_Y_gen_results)
sorted_shuffled_gen_results = {test: shuffled_gen_results[test] for test in tests}
print(sorted_shuffled_gen_results)