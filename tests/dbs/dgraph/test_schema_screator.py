from modules.models.models import Person, Lawyer, Judge, Kind, CourtSection, Disctrict, Subject, Lawsuit
from modules.dbs.dgraph.schemaCreator import SchemaCreator

def test_schema_creator(snapshot):
    sc = SchemaCreator(
        models=[
            Person(), Lawyer(), Judge(), Kind(), CourtSection(), Disctrict(), Subject(), Lawsuit()
        ]
    )
    schemas = sc.create_schemas()
    snapshot.assert_match(schemas)