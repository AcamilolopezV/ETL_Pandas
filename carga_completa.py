import pandas as pd

# Dataset inicial
data_base = {
    'id': [1, 2, 3],
    'producto': ['Camisa', 'Pantalón', 'Zapatos'],
    'cantidad': [10, 5, 8]
}
df_base = pd.DataFrame(data_base)
print("Base inicial:")
print(df_base)

# Nueva carga completa
data_nueva = {
    'id': [1, 2, 3],
    'producto': ['Camisa', 'Pantalón', 'Zapatos'],
    'cantidad': [15, 7, 12]
}
df_completa = pd.DataFrame(data_nueva)
print("\nCarga completa (nueva base):")
print(df_completa)
