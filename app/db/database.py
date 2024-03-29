from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os
from dotenv import load_dotenv

load_dotenv()

#DATABASE URL
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_NAME = os.getenv("DATABASE_NAME")

SQLALCHEMY_DATABASE_CONNECTION = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"

engine = create_engine(
    
    SQLALCHEMY_DATABASE_CONNECTION,
    #POOL CONNECTION AND OVERFLOW
    pool_size = 10,
    max_overflow = 20,
    pool_pre_ping = True,
    
    echo=os.getenv("SQLALCHEMY_ECHO", "false").lower() in ["true", "1"]
)

#Creating session local class instance 

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
)     

Base = declarative_base()