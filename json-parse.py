import json

# dictionary in string format
odics = '{"k1":"val1", "k2":"val2"}'

# parse string into json format
json_result = json.loads(odics)
print(json_result)