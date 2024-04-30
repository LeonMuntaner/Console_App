from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Postgres engine instance 
SQLALCHEMY_DATABASE_URL = "postgresql://your_username:password@server/DatabaseName"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Get the list of schemas in the database
SchemaList = inspect(engine).get_schema_names()

# Each instance of the SessionLocal class will be a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# We will inherit from this class to create each of the database models
Base = declarative_base()