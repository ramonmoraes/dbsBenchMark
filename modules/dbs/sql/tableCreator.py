from modules.models.models import (
    Person,
    Lawyer,
    Judge,
    Kind,
    CourtSection,
    Disctrict,
    Subject,
)
from modules.dbs.sql.tableCreator import TableCreator

TABLE_TEMPLATE = """CREATE TABLE IF NOT EXISTS {table_name} (
    id INT AUTO_INCREMENT,
    {columns},
    PRIMARY KEY (id)
);"""


def get_table_name(str):
    return "{}{}".format(str.lower(), "Table")


class TableCreator:
    def __init__(self, models):
        self.models = models

    def get_table_name(self, model):
        return get_table_name(model.__class__.__name__.lower())

    def create_tables(self):
        tables = []
        for model in self.models:
            columns = []
            for k, v in model.to_primitive().items():
                columns.append("{} {}".format(k, self.get_type(v)))
            table = TABLE_TEMPLATE.format(
                table_name=self.get_table_name(model), columns=",".join(columns)
            )
            tables.append(table)
        return tables

    def get_type(self, raw):
        val = type(raw)
        if val == type(""):  # string
            return "varchar(255)"
        if val == type(1):
            return "int"
        if val == type(True):
            return "boolean"
        raise Exception("Complex table", raw)

def create_simple_tables():
    tc = TableCreator(
        models=[
            Person(),
            Lawyer(),
            Judge(),
            Kind(),
            CourtSection(),
            Disctrict(),
            Subject(),
        ]
    )
    tables = tc.create_tables()
    print("Creating simple tables")
    module_path = "modules/dbs/sql/config/simple_tables.sql"
    with open(module_path, "w") as f:
        f.writelines(tables)
