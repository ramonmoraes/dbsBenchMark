import csv
import json

namesPath = "./data/nomes.csv"
csvDicts = csv.DictReader(open(namesPath), "first_name")

nameList = list(map(lambda obj: dict(obj).get("f"), csvDicts))

namesJsonPath = "./data/names.json"
jsonDict = {"names": nameList[1:]}

with open(namesJsonPath, "w") as file:
    file.write(json.dumps(jsonDict))
