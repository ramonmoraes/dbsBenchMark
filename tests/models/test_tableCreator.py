from modules.models.tableCreator import TableCreator
from schematics.models import Model
from schematics.types import StringType, ListType, BooleanType, ModelType

class SimpleModel(Model):
    foo = StringType(default="")
    bar = False

def test_table_name(snapshot):
    tc = TableCreator(
        models=[SimpleModel()]
    )

    snapshot.assert_match(tc.get_table_name(SimpleModel()))

def test_simlpe_create_table(snapshot):
    tc = TableCreator(
        models=[SimpleModel()]
    )

    snapshot.assert_match(tc.create_tables()[0])
