from database import SessionLocal
from crud import test_get_patient, test_get_specimen
from rich import print

db = SessionLocal()

# patients = test_get_patient(db)
patients = test_get_specimen(db)

# for patient in patients:
#     print(
#         f"uri: {patient.uri}\n"
#         f"resource: {patient.resource}\n"
#         f"method: {patient.method}\n"
#         f"de_user: {patient.de_user}\n"
#         f"run_ts: {patient.run_ts}\n"
#         f"body: {patient.body}\n"
#         f"patient_id: {patient.patient_id}\n"
#     )

for patient in patients:
    print(patient)

db.close()