class Lawsuit:
    number = ""
    judges = ""
    lawyers = []
    related_people = []
    court_section = "" ## Segunda turma do colegial
    disctrict = "" # SSA, BH
    subject = "" #(Ex: “Inclusão Indevida em Cadastro de Inadimplentes”, “Obrigação de Fazer”)
    kind = "" # Direito do Trabalho", "Direito Penal"

class Person:
    name = ""


class Judge(Person):
    is_judge = True


class Lawyers(Person):
    is_lawyer = True


class Disctrict:
    name = ""
    estate = ""

class CourtSection:
    name = ""

class Subject:
    name = ""

class Kind:
    name = ""
