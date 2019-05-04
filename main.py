import pydgraph
from modules.benchmark import BenchMark
from modules.dbs.dgraph.operations import DgraphOperations

# benchmark = BenchMark()
# benchmark.create_dgraph_db()
# benchmark.create_dgraph_data()
# benchmark.insert_dgraph_data()

# benchmark.create_mysql_db()
# benchmark.insert_mysql_data()


client = DgraphOperations().client
txn = client.txn()
try:
    res = txn.query(
        """
            {
                data(func: has(name)) {
                    name
                }
            }
        """
    )
    print(res)
    txn.commit()
finally:
    txn.discard()
