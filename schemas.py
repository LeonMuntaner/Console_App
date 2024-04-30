from pydantic import BaseModel
from typing import List, Optional

# Schema for patient table
class PatientBase(BaseModel):
    gender: str
    managingorganizationid: str
    identifier: str
    status_code: str
    # patient_id: str

# Schema for condition table
class ConditionBase(BaseModel):
    identifier: str
    casedefinition: str
    ageonset: str
    registrationdate: str
    localization: str
    comorbidity: List[str]
    diagnosis: str
    dstprofile: str
    weight: float
    height: float
    comments: str
    riskfactors: List[str]
    education: str
    employment: str
    totalcontacts: int
    totalchildren: int
    status_code: str
    dstnegativereason: str
    patient_id: str
    condition_id: str

# Schema for de_log table
class DeLogBase(BaseModel):
    uri: str
    resource: str
    method: str
    status_code: int
    content: str
    de_user: str
    run_ts: str
    body: str
    filename: str
    patient_id: str
    condition_id: str
    image_date: str
    modality: str
    isdicom: str
    runtime: int
    de_exception: str

# Schema for specimen table
class SpecimenBase(BaseModel):
    identifier: str
    registrationdate: str
    containeridentifier: str
    collected: str
    bodysite: str
    status_code: str
    patient_id: str
    condition_id: str



# for getting patient records in the database
class Patient(PatientBase):
    identifier: str
    
    class Config:
        orm_mode = True

# for getting condition records in the database
class Condition(ConditionBase):
    identifier: str
    
    class Config:
        orm_mode = True

# for getting de_log records in the database
class DeLog(DeLogBase):
    identifier: str
    
    class Config:
        orm_mode = True

# for getting specimen records in the database
class Specimen(SpecimenBase):
    identifier: str
    
    class Config:
        orm_mode = True