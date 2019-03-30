import json
import math
import random

from modules.models.models import Person, Lawyer

lawsuits_path = "data/lawsuits.json"
lawsuits_len = 4000000
names_len = 100787
names_path = "data/names.json"

def get_courts():
    with open(courts_path, 'r') as f:
        return json.load(f).get('courts')

def get_names():
    with open(names_path, 'r') as f:
        return json.load(f).get('names')

def get_lawsuits():
    with open(lawsuits_path, 'r') as f:
        return json.load(f).get('lawsuits_numbers')


def get_splitted_roles():
    judges_size = math.ceil(names_len / 10000) # 0,01%
    lawyers_size = math.ceil((names_len * 20) / 10000) # 0,5%

    names_list = get_names()
    judges = []
    lawyers = []
    related_peoples = []

    for i in range(judges_size):
        pop_index = random.randrange(len(names_list))
        judges.append(names_list.pop(pop_index))

    for i in range(lawyers_size):
        pop_index = random.randrange(len(names_list))
        lawyers.append(names_list.pop(pop_index))

    related_peoples = names_list
    soma = len(related_peoples) + len(judges) + len(lawyers)
    return {
        "related_peoples": related_peoples,
        "lawyers": lawyers,
        "judges": judges,
    }


def create_data_set():
    d = get_splitted_roles()
    d['lawsuits'] = get_lawsuits()
    return d


with open("data/full_dataset.json", 'w') as f:
    json.dump(create_data_set(), f)
