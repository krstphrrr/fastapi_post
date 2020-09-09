from fastapi import FastAPI, Depends
from fastapi.encoders import jsonable_encoder
import os, os.path

from pydantic import BaseModel, constr, parse_obj_as
from typing import List
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import Session
from utils import crud, models, schemas
from utils.database import SessionLocal, engine
import pickle
import base64
from pandas.io.json import json_normalize

models.Base.metadata.create_all(bind=engine)

import pandas as pd

app = FastAPI()
txt_path = r"C:\Users\kbonefont\Desktop\201143010401R1_flux.txt"


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



    # class Config:
    #     orm_mode = True

output_path = r"C:\Users\kbonefont\Desktop\output"
# TestModel.from_orm(TestTable)
Test = schemas.TestModel
# Test.parameter_set
@app.get("/")
async def root():
    print('mere')
    return {"message": "Hello World"}

@app.post("/api/v0/add-new")
def respond(data:List[Test]=None):
    # m = [i for i in data]
    m = pd.DataFrame(jsonable_encoder(data))
    # m = parse_obj_as(Test, data[0])
    print(m)
    # json_comp = jsonable_encoder(data)
    # #
    # df = pd.read_json(data[0], orient='records')
    # print(df)
    # print(type(df))
    # print(df.loc[:5,:])
    # df.to_csv(os.path.join(output_path,"test.csv"))
    # return data
    # res_pickled = pickle_dump.decode('utf-8')
    # data_dict = pd.DataFrame(data.dict())
    # print(type(data))
    # try:
    #     df = pickle_loads(base64.b64decode(res_pickled.encode()))
    #     return pickle.dumps(df)
    # except Exception as e:
    #     print(e)
    #     return pickle.dumps(pd.DataFrame())
    # return "ok"
