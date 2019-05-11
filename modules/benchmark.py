import os
import time

from modules.dbs.sql.creator import CsvCreator
from modules.dbs.sql.operations import SqlOperations
from modules.dbs.sql.queries import SqlQueries

from modules.dbs.dgraph.operations import DgraphOperations
from modules.dbs.dgraph.creator import DgraphCreator
from modules.dbs.dgraph.queries import DgraphQueries

from modules.results_writter import ResultWritter

QUERY_REPEAT_AMOUNT = 10

class BenchMark:
    def __init__(self, amount=2):
        self.amount = amount

    def start(self):
        for _ in range(self.amount):
            self.pre_scripts()
            self.configure()
            self.create_dbs()
            self.create_data()
            self.insert_data()
            self.make_queries()
            self.compare_results()

    def pre_scripts(self):
        print("Pre-scripts")
        print("Dropping all")
        os.system("./scripts/dropAll.sh")
        print("Running all")
        os.system("./scripts/runAll.sh")

    def configure(self):
        print("Configuring attributes")
        for _ in range(10):
            print(".", end=" ")
            time.sleep(1)
        self.sqlOps = SqlOperations()
        self.dgraphOps = DgraphOperations()
        self.sqlQueries = SqlQueries(self.sqlOps.get_cursor())
        self.dgraphQueries = DgraphQueries(self.dgraphOps.client)

    def create_dbs(self):
        self.create_mysql_db()

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
        for i in range(QUERY_REPEAT_AMOUNT):
            for queryMaker in [self.dgraphQueries, self.sqlQueries]:
                class_name = queryMaker.__class__.__name__
                writter = ResultWritter(class_name)
                writter.write_result("find_every_related_data", queryMaker.find_every_related_data)
                writter.write_result("find_judge_with_more_lawsuits", queryMaker.find_judge_with_more_lawsuits)
                writter.write_result("find_thousand_lawsuits_numbers", queryMaker.find_thousand_lawsuits_numbers)


    def compare_results(self):
        print(self.sql_results, self.dgraph_results)

    def create_mysql_db(self):
        self.sqlOps.recreate_database()
        self.sqlOps.create_tables()

    def insert_mysql_data(self):
        self.sqlOps.load_data()

    def insert_dgraph_data(self):
        self.dgraphOps.load_data()
        os.system("./scripts/runServer.sh")
