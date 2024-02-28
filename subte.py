import requests
import pandas as pd
from datetime import datetime, date, timedelta
import os

url = "https://raw.githubusercontent.com/LeoDataEngineer/etl_snowflake_actions/main/data_snow/data_snow.csv"

# Leer el archivo CSV utilizando pandas
df = pd.read_csv(url)

# Obtener la ruta al directorio actual del script
ruta_actual = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta al directorio "data"
ruta_data = os.path.join(ruta_actual, "data")

# Crear la carpeta "data" si no existe
if not os.path.exists(ruta_data):
    os.makedirs(ruta_data)

# Construir la ruta al archivo CSV dentro de la carpeta "data"
ruta_csv = os.path.join(ruta_data, "subte.csv")

# Supongamos que tienes un DataFrame llamado df

# Escribir el DataFrame en un archivo CSV en la ruta especificada
df.to_csv(ruta_csv, index=False)

# Construir la ruta al archivo CSV dentro de la carpeta "data"


