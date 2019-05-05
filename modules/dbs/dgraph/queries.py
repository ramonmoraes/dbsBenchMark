from modules.dbs.queries import Queries
import os

def clear():
    os.system("clear")

class DgraphQueries(Queries):
    def __init__(self, client):
        self.client = client


    def find_judge_with_more_lawsuits(self):
        query = """{
            var(func: has(is_judge)) {
                lawsuitsJudged as count(~judge)
            }

            query(func: uid(lawsuitsJudged), orderdesc: val(lawsuitsJudged), first: 5) {
                name
                val(lawsuitsJudged)
            }
        }"""
        res = self.make_query(query)

    def find_top_five_relations_judge_kind(self):
        # print(self.client)
        pass

    def find_top_five_relations_judge_lawyers(self):
        # print(self.client)
        pass

    def make_query(self, query):
        txn = self.client.txn()
        try:
            return txn.query(query)
        finally:
            txn.discard()