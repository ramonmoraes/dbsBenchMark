import pydgraph
import json

from modules.benchmark import BenchMark
from modules.dbs.dgraph.operations import DgraphOperations


benchmark = BenchMark()
# benchmark.create_dgraph_db()
# benchmark.create_dgraph_data()
# benchmark.insert_dgraph_data()
benchmark.make_queries()

# benchmark.create_mysql_db()
# benchmark.insert_mysql_data()
