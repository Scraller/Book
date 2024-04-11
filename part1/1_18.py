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


Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# Создание экземпляра прототипа
stock_prototype = Stock('', 0, 0.0, None, None)
# Функция для преобразования словаря в Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)

a = {'name': 'ACME', 'shares': 100, 'price': 123.45} #Stock(name='ACME', shares=100, price=123.45, date=None, time=None)
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'} #Stock(name='ACME', shares=100, price=123.45, date='12/17/2012', time=None)
