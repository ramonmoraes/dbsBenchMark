import csv
import random

from modules.relatedModels import get_related_model, load_dataset
from modules.dbs.sql.tableCreator import get_table_name, TableCreator
from modules.dbs.sql.insertData import create_query
from modules.models.models import *
from itertools import islice, chain


def list_batch(iterable, n=10000):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx : min(ndx + n, l)]


CSV_PATH = "data/csv"


class Creator:
    def __init__(self):
        data = load_dataset()
        self.related_people = list(
            map(lambda n: Person({"name": n}), data.get("related_peoples"))
        )
        self.lawyers = list(map(lambda n: Lawyer({"name": n}), data.get("lawyers")))
        self.judges = list(map(lambda n: Judge({"name": n}), data.get("judges")))
        self.kinds = list(map(lambda n: Kind({"name": n}), data.get("kinds")))
        self.lawsuits_numbers = data.get("lawsuits")
        self._meta_data = {
            "sizes": {
                "lawsuits_numbers": len(self.lawsuits_numbers),
                "related_people": len(self.related_people),
                "lawyers": len(self.lawyers),
                "judges": len(self.judges),
                "kinds": len(self.kinds),
            }
        }


class CsvCreator(Creator):
    def create_basic_csv(self):
        obj = self.__dict__
        del obj["lawsuits_numbers"]
        del obj["_meta_data"]
        for k, v in obj.items():
            print("Writting :", k)
            for batch in list_batch(k, 500000):
                file_path = "{}/{}.csv".format(CSV_PATH, get_table_name(k))
                dicts = list(map(lambda m: m.to_primitive(), v))
                self.write_csv(file_path, dicts)

    def write_csv(self, file_path, dicts):
        with open(file_path, "a") as f:
            w = csv.DictWriter(f, dicts[0].keys())
            w.writeheader()
            w.writerows(dicts)

    def get_random_id(self, key):
        return random.randint(1, self._meta_data["sizes"][key])

    def create_lawsuit_csv(self):
        lawsuits = self.__dict__["lawsuits_numbers"]
        lawsuit_path = "data/csv/lawsuits.csv"
        for lawsuit_batch in list_batch(lawsuits, 500000):
            related_lawsuits = []
            for lawsuit_number in lawsuit_batch:
                lawsuit = {
                    "number": lawsuit_number,
                    "judge_id": self.get_random_id("judges"),
                    "kind_id": self.get_random_id("kinds"),
                }
                related_lawsuits.append(lawsuit)
            self.write_csv(lawsuit_path, related_lawsuits)

    def create_related_csv(self):
        print("Writting lawsuit csv")
        self.create_lawsuit_csv()

    def create_one_to_many():
        lawsuits = self.__dict__["lawsuits_numbers"]
        lawsuit_path = "data/csv/lawsuits.csv"

CsvCreator().create_related_csv()
