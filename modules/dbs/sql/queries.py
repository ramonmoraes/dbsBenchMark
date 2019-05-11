from modules.dbs.queries import Queries


class SqlQueries(Queries):
    def __init__(self, cursor):
        self.cursor = cursor

    def find_judge_with_more_lawsuits(self):
        query = """
        SELECT COUNT(l.judge_id), j.name
        FROM lawsuitTable AS l
        LEFT JOIN judgeTable AS j on j.id = l.judge_id
        GROUP BY l.judge_id, j.name
        ORDER BY COUNT(l.judge_id) DESC
        limit 5
        """
        return self.cursor.execute(query)

    def find_thousand_lawsuits_numbers(self):
        query = """
        SELECT number
        FROM lawsuitTable
        limit 1000
        """
        return self.cursor.execute(query)

    def find_every_related_data(self):
        query = """
        SELECT num.number, kin.name, jud.name AS "judgeName", law.name AS "lawyerName", per.name AS "personName"
        FROM lawsuitTable AS num
        LEFT JOIN kindTable AS kin
        ON num.kind_id = kin.id
        LEFT JOIN judgeTable AS jud
        on jud.id = num.judge_id
        LEFT JOIN lawsuitlawyerTable AS ll
        on num.id = ll.lawsuit_id
        LEFT JOIN lawyerTable AS law
        on law.id = ll.lawyer_id
        LEFT JOIN lawsuitpersonTable AS lp
        on num.id = ll.lawsuit_id
        LEFT JOIN lawyerTable AS per
        on per.id = lp.person_id
        LIMIT 100
        """

        return self.cursor.execute(query)
