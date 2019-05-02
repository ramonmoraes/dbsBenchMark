from modules.dbs.sql.operations import SqlOperations
from modules.dbs.dgraph.operations import DgraphOperations


class BenchMark:
    def __init__(self, amount=1):
        self.amount = amount
        self.sqlOps = SqlOperations()
        self.dgraphOps = DgraphOperations()

    def start(self):
        self.create_dbs()
        self.insert_data()
        self.make_queries()
        self.compare_results()

    def create_dbs(self):
        self.create_mysql_db()
        self.create_dgraph_db()

    def insert_data(self):
        self.insert_mysql_data()
        self.insert_dgraph_data()

    def make_queries(self):
        self.sql_results = self.make_mysql_queries()
        self.dgraph_results = self.make_dgraph_queries()

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
