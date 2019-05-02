import pydgraph
import os

DEAFAULT_INDEXS = """
 is_lawyer: bool .
 is_courtsection: bool .
 is_kind: bool .
 estate: string .
 is_person: bool .
 is_subject: bool .
 last_name: string .
 name: string .
 is_judge: bool .
 is_lawsuit: bool .
 is_disctrict: bool .
"""


class DgraphOperations:
    def __init__(self):
        self.client = pydgraph.DgraphClient(pydgraph.DgraphClientStub("localhost:9080"))

    def drop_all(self):
        op = pydgraph.Operation(drop_all=True)
        self.client.alter(op)

    def create_index(self):
        op = pydgraph.Operation(schema=DEAFAULT_INDEXS)
        self.client.alter(op)

    def load_data(self):
        print("[Loading dgraph via os.system]")
        print("Executing script/liveLoad.sh")