import random
import re
from modules.dbs.creator import (
    Creator,
    MAX_LAWYER_PER_LAWSUIT,
    MAX_PERSON_PER_LAWSUIT,
    list_batch,
)

SUBJECT_TEMPLATE = "_:{identifier}"
NQUAD_TEMPLATE = "_:{subject} <{predicate}> {object} ."


def get_nquad(subject, predicate, obj):
    subject_sufix_regex = re.compile("_\:.*")
    if isinstance(obj, bool):
        obj = str(obj).lower()
    if isinstance(obj, str) and not subject_sufix_regex.match(obj):
        obj = '"{}"'.format(obj)

    subject = re.sub('[^A-Za-z0-9]+', '', subject)
    return NQUAD_TEMPLATE.format(
        subject=subject, predicate=predicate.lower(), object=obj
    )


NQUAD_PATH = "data/nquad/lawsuits.rdf"


class DgraphCreator(Creator):
    def write_nquads(self, nquads, amount):
        print("Writting {} relateds lawsuits".format(amount))
        with open(NQUAD_PATH, "a") as f:
            nquads = "\n".join(nquads)
            f.write(nquads)
            f.write("\n")

    def create_nquad(self, amount=5):
        self.clean_file(NQUAD_PATH)
        for lawsuit_batch in list_batch(self.lawsuits_numbers, amount):
            nquads = []
            for lawsuit_number in lawsuit_batch:
                related_nquads = [get_nquad(lawsuit_number, "number", lawsuit_number)]
                judgeNquad = self.get_related_nquads(
                    lawsuit_number, random.choice(self.judges)
                )
                related_nquads.extend(judgeNquad)
                kindNquad = self.get_related_nquads(
                    lawsuit_number, random.choice(self.kinds)
                )
                related_nquads.extend(kindNquad)

                for i in range(random.randint(0, MAX_LAWYER_PER_LAWSUIT)):
                    related_nquads.extend(
                        self.get_related_nquads(
                            lawsuit_number, random.choice(self.lawyers)
                        )
                    )

                for i in range(random.randint(0, MAX_PERSON_PER_LAWSUIT)):
                    related_nquads.extend(
                        self.get_related_nquads(
                            lawsuit_number, random.choice(self.related_people)
                        )
                    )
                nquads.extend(related_nquads)
            self.write_nquads(nquads, amount)
        print("[DONE]")

    def get_related_nquads(self, lawsuit_number, model):
        model_nquad = self.model_to_nquad(model)
        model_nquad.append(
            get_nquad(
                lawsuit_number,
                model.__class__.__name__,
                SUBJECT_TEMPLATE.format(identifier=model.name),
            )
        )
        return model_nquad

    def model_to_nquad(self, model):
        raw = model.to_primitive()
        if model.__class__.__name__ == "Kind":
            raw["is_kind"] = True

        nquads = []
        for key, value in raw.items():
            nquad = get_nquad(raw.get("name"), key, value)
            nquads.append(nquad)
        return nquads
