prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20, 
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
prices_sorted = sorted(zip(prices.values(), prices.keys()))

prices_and_names = zip(prices.values(), prices.keys()) 
min(prices_and_names)# OK
max(prices_and_names)# ValueError: max() arg is an empty sequence

# DISCUSSION
min(prices) # Вернет 'AAPL'
max(prices) # Вернет 'IBM'
min(prices.values()) # Вернет 10.75 
max(prices.values()) # Вернет 612.78

min(prices, key=lambda k: prices[k]) # Вернет 'FB' 
max(prices, key=lambda k: prices[k]) # Вернет 'AAPL'
min_value = prices[min(prices, key=lambda k: prices[k])] #Вернет 10.75

prices = { 'AAA' : 45.23, 'ZZZ': 45.23, 'AA': 45.23}
min(zip(prices.values(), prices.keys())) #(45.23, 'AA') Возвращает ключ с мин. значением
max(zip(prices.values(), prices.keys())) #(45.23, 'ZZZ') 