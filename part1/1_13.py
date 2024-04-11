from operator import itemgetter

rows = [
{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}, 
{'fname': 'David', 'lname': 'Beazley', 'uid': 1002}, 
{'fname': 'John', 'lname': 'Cleese', 'uid': 1001}, 
{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_fname1 = sorted(rows, key=itemgetter('fname')) 
rows_by_uid1 = sorted(rows, key=itemgetter('uid'))
rows_by_lfname1 = sorted(rows, key=itemgetter('lname','fname'))#sort first by first argument, in case of same value of argument -> sort by second argument
rows_by_fname2 = sorted(rows, key=lambda r: r['fname']) 
rows_by_lfname2 = sorted(rows, key=lambda r: (r['lname'],r['fname']))
#>>> rows_by_fname1 == rows_by_fname2 - TRUE
#>>> rows_by_lfname1 == rows_by_lfname2 - TRUE
min(rows, key=itemgetter('fname')) #{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
min(rows, key=itemgetter('uid')) #{'fname': 'John', 'lname': 'Cleese', 'uid': 1001}
max(rows, key=itemgetter('uid')) #{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}