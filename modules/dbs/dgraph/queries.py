from modules.dbs.queries import Queries
import json
import os


def clear():
    os.system("clear")


class DgraphQueries(Queries):
    def __init__(self, client):
        # self.client = client
        self.txn = client.txn()

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
        return self.make_query(query)

    def find_thousand_lawsuits_numbers(self):
        query = """{
            data(func: has(number), first: 1000) {
                number
             }
        }"""
        return self.make_query(query)

    def find_every_related_data(self):
        query = """{
            data(func: has(number), first: 100) {
                number,
                kind{
                    name
                }
                judge{
                    name
                }
                person{
                    name
                }
            }
        }"""
        return self.make_query(query)

    def make_query(self, query):
        return self.txn.query(query)
        # txn = self.client.txn()
        # try:
        #     return txn.query(query)
        # finally:
        #     txn.discard()
