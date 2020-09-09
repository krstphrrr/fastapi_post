from fastapi import FastAPI, Depends


from pydantic import BaseModel, constr
from typing import List
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import Session
from utils import crud, models, schemas
from utils.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

import pandas as pd
dd
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


# TestModel.from_orm(TestTable)

@app.get("/")
async def root():
    print('mere')
    return {"message": "Hello World"}

@app.post("/api/v0/add-new" , response_model=List[schemas.TestModel])
def add_new_data(item: schemas.TestModel, db:Session=Depends(get_db)):
    return item
