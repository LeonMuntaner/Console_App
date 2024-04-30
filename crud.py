import json
import models
from sqlalchemy.orm import Session
from datetime import datetime
from schemas import Patient, Condition

# Function to get the patient records from the database
def test_get_patient(db: Session):
    try:
        patients = db.query(models.Patient).filter(models.Patient.status_code == '201').all()
        
        de_log_entries = []
        for patient in patients:
            patient_clone = {
                "gender": patient.gender,
                "managingorganizationid": patient.managingorganizationid,
                "identifier": patient.identifier
            }
            
            condition = db.query(models.Condition).filter(models.Condition.identifier == patient.identifier).first()
            
            if condition is None:
                print(f"No condition record found for patient {patient_clone.identifier}")
                print("Record was not created because an associated condition was not found.")
                continue
            
            # Request condition object
            condition_clone = {
                "identifier": condition.identifier,
                "casedefinition": condition.casedefinition,
                "ageonset": condition.ageonset,
                "registrationdate": condition.registrationdate,
                "localization": condition.localization,
                "comorbidity": condition.comorbidity,
                "diagnosis": condition.diagnosis,
                "dstprofile": condition.dstprofile,
                "weight": condition.weight,
                "height": condition.height,
                "comments": condition.comments,
                "riskfactors": condition.riskfactors,
                "education": condition.education,
                "employment": condition.employment,
                "totalcontacts": condition.totalcontacts,
                "totalchildren": condition.totalchildren,
                "status_code": condition.status_code,
                "dstnegativereason": condition.dstnegativereason
            }
            
            # Adding the condition clone to the patient clone
            patient_clone.update(condition_clone)
            
            _log = models.DeLog(
                uri = "fake_uri",
                resource = "patient",
                method = "POST",
                de_user = "NIH\muntanerl2",
                run_ts = datetime.now(),
                body = json.dumps(patient_clone),
                patient_id = patient_clone['identifier']
            )
            
            de_log_entries.append(_log)
            
            # From this point on, the code would call the DataEntryAPI to create the patient record.
            # The response would be logged in the de_log table, along with the status code.
            # I would also need to add the URI, and token as a parameter to the function.
        return de_log_entries
    except Exception as e:
        print(e)
        return None

# Function to get the specimen records from the database
def test_get_specimen(db: Session):
    try:
        patients = []
        for log in db.query(models.DeLog).filter((models.DeLog.resource == 'patient') & (models.DeLog.status_code == 201)).all():
            patients.append(json.loads(log.content))
        
        # Get the Specimens with status code not equal to '201'
        specimens = db.query(models.Specimen).filter(models.Specimen.status_code != 201).all()
        
        de_log_entries = []
        for specimen in specimens:
            try:
                # Request Object (Specimen)
                specimen_clone = models.Specimen(
                    body_site = specimen.body_site,
                    collected = specimen.collected,
                    registration_date = specimen.registration_date,
                    identifier = specimen.identifier,
                    container_identifier = specimen.container_identifier
                )
                
                _patient_id = ''
                _condition_id = ''
                patient = next((x for x in patients if x['identifier'] == specimen_clone.identifier), None)
                
                # If no patient information, move to the next specimen record
                if patient is None:
                    continue
                
                if patient is not None and 'condition' in patient:
                    _patient_id = patient['id']
                    _condition_id = patient['condition']['id']
                else:
                    continue
                
                specimen_clone.patient_id = _patient_id
                specimen_clone.condition_id = _condition_id
                
                _log = models.DeLog(
                    uri = "fake_uri",
                    resource = "/patient/" + specimen_clone.patient_id + "/condition/" + specimen_clone.condition_id + "/specimen",
                    method = "POST",
                    de_user = "NIH\muntanerl2",
                    run_ts = datetime.now(),
                    body = json.dumps(specimen_clone),
                    patient_id = specimen_clone.identifier
                )
                
                de_log_entries.append(_log)
            except Exception as e:
                print(e)
        
        return de_log_entries
    except Exception as e:
        print(e)
        return None