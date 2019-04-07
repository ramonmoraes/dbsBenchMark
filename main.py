# import modules.dbs.sql.operations
from modules.models.models import *

p = Person({"nome": "dart"})
print(p)
print(p.create_nquad())