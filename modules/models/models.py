from schematics.types import StringType, ListType, BooleanType, ModelType
from schematics.models import Model


class Person(Model):
    name = StringType()


class Judge(Person):
    is_judge = BooleanType()


class Lawyer(Person):
    is_lawyer = BooleanType()


class Disctrict(Model):
    name = StringType()
    estate = StringType()


class CourtSection(Model):
    name = StringType()


class Subject(Model):
    name = StringType()


class Kind(Model):
    name = StringType()


class Lawsuit(Model):
    number = StringType()
    judge = ModelType(Judge)
    lawyers = ListType(ModelType(Lawyer))
    related_people = ListType(ModelType(Person))
    court_section = ModelType(CourtSection)  ## Segunda turma do colegial
    disctrict = ModelType(Disctrict)  # SSA, BH
    subject = ModelType(
        Subject
    )  # (Ex: “Inclusão Indevida em Cadastro de Inadimplentes”, “Obrigação de Fazer”)
    kind = ModelType(Kind)  # Direito do Trabalho", "Direito Penal"
