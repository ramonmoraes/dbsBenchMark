from modules.dbs.queries import Queries


class SqlQueries(Queries):
    def __init__(self, cursor):
        self.cursor = cursor

    def find_judge_with_more_lawsuits(self):
        query = """
        SELECT l.judge_id, count(l.judge_id), j.name
        FROM lawsuitTable as l
        left join judgeTable as j on j.id = l.judge_id
        group by judge_id
        limit 5
        """
        return self.cursor.execute(query)

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
        """Error Code: 1140. In aggregated query without GROUP BY, expression #1 of SELECT list contains nonaggregated column 'db.num.number'; this is incompatible with sql_mode=only_full_group_by

        return self.cursor.execute(query)
