import pyodbc

SERVER = "DESKTOP-AGPK6AM"
DATABASE = "hangman"

connectionString = f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Integrated Security=True;'
conn = pyodbc.connect(connectionString)

cursor= conn.cursor()
cursor.execute("SELECT Word FROM tWords")

records = cursor.fetchall()

for r in records:
    rec=[]
    for col in r:
        rec.append(col)
    print(rec)
