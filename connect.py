from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Base

engine = create_engine(
    "mysql+pymysql://user:pass@webdb.uvm.edu/dbname?charset=utf8mb4"
)

Base.metadata.create_all(engine)