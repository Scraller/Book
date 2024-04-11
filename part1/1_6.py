from collections import defaultdict

pairs = {'a': [1, 2], 'b': [4,2]}, {'c': [], 'd':'e'}
d = defaultdict(list) 
for key, value in pairs: 
    d[key].append(value)