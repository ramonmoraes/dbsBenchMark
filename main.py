# from modules.benchmark import BenchMark
# benchmark = BenchMark()
# benchmark.create_mysql_db()
# benchmark.insert_mysql_data()

from modules.dbs.dgraph.creator import DgraphCreator

c = DgraphCreator()

c.create_nquad()

# from modules.dbs.dgraph.operations import DgraphOperation

# # ops = DgraphOperation()
# # ops.drop_all()

# client = DgraphOperation().client


# import pydgraph
# # schema = 'name: string @index(exact) .'
# # op = pydgraph.Operation(schema=schema)


# txn = client.txn()
# try:
#     # res = txn.query(
#     #     """
#     #         {
#     #             data(func: has(name)) {
#     #                 name
#     #             }
#     #         }
#     #     """
#     # )
#     # print(res)
#     txn.mutate(set_nquads=nquads)
# #     schema = 'name: string @index(exact) .'
# #     op = pydgraph.Operation(schema=schema)
#     txn.commit()
# finally:
#     txn.discard()
