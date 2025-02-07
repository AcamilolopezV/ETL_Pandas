import requests
import pandas as pd

# Realizar una solicitud GET
response = requests.get('https://disease.sh/v3/covid-19/countries')
data = response.json()
df = pd.DataFrame(data)
print(df)
print(df.info())

