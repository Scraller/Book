prices = {
'ACME': 45.23,
'AAPL': 612.78, 
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
#
p1 = { key:value for key, value in prices.items() if value > 200 }
p1_alt = dict((key, value) for key, value in prices.items() if value > 200)
#
p2 = { key:value for key,value in prices.items() if key in tech_names } #более интуитивное и быстрое в выполнении
p2_alt = { key:prices[key] for key in prices.keys() & tech_names } #более медленное

