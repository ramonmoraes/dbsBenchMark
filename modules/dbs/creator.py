from modules.relatedModels import load_dataset
from modules.models.models import *

MAX_LAWYER_PER_LAWSUIT = 3
MAX_PERSON_PER_LAWSUIT = 4


def list_batch(iterable, n=10000):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx : min(ndx + n, l)]


class Creator:
    def __init__(self):
        data = load_dataset()
        self.persons = list(
            map(lambda n: Person({"name": n}), data.get("related_peoples"))
        )
        self.lawyers = list(map(lambda n: Lawyer({"name": n}), data.get("lawyers")))
        self.judges = list(map(lambda n: Judge({"name": n}), data.get("judges")))
        self.kinds = list(map(lambda n: Kind({"name": n}), data.get("kinds")))
        self.lawsuits_numbers = data.get("lawsuits")
        self._meta_data = {
            "sizes": {
                "lawsuits_numbers": len(self.lawsuits_numbers),
                "persons": len(self.persons),
                "lawyers": len(self.lawyers),
                "judges": len(self.judges),
                "kinds": len(self.kinds),
            }
        }

    def clean_file(self, path):
        with open(path, "w"):
            print("Cleaning file at", path)
