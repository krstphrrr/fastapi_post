
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from utils.tools import db


def engine_conn_string(string):
    d = db(string)
    return f'postgresql://{d.params["user"]}:{d.params["password"]}@{d.params["host"]}:{d.params["port"]}/{d.params["dbname"]}'

engine = create_engine(
    engine_conn_string('dima')
)
SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
