import pandas as pd

data = {
    'producto': ['A', 'B', 'A', 'B'],
    'ventas': [10, 20, 30, 40]
}
df = pd.DataFrame(data)
grupo = df.groupby('producto').agg({'ventas': ['sum', 'mean']})
print(grupo)
