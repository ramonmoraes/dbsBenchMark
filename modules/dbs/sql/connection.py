import MySQLdb

connection = MySQLdb.connect(
    host="127.0.0.1", port=3306, user="user", password="password", db="db"
)
