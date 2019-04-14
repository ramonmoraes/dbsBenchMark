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
        yield iterable[ndx:min(ndx + n, l)]


CSV_PATH = "data/csv"


class Creator:
    def __init__(self):
        data = load_dataset()
        self.related_people = list(map(
            lambda n: Person({"name": n}), data.get("related_peoples")
        ))
        self.lawyers = list(map(lambda n: Lawyer({"name": n}), data.get("lawyers")))
        self.judges = list(map(lambda n: Judge({"name": n}), data.get("judges")))
        self.kinds = list(map(lambda n: Kind({"name": n}), data.get("kinds")))
        self.lawsuits_numbers = data.get("lawsuits")
        self._meta_data = {
            "sizes": {
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
                with open(file_path, 'a') as f:
                    dicts = list( map(lambda m: m.to_primitive(), v) )
                    w = csv.DictWriter(f, dicts[0].keys())
                    w.writeheader()
                    w.writerows(dicts)

# CsvCreator().create_basic_csv()
tc = TableCreator([Lawsuit])

lawsuit_query_template = """
INSERT INTO {table} (number, judge_id, kind_id) VALUES ("{number}", {judge_id}, {kind_id});
"""

#TODO: Add UNIQUE TO SIMPLE TABLES!!!!
class DataCreator(Creator):
    def get_id(self, model):
        return "(SELECT id FROM {table} WHERE {identifier}=\"{value}\")".format(
            table = tc.get_table_name(model),
            identifier = model.keys()[0],
            value = model.values()[0]
        )

    def clean_file(self, path):
        f = open(path, 'w')
        f.close()

    def create_data(self, max_data=1):
        data_path = 'data/insert_queries.sql'
        self.clean_file(data_path)
        data_count = 0
        for lawsuits_numbers in list_batch(self.lawsuits_numbers):
            if data_count >= max_data:
                print("Creating data ended")
                return
            insert_queries = []
            for lawsuit_number in lawsuits_numbers:
                if data_count >= max_data:
                    with open(data_path, 'a') as f:
                        print('Writting file')
                        f.writelines(insert_queries)
                    return

                judge = random.choice(self.judges)
                kind = random.choice(self.kinds)

                for model in [judge, kind]:
                    insert_queries.extend(create_query(tc.get_table_name(model), model))

                insert_queries.append(
                    lawsuit_query_template.format(
                        table=tc.get_table_name(Lawsuit()),
                        number=lawsuit_number,
                        kind_id=self.get_id(kind),
                        judge_id=self.get_id(judge)
                    )
                )
                data_count+=1

DataCreator().create_data()