TABLE_TEMPLATE = "CREATE TABLE {table_name} ({columns});"

class TableCreator:
    def __init__(self, models):
        self.models = models
        # self.create_tables()


    def get_table_name(self, model):
        return "{}{}".format(model.__class__.__name__.lower(), "Table")


    def create_tables(self):
        tables = []
        for model in self.models:
            columns = []
            for k, v in model.to_primitive().items():
                columns.append(
                    "{} {}".format(k, self.get_type(v))
                )
            table = TABLE_TEMPLATE.format(
                table_name=self.get_table_name(model),
                columns= ",".join(columns)
            )
            tables.append(table)
        return tables



    def get_type(self, raw):
        val = type(raw)
        if val == type(""): # string
            return "varchar(255)"
        if val == type(1):
            return "int"
        if val == type(True):
            return "boolean"
        raise Exception("Not found type for", raw)