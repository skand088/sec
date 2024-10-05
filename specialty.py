## pandas dataframes for appointment, patient, and doctor data

import datetime as datetime
from nicegui import ui

'''
dates = pd.DataFrame({'date': ['10/05/2024', '10/06/2024', '10/07/2024', '10/08/2024', '10/09/2024']})
times = pd.DataFrame({'time': ['8:00','8:15','8:30']})

doctors = pd.DataFrame({'speciality': ['Dr.A', 'Dr.B', 'Dr.C', 'Dr.D', 'Dr.E', 'Dr.F'],'specialty': ['cardiology', 'cardiology', 'dermatologist', 'family doctor', 'pediatrician', 'gynecologist']})
specialities = ['']
'''
class ToggleButton(ui.button):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._state = True
        self.on('click', self.toggle)

    def toggle(self) -> None:
        """Toggle the button state."""
        self._state = not self._state
        self.update()
        if not self._state:
            ui.navigate.to('/Booking and Availability')

    def update(self) -> None:
        self.props(f'color={"green" if self._state else "red"}')
        super().update()
        
class Time:
    def __init__(self, time, avail):
        self.time = time
        self.avail = avail

    def get_time(self):
        return self.time
    
    def get_avail(self):
        return self.avail
    
    def set_avail(self, avail):
        self.avail = avail
    
ls =[Time('9:00am', True),Time('10:00am', True),Time('11:00am', True),
     Time('1:00pm', True),Time('2:00am', True),Time('3:00am', True),Time('4:00am', True)]
for i in ls:
    if i.get_avail() == True:
        ToggleButton(i.get_time())


class Users:
    def __init__(self, patient_id, name, contact):
        self.patient_id = patient_id
        self.name = name
        self.contact = contact
        self.booked = True

    patient_bookings =[Time('9:00am', True),Time('10:00am', True),Time('11:00am', True),
                       Time('1:00pm', True),Time('2:00am', True),Time('3:00am', True),Time('4:00am', True)]


class Doctor:
    def __init__(self, doctor_id, doctor_name, specialty, available):
        self.doctor_id = doctor_id
        self.doctor_name = doctor_name
        self.specialty = specialty
        self.available = available
    
    def get_specialty(self):
        return self.specialty
    
    def get_name(self):
        return self.doctor_name

doctors = []
doctors.append(Doctor("123", "Sam", "Cardiology", True))    #list of doctors

def selection(user_specialty):
    
    special_dr = []
    for i in doctors:
        if i.get_specialty().casefold() == user_specialty.casefold():
            special_dr.append(i)
    return special_dr


def main():
    ls = selection('Cardiology')
    '''
    for i in ls:
        print(i.get_name())
    '''
    return ls


if __name__ == "__main__":
    main()

## website interfacing

## times

@ui.page('/Booking and Availability')
def booking():
    with ui.header(elevated=True).style('background-color: #ff9999').classes('items-center justify-between'):
        ui.label('View Doctor Booking and Availability')
    with ui.footer().style('background-color: #ff9999'):
        with ui.row():
            ui.button('Back To Bookings', on_click=ui.navigate.back)




        
ui.run()

