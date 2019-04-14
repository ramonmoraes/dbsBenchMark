import pydgraph


class GraphAlter(object):
    def __init__(self):
        self.client = pydgraph.DgraphClient(pydgraph.DgraphClientStub("localhost:9080"))

    def drop_all(self):
        op = pydgraph.Operation(drop_all=True)
        self.client.alter(op)

    def create_schema(self, schema):
        op = pydgraph.Operation(schema=schema)
        self.client.alter(op)

    def re_create_db(self):
        self.drop_all()
        self.create_schema()
