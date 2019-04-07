import csv
from modules.relatedModels import get_related_model, load_dataset
from modules.dbs.sql.tableCreator import get_table_name
from modules.models.models import *

csv_path = "data/csv"
class CsvCreator:
    def __init__(self):
        data = load_dataset()
        self.related_people = map(lambda n: Person({"name": n}), data.get('related_peoples'))
        self.lawyers = map(lambda n: Lawyer({"name": n}), data.get('lawyers'))
        self.judges = map(lambda n: Judge({"name": n}), data.get('judges'))
        self.kinds = map(lambda n: Kind({"name": n}), data.get('kinds'))
        self.lawsuits_numbers = data.get('lawsuits')

    def create_basic_csv(self):
        d = self.__dict__
        del d['lawsuits_numbers']

        for k, v in d.items():
            print("Writting :", k)
            with open("{}/{}.csv".format(csv_path, get_table_name(k)), 'w') as f:
                dicts = list(
                    map(lambda m: m.to_primitive(), v)
                )[1:10]
                w = csv.DictWriter(f, dicts[0].keys())
                w.writeheader()
                w.writerows(dicts)

CsvCreator().create_basic_csv()

# def get_model_random_amount(model, arr, max):
#     res = []
#     for x in range(random.randint(1, max)):
#         res.append(
#             model({"name": random.choice(arr)})
#         )
#     return res



    # def create(self, percent = 100):
    #     max_csv_size = len(self.lawsuits) * percent / 100
    #     if max_csv_size < 1:
    #         print("Can not create less then 1 csv")
    #         return
    #     print("Getting {} csv".format(max_csv_size))
    #     csv_count = 0
    #     for lawsuit in self.lawsuits:
    #         if csv_count>=max_csv_size:
    #             return
    #         csv_count+=1
#CsvCreator().create(0.0001)
