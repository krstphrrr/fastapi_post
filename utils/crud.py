from sqlalchemy.orm import Session

from utils import models, schemas



def create_test_table(db:Session, item:schemas.TestModel):
    items = models.TestTable
    db.add(items)
    db.commit()
    db.refresh(items)
    return items
