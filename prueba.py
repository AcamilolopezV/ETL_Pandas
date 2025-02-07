# import pandas as pd
# import requests

# url = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=your_api_key"
# response = requests.get(url)

# if response.status_code == 200:
#     weather_data = response.json()
#     df = pd.json_normalize(weather_data)
#     print(df.head())
# else:
#     print(f"Error en la solicitud: {response.status_code}")

import pandas as pd
import requests

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
data = response.json()
df = pd.DataFrame(data)
print(f"\n {df.head()}")
