import json

data = {"agent" : "Researcher", "task" : "find AI trends"}
print(type(data))
json_data = json.dumps(data)
print(type(json_data))
print(json_data)

# conver json to dict
parsed_data = json.loads(json_data)
print(type(parsed_data))
print(parsed_data['task'])