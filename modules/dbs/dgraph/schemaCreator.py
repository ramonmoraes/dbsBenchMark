SCHEMA_TEMPLATE = """ {label}: {type} . \n"""

class SchemaCreator:
    def __init__(self, models):
        self.models = models


    def get_identifier(self, model):
        identifier_label = "is_{}".format(model.__class__.__name__.lower())
        return SCHEMA_TEMPLATE.format(
            label=identifier_label,
            type=self.get_type(True)
        )



    def create_schemas(self):
        schemas = []
        for model in self.models:
            schemas.append(
                self.get_identifier(model)
            )
            for k, v in model.to_primitive().items():
                index_type=self.get_type(v)
                if index_type:
                    schema = SCHEMA_TEMPLATE.format(
                        label=k,
                        type=index_type
                    )
                    schemas.append(schema)
        return list(set(schemas))



    def get_type(self, raw):
        val = type(raw)
        if val == type(""):
            return "string"
        if val == type(1):
            return "double"
        if val == type(True):
            return "bool"
        return None