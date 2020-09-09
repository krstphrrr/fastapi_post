import pandas as pd
import requests

txt_path = r"C:\Users\kbonefont\Desktop\201143010401R1_flux.txt"
df = pd.read_table(txt_path)
df
df_json= df.to_json(orient='records')
request.post('http://localhost:8000/api/v0/add-new', data=df_json)
