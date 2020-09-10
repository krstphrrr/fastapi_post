from fastapi import FastAPI, Depends
from fastapi.encoders import jsonable_encoder
import os, os.path

from pydantic import BaseModel, constr, parse_obj_as
from typing import List

from utils import crud, models, schemas
from utils.database import SessionLocal, engine

from pandas.io.json import json_normalize


import pandas as pd

app = FastAPI()

@app.get("/")
def root():
    return {"message": "fastapi for post requests up!"}

@app.post("/api/v0/add-new")
def respond(data:List[Test]=None):

    m = pd.DataFrame(jsonable_encoder(data))

    print(m)
