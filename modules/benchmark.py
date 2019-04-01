class BenchMark:
    def __init__(self, amount = 1):
        self.amount = amount

    def start():
        self.create_dbs()
        self.insert_datas()
        self.make_queries()
        self.compare_results()

    def create_dbs():
        self.create_mysql_db()
        self.create_dgraph_db()

    def insert_data():
        self.insert_mysql_data()
        self.insert_dgraph_data()

    def make_queries():
        self.sql_results = make_mysql_queries()
        self.dgraph_results = make_dgraph_queries()

    def compare_results():
        print(
            self.sql_results
            self.dgraph_results
        )