from modules.models.models import Person, Lawyer, Judge, Kind, CourtSection, Disctrict, Subject
from modules.dbs.sql.tableCreator import TableCreator

def create_simple_tables():
    tc = TableCreator(
        models=[
            Person(), Lawyer(), Judge(), Kind(), CourtSection(), Disctrict(), Subject()
        ]
    )
    tables = tc.create_tables()
    print("Creating simple tables")
    module_path = "modules/dbs/sql/config/simple_tables.sql"
    with open(module_path, "w") as f:
        f.writelines(tables)
