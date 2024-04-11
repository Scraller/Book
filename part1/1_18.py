from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')

sub.addr #'jonesy@example.com'
sub.joined #'2012-10-19'
len(sub) #2
address, joined_date = sub #распаковка
address #'jonesy@example.com'
joined_date #'2012-10-19'

# Абстрактные примеры для замера времени исполнения кортежей, сначало обычные кортежи, после - именованные 
def compute_cost1(records): 
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

Stock = namedtuple('Stock', ['name', 'shares', 'price']) 
def compute_cost2(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price 
    return total