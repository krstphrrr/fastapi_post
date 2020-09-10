import pandas as pd
import requests
import pickle
import base64

txt_path = r"C:\Users\kbon3efont\Desktop\201143010401R1_flux.txt"
df = pd.read_table(txt_path)

df_json = df.to_json(orient='records')

requests.post('http://localhost:8000/api/v0/add-new', data=df_json)
