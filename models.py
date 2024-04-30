# This file contains the SQLAlchemy models for the database tables.
from sqlalchemy import Column, Integer, String, Numeric, DateTime, BIGINT, ARRAY
from sqlalchemy.orm import relationship
from database import Base

# Tells SQLAlchemy the name of the table to use in the database
class Patient(Base):
    __tablename__ = "patient"
    __table_args__ = {"schema": "public"}
    
    gender = Column("gender", String(50))
    managingorganizationid = Column("managingorganizationid", String(50))
    identifier = Column("identifier", String(50), primary_key=True, nullable=False)
    status_code = Column("status_code", String(5))

# Create the model for the Condition table
class Condition(Base):
    __tablename__ = "condition"
    __table_args__ = {"schema": "public"}
    
    identifier = Column("identifier", String(100), primary_key=True, nullable=False)
    casedefinition = Column("casedefinition", String(100))
    ageonset = Column("ageonset", String(50))
    registrationdate = Column("registrationdate", String(50))
    localization = Column("localization", String(50))
    comorbidity = Column("comorbidity", ARRAY(String))
    diagnosis = Column("diagnosis", String(100))
    dstprofile = Column("dstprofile", String(100))
    weight = Column("weight", Numeric(3, 2))
    height = Column("height", Numeric(3, 2))
    comments = Column("comments", String(100))
    riskfactors = Column("riskfactors", ARRAY(String))
    education = Column("education", String(100))
    employment = Column("employment", String(100))
    totalcontacts = Column("totalcontacts", Integer)
    totalchildren = Column("totalchildren", Integer)
    status_code = Column("status_code", String(5))
    dstnegativereason = Column("dstnegativereason", String(100))
    patient_id = Column("patient_id", String(50))
    condition_id = Column("condition_id", String(50))

# Create the model for the De_log table
class DeLog(Base):
    __tablename__ = "de_log"
    __table_args__ = {"schema": "public"}
    
    id = Column("id", Integer, primary_key=True, nullable=False)
    uri = Column("uri", String(100))
    resource = Column("resource", String)
    method = Column("method", String)
    status_code = Column("status_code", Integer)
    content = Column("content", String)
    de_user = Column("de_user", String)
    run_ts = Column("run_ts", DateTime(timezone=False))
    body = Column("body", String)
    filename = Column("filename", String)
    patient_id = Column("patient_id", String)
    condition_id = Column("condition_id", String)
    image_date = Column("image_date", DateTime(timezone=False))
    modality = Column("modality", String)
    isdicom = Column("isdicom", String)
    runtime = Column("runtime", BIGINT)
    de_exception = Column("de_exception", String)

# Create the model for the Specimen table
class Specimen(Base):
    __tablename__ = "specimen"
    __table_args__ = {"schema": "public"}
    
    identifier = Column("identifier", String(100), primary_key=True, nullable=False)
    registrationdate = Column("registrationdate", String(50), nullable=False)
    containeridentifier = Column("containeridentifier", String(100), primary_key=True, nullable=False)
    collected = Column("collected", String(100))
    bodysite = Column("bodysite", String(100))
    status_code = Column("status_code", String(5))