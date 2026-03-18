import json

our_json = """
{
    "a": {
        "name": "Jack",
        "surname": "Sparrow"
    },
    "b": [1, 2, 3, 45],
    "c": "Allan Wake",
    "d": 123
}
"""

# my_dict1 = json.loads(our_json)
# my_dict1 = json.load(open("file1.json"))
# print(type(my_dict1))
# print(my_dict1)
# print(my_dict1['a'])
# print(my_dict1['a']['surname'])
# print(type(my_dict1['x']['a']))
# for node in my_dict1:
#     print(node)

# my_dict2 = {'a': [1, 2], 'b': [3, 4], 'c': {'x': 1, 'y': 2}}
# json.dump(my_dict2, open("file3.json", "w"), indent=4)


f = open("data.csv")
data_dict = dict()
for i, l in enumerate(f):
    if i == 0:
        continue
    _, _, d, t, q = l.strip().split(',')
    data_dict[f"node_{i}"] = {"date": d, "temp": int(t), "q": int(q)}
print(data_dict)
json.dump(data_dict, open("file3.json", "w"), indent=4)

