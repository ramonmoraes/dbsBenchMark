from modules.dbs.queries import Queries

class SqlQueries(Queries):
    def __init__(self, cursor):
        self.cursor = cursor

    def find_judge_with_more_lawsuits(self):
        pass

    def find_top_five_relations_judge_kind(self):
        pass

    def find_top_five_relations_judge_lawyers(self):
        pass
