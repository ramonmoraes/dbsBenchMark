import os
import csv
import random

from modules.relatedModels import get_related_model, load_dataset
from modules.dbs.creator import (
    Creator,
    MAX_LAWYER_PER_LAWSUIT,
    MAX_PERSON_PER_LAWSUIT,
    list_batch,
)
from modules.dbs.sql.tableCreator import get_table_name, TableCreator
from modules.dbs.sql.insertData import create_query
from modules.models.models import *
from itertools import islice, chain

CSV_PATH = "data/csv"


class CsvCreator(Creator):
    def create_basic_csv(self):
        obj = self.__dict__.copy()
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
        lawsuit_path = "data/csv/lawsuitTable.csv"
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
        print("Cleaning files on data/csv/*.csv")
        os.system("rm -rf data/csv/*.csv")
        self.create_basic_csv()
        self.create_lawsuit_csv()
        self.create_one_to_many_lawsuitlawyer()
        self.create_one_to_many_lawsuitperson()

    def create_one_to_many_lawsuitlawyer(self):
        lawsuits_amount = self._meta_data.get("sizes").get("lawsuits_numbers")
        lawyers_max_id = self._meta_data.get("sizes").get("lawyers")
        lawsuitlawyerTable_path = "data/csv/lawsuitlawyerTable.csv"
        data_list = []
        for lawsuit_id in range(lawsuits_amount):
            lawyer_amount = random.randint(1, MAX_LAWYER_PER_LAWSUIT)
            for i in range(lawyer_amount):
                lawyers_id = random.randint(0, lawyers_max_id)
                data = {"lawsuit_id": lawsuit_id, "lawyer_id": lawyers_id}
                data_list.append(data)
        self.write_csv(lawsuitlawyerTable_path, data_list)

    def create_one_to_many_lawsuitperson(self):
        lawsuits_amount = self._meta_data.get("sizes").get("lawsuits_numbers")
        related_people = self._meta_data.get("sizes").get("persons")
        lawsuitlawyerTable_path = "data/csv/lawsuitpersonTable.csv"
        data_list = []
        for lawsuit_id in range(lawsuits_amount):
            lawyer_amount = random.randint(0, MAX_PERSON_PER_LAWSUIT)
            for i in range(lawyer_amount):
                person_id = random.randint(0, related_people)
                data = {"lawsuit_id": lawsuit_id, "person_id": person_id}
                data_list.append(data)
        self.write_csv(lawsuitlawyerTable_path, data_list)
