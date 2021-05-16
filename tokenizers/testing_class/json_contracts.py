import json

FILE = 'example.json'
with open(FILE, 'r') as f:
    d = json.load(f)
    for idx, info in d.items():
        print("\nID:", idx)
        for key in info:
            print(key + ':', info[key])
            with open(idx,'w') as out:
                out.write(info[key])


