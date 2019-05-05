from modules.dbs.sql.creator import CsvCreator
from modules.dbs.sql.operations import SqlOperations
from modules.dbs.sql.queries import SqlQueries

from modules.dbs.dgraph.operations import DgraphOperations
from modules.dbs.dgraph.creator import DgraphCreator
from modules.dbs.dgraph.queries import DgraphQueries



class BenchMark:
    def __init__(self, amount=1):
        self.amount = amount
        self.sqlOps = SqlOperations()
        self.sqlQueries = SqlQueries(self.sqlOps.get_cursor())
        self.dgraphOps = DgraphOperations()
        self.dgraphQueries = DgraphQueries(self.dgraphOps.client)

    def start(self):
        self.create_dbs()
        self.create_data()
        self.insert_data()
        self.make_queries()
        self.compare_results()

    def create_dbs(self):
        self.create_mysql_db()
        self.create_dgraph_db()

    def create_data(self):
        self.create_dgraph_data()
        self.create_mysql_data()

    def create_dgraph_data(self):
        DgraphCreator().create_nquad()

    def create_mysql_data(self):
        CsvCreator().create_related_csv()

    def insert_data(self):
        self.insert_mysql_data()
        self.insert_dgraph_data()

    def make_queries(self):
        for queryMaker in [self.dgraphQueries, self.sqlQueries]:
            queryMaker.find_every_related_data()
            queryMaker.find_judge_with_more_lawsuits()
            queryMaker.find_top_five_relations_judge_kind()
        # self.sql_results = self.make_mysql_queries()
        # self.dgraph_results = self.make_dgraph_queries()

    def compare_results(self):
        print(self.sql_results, self.dgraph_results)

    def create_mysql_db(self):
        self.sqlOps.recreate_database()
        self.sqlOps.create_tables()

    def create_dgraph_db(self):
        self.dgraphOps.drop_all()
        self.dgraphOps.create_index()

    def insert_mysql_data(self):
        self.sqlOps.load_data()

    def insert_dgraph_data(self):
        self.dgraphOps.load_data()
