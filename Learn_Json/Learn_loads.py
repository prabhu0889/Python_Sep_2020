import json  # dumps, dump, loads, load

# loads ->  covert json to python
py = json.loads('{"name": "GN", "active": false, "value":null}')
print(py)

# load -> read the data from json
with open('hello.json', 'r') as f:
    ud = json.load(f)       # reads the data from json
    x = json.loads(ud)      # conver json to python


print(x)

# sqlite3


