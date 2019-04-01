from modules.models.models import Person, Lawyer, Judge, Kind, CourtSection, Disctrict, Subject, Lawsuit
from modules.dbs.dgraph.schemaCreator import SchemaCreator

def create_schema():
    sc = SchemaCreator(
        models=[
            Person(), Lawyer(), Judge(), Kind(), CourtSection(), Disctrict(), Subject(), Lawsuit()
        ]
    )
    schemas = sc.create_schemas()
    print("Creating simple schemas")
    module_path = "modules/dbs/dgraph/config/simple_schemas.txt"
    with open(module_path, "w") as f:
        f.writelines(schemas)
