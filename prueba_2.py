import pandas as pd

# #leer el archivo csv
# df = pd.read_csv("AB_NYC_2019.csv", sep=",",quotechar='"')
# #mostrfar las primera filas del fataframe
# print(f"\n {df.head()}")
# #informacion general del dataframe
# print(f"\n {df.info()}")
# #estadisticas del dataframe
# print(f"\n {df.describe()}")

#leer archivo excel
df = pd.read_excel("data.xlsx")
#mostrfar las primera filas del fataframe
print(f"\n {df.head()}")
#informacion general del dataframe
print(f"\n {df.info()}")
#estadisticas del dataframe
print(f"\n {df.describe()}")