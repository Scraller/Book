values = ['1', '2', '-3', '-', '4', 'N/A', '5']

import math
from itertools import compress

def is_int(val): 
    try:
        x = int(val)
        return True 
    except ValueError:
        return False
ivals = list(filter(is_int, values)) 
print(ivals) # Выведет ['1', '2', '-3', '4', '5']

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
[math.sqrt(n) for n in mylist if n > 0] #[1.0, 2.0, 3.1622776601683795, 1.4142135623730951, 1.7320508075688772]
clip_neg = [n if n > 0 else 0 for n in mylist]#[1, 4, 0, 10, 0, 2, 3, 0]
clip_pos = [n if n < 0 else 0 for n in mylist]#[0, 0, -5, 0, -7, 0, 0, -1]
###############
addresses = [
'5412 N CLARK',
'5148 N CLARK', '5800 E 58TH',
'2122 N CLARK', '5645 N RAVENSWOOD',
'1060 W ADDISON', '4801 N BROADWAY',
'1039 W GRANVILLE',
]

counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
more5 = [n > 5 for n in counts] #[False, False, True, False, False, True, True, False]
list(compress(addresses, more5)) # ['5800 E 58TH', '1060 W ADDISON', '4801 N BROADWAY']