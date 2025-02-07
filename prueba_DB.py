import sqlite3
import pandas as pd

conexion = sqlite3.connect('nba_salary.sqlite')
cursor = conexion.cursor()
cursor.execute('SELECT * FROM NBA_season1718_salary LIMIT 5')
rows = cursor.fetchall()
df = pd.DataFrame(rows)
print(df)
conexion.close()


