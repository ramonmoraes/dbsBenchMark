from schematics.types import StringType, ListType, BooleanType, ModelType
from schematics.models import Model


class Person(Model):
    name = StringType(default="")
    last_name = StringType(default="")

class Judge(Person):
    is_judge = BooleanType(default=True)


class Lawyer(Person):
    is_lawyer = BooleanType(default=True)


class Disctrict(Model):
    name = StringType(default="")
    estate = StringType(default="")


class CourtSection(Model):
    name = StringType(default="")


class Subject(Model):
    name = StringType(default="")


class Kind(Model):
    name = StringType(default="")


class Lawsuit(Model):
    number = StringType(default="")
    judge = ModelType(Judge)
    lawyers = ListType(ModelType(Lawyer))
    related_people = ListType(ModelType(Person))
    court_section = ModelType(CourtSection)  ## Segunda turma do colegial
    disctrict = ModelType(Disctrict)  # SSA, BH
    subject = ModelType(
        Subject
    )  # (Ex: “Inclusão Indevida em Cadastro de Inadimplentes”, “Obrigação de Fazer”)
    kind = ModelType(Kind)  # Direito do Trabalho", "Direito Penal"
