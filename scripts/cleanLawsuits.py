import json

names_path = "./data/lawsuits.csv"
with open(names_path, "r") as names_file:
    lines = names_file.readlines()
    lawsuits = list(map(lambda row: row.split("|")[-1].strip(), lines))[1:]

    jsonDict = {"lawsuits_numbers": lawsuits}
    lawsuit_json_path = "./data/lawsuits.json"

    with open(lawsuit_json_path, "w") as file:
        file.write(json.dumps(jsonDict))
