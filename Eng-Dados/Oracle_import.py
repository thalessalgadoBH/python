import cx_Oracle
import os
from dotenv import load_dotenv

load_dotenv() 


userbd=os.getenv("USER_ORACLE")
passbd=os.getenv("SENHA_ORACLE")
stringbd=os.getenv("STRING_CON")

connection = cx_Oracle.connect(user=userbd, password=passbd, dsn=stringbd, encoding="UTF-8")


cur = connection.cursor()
for row in cur.execute("select * from teste"):
    print(row)