from modules.dbs.queries import Queries
import json
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
        return self.make_query(query)


    def find_top_five_relations_judge_kind(self):
        # clear()

        # query = """{
        #     data(func: has(is_kind), first: 1) {
        #         name
        #         lawsuit: ~kind {
        #             judge {
        #                 name
        #             }
        #         }
        #     }
        # }"""

        # query = """{
        #     var(func: has(is_kind)) {
        #         totalKind as count(~kind)
        #     }

        #     data(func: uid(totalKind), orderdesc: val(totalKind), first: 1) {
        #         totalKind:val(totalKind)
        #         name
        #         ~kind @groupby(judge) {
        #             count(uid)
        #         }
        #     }
        # }"""

        # Do kind, ver quais ja o chamaram, e agrupar pelos juizes

        # res = self.make_query(query)
        # print(json.loads(res.json).get('data'))
        pass

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
        txn = self.client.txn()
        try:
            return txn.query(query)
        finally:
            txn.discard()
