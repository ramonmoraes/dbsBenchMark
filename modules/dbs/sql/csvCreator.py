import csv
from modules.relatedModels import get_related_model, load_dataset
from modules.dbs.sql.tableCreator import get_table_name
from modules.models.models import *
from itertools import islice, chain

def list_batch(iterable, n=10000):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]


CSV_PATH = "data/csv"


class CsvCreator:
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


    def iter_from_attribte(self, key):
        for d in self.__dict__.get("key"):
            yield d

    def create_basic_csv(self):
        obj = self.__dict__
        del obj["lawsuits_numbers"]
        del obj["_meta_data"]
        # import pdb; pdb.set_trace()
        for k, v in obj.items():
            print("Writting :", k)
            for batch in list_batch(k, 500000):
                file_path = "{}/{}.csv".format(CSV_PATH, get_table_name(k))
                with open(file_path, 'a') as f:
                    dicts = list( map(lambda m: m.to_primitive(), v) )
                    w = csv.DictWriter(f, dicts[0].keys())
                    w.writeheader()
                    w.writerows(dicts)

    def create(self, percent = 100):
        max_csv_size = len(self.lawsuits) * percent / 100
        if max_csv_size < 1:
            print("Can not create less then 1 csv")
            return
        print("Getting {} csv".format(max_csv_size))
        csv_count = 0
        for lawsuit in self.iter_from_attribte('lawsuits_mumber'):
            if csv_count>=max_csv_size:
                return
            csv_count+=1


creator = CsvCreator()
creator.create()

# CsvCreator().create(0.0001)
