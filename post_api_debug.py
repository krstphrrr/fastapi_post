import pandas as pd
import requests
import pickle
import base64

txt_path = r"C:\Users\kbonefont\Desktop\201143010401R1_flux.txt"
df = pd.read_table(txt_path)

df_json = df.to_json(orient='records')
df_json
requests.post('http://localhost:5009/aero', data=df_json)
requests.post('http://localhost:8000/aero', data=df_json)
