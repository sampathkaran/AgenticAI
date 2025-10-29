import json

json_data = """{"name": "Honda City 4th Generation", "description": "This is a sedan Car", "price_estimate": "null", "pros": [], "cons": [],}"""

print(json.loads(json_data))