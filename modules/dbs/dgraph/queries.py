from modules.dbs.queries import Queries

class DgraphQueries(Queries):
    def __init__(self, connection):
        self.connection = connection

    def find_judge_with_more_lawsuits(self):
        pass

    def find_top_five_relations_judge_kind(self):
        pass

    def find_top_five_relations_judge_lawyers(self):
        pass
