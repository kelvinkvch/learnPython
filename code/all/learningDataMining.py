from collections import defaultdict
import numpy as np
file = r'infile\affinity_dataset.txt'
features = ['bread', 'milk', 'cheese', 'apples', 'banana']
x = np.loadtxt(file)
valid_rules = defaultdict(int)
invalid_rules = defaultdict(int)
num_occurences = defaultdict(int)
nsample, nfeatures = x.shape
for sample in x:
    for premise in range(nfeatures):
        if sample[premise] == 0: continue
        num_occurences[premise] += 1
        for conclusion in range(nfeatures):
            if premise == conclusion: continue
            if sample[conclusion] == 1:
                valid_rules[(premise,conclusion)] += 1
            else:
                invalid_rules[(premise, conclusion)] += 1
support = valid_rules
confidence = defaultdict(float)
for premise, conclusion in valid_rules.keys():
    confidence[(premise, conclusion)] = valid_rules[
        (premise, conclusion)] / num_occurences[premise]
# for i,(premise, conclusion) in enumerate(confidence):
#     premise_name = features[premise]
#     conclusion_name = features[conclusion]
#     print(i+1)
#     print('Rule: If a person buys {0} they will also buy {1}'.format(
#         premise_name, conclusion_name))
#     print('\t-Confidence: {0:.2f}%'.format(confidence[(premise, conclusion)]*100))
#     print('\t-Support: {0}'.format(support[(premise, conclusion)]))
#     print('')
from pprint import  pprint
from operator import itemgetter
sorted_support=sorted(support.items(),key=itemgetter(1),reverse=True)
for index in range(10):
    print('Rule #{0}'.format(sorted_support[index]))
    # premise,conclusion=sorted_support[index][0]
    # pprint(premise,conclusion)