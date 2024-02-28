import requests
import pandas as pd
from datetime import datetime, date, timedelta


url = "https://raw.githubusercontent.com/LeoDataEngineer/etl_snowflake_actions/main/data_snow/data_snow.csv"

# Leer el archivo CSV en un DataFrame de pandas
df = pd.read_csv(url)

# Escribir el DataFrame en un archivo CSV en la ruta especificada
df.to_csv("data/subte.csv", index=False)

# Construir la ruta al archivo CSV dentro de la carpeta "data"


