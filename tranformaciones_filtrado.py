import pandas as pd

datos = {
  'producto': ['A', 'B', 'C', 'D'],
  'cantidad': [10, 20, 30, 40],
  'precio': [100, 200, 300, 400]
}

df = pd.DataFrame(datos)

df_filtrado = df[df['cantidad'] > 10]
print(df_filtrado)
df_seleccion = df_filtrado[['producto', 'cantidad']] 
print(df_seleccion)
df_filtrado['total_venta'] = df_filtrado['cantidad'] * df_filtrado['precio']
print(df_filtrado)


#guardar DF en un archivo csv
df.to_csv('transformacionAvanzada.csv', index=False)
   
# df_seleccion = df[['columna1', 'columna2']]
# df['nueva_columna'] = df['columna1'] * df['columna2']
