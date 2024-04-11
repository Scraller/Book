

# Выводит кортеж как CSV
s = ('ACME', 50, 123.45) 
print(','.join(str(x) for x in s))

portfolio = [
    {'name':'GOOG', 'shares': 50}, 
    {'name':'YHOO', 'shares': 75}, 
    {'name':'AOL', 'shares': 20}, 
    {'name':'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio) #20
min_shares2 = min(portfolio, key=lambda s: s['shares']) #{'name': 'AOL', 'shares': 20}
