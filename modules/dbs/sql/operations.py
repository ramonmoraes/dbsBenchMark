from modules.dbs.sql.connection import connection
from os.path import abspath

class SqlOperations:
    def print_cursor(self, cursor):
        for res in cursor.fetchall():
            print(res)

    def recreate_database(self):
        cursor = connection.cursor()
        commands = """SET FOREIGN_KEY_CHECKS = 0;
    SET @tables = NULL;
    SELECT GROUP_CONCAT(table_schema, '.', table_name) INTO @tables
    FROM information_schema.tables
    WHERE table_schema = 'db';

    SET @tables = CONCAT('DROP TABLE ', @tables);
    PREPARE stmt FROM @tables;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
    SET FOREIGN_KEY_CHECKS = 1; """
        querys = commands.split(";")
        querys = filter(lambda x: x.strip(), querys)
        querys = map(lambda s: "{}{}".format(s, ";"), querys)
        for querie in querys:
            print("Querie:", querie)
            cursor.execute(querie)
            connection.commit()

    def create_tables(self):
        base_config_path = "modules/dbs/sql/config/"
        schemas_paths = list(
            map(
                lambda name: "{}{}".format(base_config_path, name),
                ["simple_tables.sql", "complex_tables.sql"],
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
            print("Executing command:", command)
            cursor = connection.cursor()
            cursor.execute(command)

    def load_data(self):
        cursor = connection.cursor()
        print("Loading")
        tables = [
            "kindsTable",
            "judgesTable",
            "related_people",
            "lawsuits",
        ]
        command_template = """
    LOAD DATA LOCAL INFILE "data/csv/{table_name}.csv"
    INTO TABLE kindTable
    COLUMNS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\r\n'
    IGNORE 1 ROWS
    (name);
        """
        for table in tables:
            print("Loading table:", table)
            cursor.execute(command_template.format(table_name=table))
        print_cursor(cursor)
        connection.commit()

ops = SqlOperations()
ops.recreate_database()
ops.create_tables()
ops.load_data()