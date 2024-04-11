def dedupe(items): 
    seen = set()
    for item in items:
        if item not in seen:
            yield item 
            seen.add(item)
            
a = [1, 5, 2, 1, 9, 1, 5, 10]
b = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]

# We can work around dictinary, by removing either seen {key:value} or {key}
def dedupe_dictinary(items, key=None): 
    seen = set()
    for item in items:
        val = item if key is None else key(item) 
        if val not in seen:
            yield item 
            seen.add(val)

list(dedupe_dictinary(b, key=lambda d: (d['x'],d['y']))) #[{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
list(dedupe_dictinary(b, key=lambda d: d['x']))[{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]