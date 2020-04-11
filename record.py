import pyodbc as pd

conn = pd.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-I8FD6VJC\SQL2016;"
    "Database=Restaurant;"
    "Trusted_Connection=yes;"
)


def get(n, c, total):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO dbo.details(Name, "Contact No", Amount) values(?, ?, ?)',
                   (n, c, total)
                   )
    conn.commit()
    print("Details Entered")
