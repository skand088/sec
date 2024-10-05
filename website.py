from nicegui import ui

time_slots = {
    '9:00am': True, '10:00am': True, '11:00am': True,
    '1:00pm': True, '2:00pm': True, '3:00pm': True, '4:00pm': True
}

booked_times = []


with ui.tabs().classes("w-full") as tabs:
    home = ui.tab("Home")
    contact = ui.tab("Contact")
    settings = ui.tab("Settings")

def set_background(color: str) -> None:
    ui.query('body').style(f'background-color: {color}')

with ui.tab_panels(tabs, value = settings).classes("w-full"):
    with ui.tab_panel(settings):
        dark = ui.dark_mode()
        with ui.row():
            ui.button('Pink', on_click=lambda: set_background('#ff9999'))
            ui.button('Teal', on_click=lambda: set_background('#26A69A'))
            ui.button("Dark", on_click = dark.enable)
            ui.button("Light", on_click = dark.disable)

@ui.page('/Booking and Availability Family Doctor')
def booking():
    with ui.header(elevated=True).style('background-color: #ff9999').classes('items-center justify-between'):
        ui.label('View DoctorBooking and Availability')
    ui.date(value = "2024-10-05")
    with ui.row().classes('justify-center'):
                for time, available in time_slots.items():
                    def create_button(time):
                        def toggle_booking():
                            if time in booked_times:
                                booked_times.remove(time)
                                time_slots[time] = not time_slots[time]
                            else:
                                booked_times.append(time)
                                time_slots[time] = not time_slots[time]

                            button.props(f'color={"green" if time not in booked_times else "red"}')
                            button.update() 

                            booking_info.set_text(f"Currently booked times: {', '.join(booked_times) if booked_times else 'None'}")
                        button = ui.button(time, on_click=toggle_booking)
                        button.props(f'color={"green" if available else "red"}')
                        return button
                    
                    create_button(time)
                        
                booking_info = ui.label(f"Currently booked times: {', '.join(booked_times) if booked_times else 'None'}")


    with ui.footer().style('background-color: #ff9999'):
        with ui.row():
            ui.button('Back To Bookings', on_click=ui.navigate.back)
            with ui.dialog() as dialog, ui.card():
                ui.label(f"Your reservations are confirmed")
                ui.button('Close', on_click = dialog.close)
            ui.button("Confirm Booking", on_click = dialog.open)
    class ToggleButton(ui.button):

        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self._state = True
            self.on('click', self.toggle)

        def toggle(self) -> None:
            """Toggle the button state."""
            if self._state == True:
                self._state = not self._state
                self.update()
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
    

    patient_bookings =[Time('9:00am', True),Time('10:00am', True),Time('11:00am', True),
                    Time('1:00pm', True),Time('2:00am', True),Time('3:00am', True),Time('4:00am', True)]

    class Patient:

        def __init__(self, patient_id, name, contact, patient_bookings):
            self.patient_id = patient_id
            self.name = name
            self.contact = contact
            self.booked = True
            self.patient_bookings = patient_bookings

    patients = []
    patients.append(Patient("321", "Jill", "jill@mail.com", patient_bookings))    #list of all patients

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
    doctors.append(Doctor("123", "Sam", "Cardiology", True))    #list of all doctors

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
            ui.button('Back To Doctors', on_click=ui.navigate.back)
@ui.page('/doctors')
def doctor():
    with ui.card().tight():
        with ui.card_section():
            ui.label("Dr.A")
        with ui.card_actions():
            ui.button("Show times")


    with ui.footer().style('background-color: #ff9999'):
        with ui.row():
            ui.button('Back To Times', on_click=ui.navigate.back)

@ui.page('/Booking and Availability Cardiologist')
def booking():
    with ui.header(elevated=True).style('background-color: #ff9999').classes('items-center justify-between'):
        ui.label('View Cardiologist Booking and Availability')
    with ui.footer().style('background-color: #ff9999'):
        with ui.row():
            ui.button('Back To Hompage', on_click=ui.navigate.back)

@ui.page('/Booking and Availability Dermatologist')
def booking():
    with ui.header(elevated=True).style('background-color: #ff9999').classes('items-center justify-between'):
        ui.label('View Dermatologist Booking and Availability')
    with ui.footer().style('background-color: #ff9999'):
        with ui.row():
            ui.button('Back To Hompage', on_click=ui.navigate.back)

@ui.page('/Booking and Availability Pediatrician')
def booking():
    with ui.header(elevated=True).style('background-color: #ff9999').classes('items-center justify-between'):
        ui.label('View Pediatrician Booking and Availability')
    with ui.footer().style('background-color: #ff9999'):
        with ui.row():
            ui.button('Back To Hompage', on_click=ui.navigate.back)

specialties = [
    'Cardiologist',
    'Dermatologist',
    'Family Doctor',
    'Pediatrician'
]

with ui.tab_panels(tabs, value = contact).classes("w-full"):
    with ui.tab_panel(contact):
        with ui.expansion('Family Doctor', icon='medication').classes('w-full'):
            with ui.card().tight().style('width: 200px;'):
                ui.image(source="familydoc.jpg")
            with ui.dialog() as dialog, ui.card():
                ui.label('Book an Appointment with a Family Doctor:')
                ui.button('Call', icon='phone')
                ui.button('Book online', icon = 'laptop', on_click = lambda: ui.navigate.to('/Booking and Availability Family Doctor'))
                ui.button('Close', on_click=dialog.close)
            ui.button("Book Now", on_click=dialog.open)
        with ui.expansion('Cardiologist', icon='favorite').classes('w-full'):
            with ui.card().tight().style('width: 200px;'):
                ui.image(source="cardio.png")
            with ui.dialog() as dialog, ui.card():
                ui.label('Book an Appointment with a Cardiologist:')
                ui.button('Call', icon='phone')
                ui.button('Book online', icon = 'laptop', on_click = lambda: ui.navigate.to('/Booking and Availability Family Doctor'))
                ui.button('Close', on_click=dialog.close)
            ui.button("Book Now", on_click=dialog.open)   
        with ui.expansion('Dermatologist', icon='face').classes('w-full'):
            with ui.card().tight().style('width: 200px;'):
                ui.image(source="derma.png")
            with ui.dialog() as dialog, ui.card():
                ui.label('Book an Appointment with a Dermatologist:')
                ui.button('Call', icon='phone' )
                ui.button('Book online', icon = 'laptop', on_click = lambda: ui.navigate.to('/Booking and Availability Family Doctor'))
                ui.button('Close', on_click=dialog.close)
            ui.button("Book Now", on_click=dialog.open)
        with ui.expansion('Pediatrician', icon='medication').classes('w-full'):
            with ui.card().tight().style('width: 200px;'):
                ui.image(source="pedia.png")
            with ui.dialog() as dialog, ui.card():
                ui.label('Book an Appointment with a Pediatrician :')
                ui.button('Call', icon='phone')
                ui.button('Book online', icon = 'laptop', on_click = lambda: ui.navigate.to('/Booking and Availability Family Doctor'))
                ui.button('Close', on_click=dialog.close)
            ui.button("Book Now", on_click=dialog.open)
         
        
with ui.tab_panels(tabs, value = home).classes("w-full"):
    with ui.tab_panel(home):
        greeting = ui.label("Hello!").style('font-size: 24px; font-weight: bold;')
        user_id = ''
        def greet_user(name):
            greeting.set_text(f"Hello!")
            user_id.append(name)

        ui.input(placeholder="Enter your Patient ID", on_change=lambda e: greet_user(e.value))



ui.run(host="127.0.0.1", port=8003 )