
import numpy as np

s = """testApproximateEntropyTestEndpoint: 5.110479831695557
.testBinaryMatrixRankTestEndpoint: 1.7622203826904297
.testCumulativeSumsBackwardTestEndpoint: 0.772552490234375
.testCumulativeSumsForwardTestEndpoint: 0.7692513465881348
.testDiscreteFourierTransformTestEndpoint: 0.5124905109405518
.testFrequencyMonobitTestEndpoint: 0.32040977478027344
.testFrequencyTestWithinBlockEndpoint: 0.4076673984527588
.testLongestRunOfOnesInABlockTestEndpoint: 0.3401670455932617
.testMaurersUniversalStatisticalTestEndpoint: 0.5718038082122803
.testNonOverlappingTemplateMatchingTestEndpoint: 2.0884406566619873
.testOverlappingTemplateMatchingTestEndpoint: 2.1745798587799072
.testRandomExcursionsTestEndpoint: 0.8859479427337646
.testRandomExcursionsVariantTestEndpoint: 0.7407591342926025
.testRunsTestEndpoint: 0.41521120071411133
.testSerialTestEndpoint: 1.5594747066497803"""
s = s.replace('test', '')
s = s.replace('Endpoint', '')
s = s.split('\n')
d = {}
for ss in s:
    k, v = ss.split(':')
    k = k.replace('.', '')
    d[k] = float(v)
#print dict sorted by value
for k, v in sorted(d.items(), key=lambda x: x[1]):
    print(k, v)

result = """
FrequencyMonobitTest 0.32040977478027344
LongestRunOfOnesInABlockTest 0.3401670455932617
FrequencyTestWithinBlock 0.4076673984527588
RunsTest 0.41521120071411133
DiscreteFourierTransformTest 0.5124905109405518
MaurersUniversalStatisticalTest 0.5718038082122803
RandomExcursionsVariantTest 0.7407591342926025
CumulativeSumsForwardTest 0.7692513465881348
CumulativeSumsBackwardTest 0.772552490234375
RandomExcursionsTest 0.8859479427337646
SerialTest 1.5594747066497803
BinaryMatrixRankTest 1.7622203826904297
NonOverlappingTemplateMatchingTest 2.0884406566619873
OverlappingTemplateMatchingTest 2.1745798587799072
ApproximateEntropyTest 5.110479831695557
"""