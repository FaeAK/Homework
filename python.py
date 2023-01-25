
import json

with open("text.json") as json_data:
	python_obj = json.load(json_data)
	print(python_obj)

