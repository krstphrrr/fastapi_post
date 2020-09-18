from fastapi import FastAPI, Depends
from fastapi.encoders import jsonable_encoder
import os, os.path

from pydantic import BaseModel, constr, parse_obj_as
from typing import List

from utils import crud, models, schemas
from utils.database import SessionLocal, engine
# to actually ingest
from tall_tables.talltables_handler import ingesterv2
# to create tables and check for existence
from dima.tabletools import table_create, tablecheck
# aero test run:
from aero.aero import model_run_updater
from pandas.io.json import json_normalize


import pandas as pd

app = FastAPI()
Test = schemas.TestModel

@app.get("/")
def root():
    return {"message": "fastapi for post requests up!"}

@app.post("/met")
def post_met():
    """
    will receive a jsonified .dat file from a scraper api
    "List" model cannot be used, but..also
    how can I keep columns flexible ?
    - maybe create an on the fly table schema?

    needs to:
    1. check timestamp to not ingest dups
    2. add any column present on pg table, not present on current df

    """
    m
    # return {"message":"met data uploader"}

@app.post("/nri")
def post_nri():
    return {"message":"nri data uploader"}

@app.post("/tall")
def post_tall(data:List[Test]=None):

    m = pd.DataFrame(jsonable_encoder(data))

    print(m)
# aero test
@app.post("/aero")
def post_aero(data:List[Test]=None):
    m = pd.DataFrame(jsonable_encoder(data))
    model_run_updater(m)
    # print(m)
