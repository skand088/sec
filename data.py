## pandas dataframes for appointment, patient, and doctor data

import pandas as pd
import numpy as np
import datetime as datetime


dates = pd.DataFrame({'date': ['10/05/2024', '10/06/2024', '10/07/2024', '10/08/2024', '10/09/2024']})
times = pd.DataFrame({'time': ['8:00','8:15','8:30']})

doctors = pd.DataFrame({'speciality': ['Dr.A', 'Dr.B', 'Dr.C', 'Dr.D', 'Dr.E', 'Dr.F'],'specialty': ['cardiology', 'cardiology', 'dermatologist', 'family doctor', 'pediatrician', 'gynecologist']})
specialities = specialties = [
    'Cardiologist',
    'Family Doctor',
    'Dermatologist',
    'Oncologist',
    'Pediatrician',
    'Psychiatrist',
    'Gynaecologist',
    'Anesthesiologist'
]