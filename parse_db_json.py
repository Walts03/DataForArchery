import json

with open("./cos20031_48_db.json") as f:
	datas = json.load(f)

for data in datas:
	if data["type"] == "table":
		with open(f"./{data['name']}.json", "w+") as table_f:
			json.dump(data["data"], table_f, indent=2)
