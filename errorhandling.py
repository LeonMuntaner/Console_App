from sqlalchemy.orm import Session
from sqlalchemy import desc
from fastapi import HTTPException
from database import SchemaList
from datetime import date

# Sets the schema settings for the database session
def set_schema_settings(schema: str, db: Session):
    # Check if the schema exists in the database
    if schema not in SchemaList or schema == "":
        raise HTTPException(status_code=404, detail=f"Schema \'{schema}\' does not exist in the database.")
    
    # If schema is not default 'patient'
    if schema != "public":
        db.connection(execution_options={"schema_translate_map": {'public': schema}})
    
    return db