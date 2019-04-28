# import modules.dbs.sql.creator
import modules.dbs.sql.operations

ops = SqlOperations()
ops.load_data(["lawyerTable", "lawsuitlawyerTable"])
