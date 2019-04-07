import json
import random

from modules.models.models import *


def load_dataset():
    with open("data/full_dataset.json", "r") as f:
        return json.load(f)


def get_related_model(porcent=100):
    data = load_dataset()
    related_people = data.get("related_peoples")
    lawsuits = data.get("lawsuits")
    lawyers = data.get("lawyers")
    judges = data.get("judges")
    kinds = data.get("kinds")
    courts = data.get("courts")

    lawsuits_models = []
    max_models_size = len(lawsuits) * porcent / 100
    print("Getting {} models".format(max_models_size))
    models_count = 0
    for lawsuit in lawsuits:
        if models_count >= max_models_size:
            return lawsuits_models
        models_count += 1
        judge = Judge({"name": random.choice(judges)})
        kind = Kind({"name": random.choice(kinds)})
        people = get_model_random_amount(Person, related_people, 5)
        law = get_model_random_amount(Lawyer, lawyers, 3)
        court = CourtSection({"name": "TJ-BA"})
        lawsuit = Lawsuit(
            {
                "number": lawsuit,
                "related_people": people,
                "lawyers": law,
                "kind": kind,
                "judge": judge,
                # "district": d,
                "court_section": court,
            }
        )
        lawsuits_models.append(lawsuit)
    return lawsuits_models


def get_model_random_amount(model, arr, max):
    res = []
    for x in range(random.randint(1, max)):
        res.append(model({"name": random.choice(arr)}))
    return res
