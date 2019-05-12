import csv
from modules.relatedModels import get_related_model, load_dataset
from modules.dbs.sql.tableCreator import get_table_name


def format_col_values(val):
    if type(val) == type("str"):
        return '"{}"'.format(val)
    if type(val) == type(True):
        return str(val).lower()
    return val


def create_query(table, objs):
    if type(objs) != type([]):
        objs = [objs]

    queries = []
    for obj in objs:
        query_template = "INSERT INTO {table} ({columns}) VALUES ({values});"
        columns = obj.keys()
        values = list(map(format_col_values, obj.values()))

        columns = " ,".join(columns)
        values = " ,".join(values)
        queries.append(
            query_template.format(table=table, columns=columns, values=values)
        )
    return queries


def get_queires():
    for lawsuit in get_related_model(0.0001)[1:2]:
        data = lawsuit.to_primitive()
        law_dict = {"number": data.pop("number")}
        queries = []
        for k, v in data.items():
            if v:
                queries.extend(create_query(get_table_name(k), v))
        queries.extend(create_query(get_table_name("lawsuits"), law_dict))
        for q in queries:
            print(q)
