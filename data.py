## pandas dataframes for appointment, patient, and doctor data

import pandas as pd
import numpy as np
import datetime as datetime

'''
dates = pd.DataFrame({'date': ['10/05/2024', '10/06/2024', '10/07/2024', '10/08/2024', '10/09/2024']})
times = pd.DataFrame({'time': ['8:00','8:15','8:30']})

doctors = pd.DataFrame({'speciality': ['Dr.A', 'Dr.B', 'Dr.C', 'Dr.D', 'Dr.E', 'Dr.F'],'specialty': ['cardiology', 'cardiology', 'dermatologist', 'family doctor', 'pediatrician', 'gynecologist']})
specialities = ['']
'''

class Doctor:
    def __init__(self, doctor_id, doctor_name, specialty, available):
        self.doctor_id = doctor_id
        self.doctor_name = doctor_name
        self.specialty = specialty
        self.available = available
    
    def specialty(self):
        return self.specialty

doctors = []
doctors.append(Doctor("123", "Sam", "Cardiology", True))    #list of doctors

def selection(user_specialty):
    
    special_dr = []
    for i in doctors:
        if i.specialty().casefold() == user_specialty.casefold():
            special_dr.append(special_dr)
    return special_dr


def main():
    user_specialty = input("Enter a specialty: ")    #user will input a specialty
    list = selection(user_specialty)
    return list

if __name__ == "__main__":
    main()