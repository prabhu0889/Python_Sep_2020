data = {
        'name' : 'Gopinath Jayakumar',
        'Pay'  : 00000000,
        'exp'  : '10+',
        'hobbies': ('always sleeping', 'always eating'),
        'value': None,
        'is_nothing': True
        }

import json

# dumps -> convert python to json
print(type(data))
j = json.dumps(data, indent=4)          # dumps vs dump
print(type(j))
print(j)

# dump  ->  write the json file
with open('hello.json', 'w') as f:
    json.dump(j, f, indent=4, sort_keys=True)


# loads