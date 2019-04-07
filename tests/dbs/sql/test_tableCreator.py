from modules.dbs.sql.tableCreator import TableCreator
from schematics.models import Model
from schematics.types import StringType, ListType, BooleanType, ModelType


class SimpleModel(Model):
    foo = StringType(default="")
    bar = False


def test_table_name(snapshot):
    tc = TableCreator(models=[SimpleModel()])

    snapshot.assert_match(tc.get_table_name(SimpleModel()))


def test_simlpe_create_table(snapshot):
    tc = TableCreator(models=[SimpleModel()])

    snapshot.assert_match(tc.create_tables()[0])


def test_get_type(snapshot):
    tc = TableCreator(models=[SimpleModel()])

    snapshot.assert_match(tc.get_type(""))
    snapshot.assert_match(tc.get_type(True))
    snapshot.assert_match(tc.get_type(1))
