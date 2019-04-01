from modules.dbs.sql.connection import connection

def create_tables():
    base_config_path="modules/dbs/sql/config/"
    schemas_paths = list(
        map(
            lambda name: "{}{}".format(base_config_path, name), ["simple_tables.sql", "complex_tables.sql"]
        )
    )

    commands = []
    for path in schemas_paths:
        with open(path, "r") as f:
            lines = f.read()
            querys = lines.split(";")
            querys = filter(lambda x: x.strip(), querys)
            querys = map(lambda s: "{}{}".format(s, ";"), querys)
            commands.extend(querys)

    for command in commands:
        print("Executing command:",command)
        cursor = connection.cursor()
        cursor.execute(command)
