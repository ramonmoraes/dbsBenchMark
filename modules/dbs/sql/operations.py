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
        print("[Recreating sql database]")
        for querie in querys:
            print(".", end="")
            cursor.execute(querie)
            connection.commit()
        print("[Done]")

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
        print("[Creating sql tables]")
        for command in commands:
            print(".", end="")
            cursor = connection.cursor()
            cursor.execute(command)
        print("[Done]")

    def load_data(
        self,
        tables=[
            "kindTable",
            "judgeTable",
            "personTable",
            "lawsuitTable",
            "lawyerTable",
            "lawsuitlawyerTable",
            "lawsuitpersonTable",
        ],
    ):
        cursor = connection.cursor()
        path = "data/csv/{table_name}.csv"
        command_template = """
    LOAD DATA LOCAL INFILE "{path}"
    INTO TABLE {table_name}
    COLUMNS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\r\n'
    IGNORE 1 ROWS
    ({columns});
        """
        print("[Loading sql data]")
        for table in tables:
            table_path = path.format(table_name=table)
            columns = ""
            print("Getting columns from", table_path)
            with open(table_path, "r") as f:
                columns = f.readline().strip()

            print("Loading into table:", table)
            command = command_template.format(
                table_name=table, path=table_path, columns=columns
            )
            print(command)
            cursor.execute(command)

        self.print_cursor(cursor)
        connection.commit()
        print("[Done]")
