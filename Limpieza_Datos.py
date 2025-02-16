import pandas as pd

# leer el archivo CSV
df = pd.read_csv('datos_ejemplo.csv')

#mostrar el df original
print(df)

# -----------------------------------------------------
# Manejo de valores nulos
# -----------------------------------------------------
#manejo de valores nulos
print("\nCantidad de Valores nulos por columna:")
print(df.isnull().sum())

#eliminar filas con valores nulos
df_sin_nulos = df.dropna()
print("\nDataFrame sin valores nulos:")
print(df_sin_nulos)

#rellenar valores nulos con un valor específico ejemplo 0 o 'desconocido'
df_con_relleno = df.fillna({'Salario': 0, 'Nombre': 'Desconocido'})
print("\nDataFrame con valores nulos rellenados:")
print(df_con_relleno)

# -----------------------------------------------------
# deteccion y correccion de errores en los tipos de datos
# -----------------------------------------------------
#intentar convertir la columna edad a numerica
df['Edad'] = pd.to_numeric(df['Edad'], errors='coerce')

#ver los tipos de datos de las columnas
print("\nTipos de datos antes de la correcion:")
print(df.dtypes)

#corregir valores no numericos en la columna Edad ejemplo convertir a NaN
df['Edad'] = df['Edad'].fillna(df['Edad'].mean()) #rellenar los Nan con el promedio de la columna

#ver los tipos de datos despues de la correcion
print("\nTipos de datos despues de la correcion:")
print(df.dtypes)

#ver df correjido
print("\nDataFrame corregido:")
print(df)

# -----------------------------------------------------
# Correcion de variables categoricas en numeros
# -----------------------------------------------------
df['Genero'] = df['Genero'].map({'F': 0, 'M': 1})# covertir en variable binaria 0 y 1
#usar la tecnica de get_dummies para convertir departamento en variables dummy
df_genero = pd.get_dummies(df, columns=['Departamento'], drop_first=True)

#ver df final
print("\nDataFrame final:")
print(df_genero)


