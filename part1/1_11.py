record = '2000000000111111111112341234111110120120513.251111111111111' 
cost = int(record[0:5]) * float(record[40:48])
SHARES = slice(0,5)
PRICE = slice(40,48)
cost2 = int(record[SHARES]) * float(record[PRICE])
####
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4, 1)
#items[2:4]#[2, 3]
#items[a]#[2, 3]
#items[a] = [10] #[0, 1, 10, 4, 5, 6]
#items[a] = [10,11]#[0, 1, 10, 11, 5, 6]
#del items[a]#[0, 1, 5, 6]

#>>> a.start
#2
#>>> a.stop
#4
#>>> a.step
#>>> 
#1