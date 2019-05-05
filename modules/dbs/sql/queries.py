from modules.dbs.queries import Queries


class SqlQueries(Queries):
    def __init__(self, cursor):
        self.cursor = cursor

    def find_judge_with_more_lawsuits(self):
        pass

    def find_top_five_relations_judge_kind(self):
        pass

    def find_every_related_data(self):
        query = """
        SELECT num.number, kin.name, jud.name as "judgeName", law.name as "lawyerName", per.name as "personName"
        FROM lawsuitTable as num
        LEFT JOIN kindTable as kin
        ON num.kind_id = kin.id
        LEFT JOIN judgeTable as jud
        on jud.id = num.judge_id
        LEFT JOIN lawsuitlawyerTable as ll
        on num.id = ll.lawsuit_id
        LEFT JOIN lawyerTable as law
        on law.id = ll.lawyer_id
        LEFT JOIN lawsuitpersonTable as lp
        on num.id = ll.person_id
        LEFT JOIN lawyerTable as per
        on per.id = lp.person_id
        """
        pass
