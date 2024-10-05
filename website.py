from nicegui import ui
import pandas as pd

with ui.tabs().classes("w-full") as tabs:
    home = ui.tab("Home")
    about = ui.tab("About")
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

@ui.page('/Booking and Availability')
def booking():
    with ui.header(elevated=True).style('background-color: #ff9999').classes('items-center justify-between'):
        ui.label('View Doctor Booking and Availability')
    with ui.footer().style('background-color: #ff9999'):
        with ui.row():
            ui.button('Back To Hompage', on_click=ui.navigate.back)

specialties = [
    'Cardiologist',
    'Family Doctor',
    'Dermatologist',
    'Oncologist',
    'Pediatrician',
    'Psychiatrist',
    'Gynaecologist',
    'Anesthesiologist'
]

with ui.tab_panels(tabs, value = contact).classes("w-full"):
    with ui.tab_panel(contact):
        with ui.expansion('Family Doctor', icon='medication').classes('w-full'):
            with ui.card().tight().style('width: 200px;'):
                ui.image(source="DSC00017.jpg")
            with ui.dialog() as dialog, ui.card():
                ui.label('Book an Appointment with Doctor Tantan:')
                ui.button('Call', icon='phone')
                ui.button('Book online', icon = 'laptop', on_click = lambda: ui.navigate.to('/Booking and Availability'))
                ui.button('Close', on_click=dialog.close)
            ui.button("Doctor Tantan", on_click=dialog.open)
        with ui.expansion('Cardiologist', icon='favorite').classes('w-full'):
            with ui.card().tight().style('width: 200px;'):
                ui.image(source="DSC00017.jpg")
            with ui.dialog() as dialog, ui.card():
                ui.label('Book an Appointment with Doctor Tantan:')
                ui.button('Call', icon='phone')
                ui.button('Book online', icon = 'laptop', on_click = lambda: ui.navigate.to('/Booking and Availability'))
                ui.button('Close', on_click=dialog.close)
            ui.button("Doctor Tantan", on_click=dialog.open)
        with ui.expansion('Dermatologist', icon='face').classes('w-full'):
            with ui.card().tight().style('width: 200px;'):
                ui.image(source="DSC00017.jpg")
            with ui.dialog() as dialog, ui.card():
                ui.label('Book an Appointment with Doctor Tantan:')
                ui.button('Call', icon='phone' )
                ui.button('Book online', icon = 'laptop', on_click = lambda: ui.navigate.to('/Booking and Availability'))
                ui.button('Close', on_click=dialog.close)
            ui.button("Doctor Tantan", on_click=dialog.open)
        with ui.expansion('Oncologist', icon='favorite').classes('w-full'):
            with ui.card().tight().style('width: 200px;'):
                ui.image(source="DSC00017.jpg")
            with ui.dialog() as dialog, ui.card():
                ui.label('Book an Appointment with Doctor Tantan:')
                ui.button('Call', icon='phone')
                ui.button('Book online', icon = 'laptop', on_click = lambda: ui.navigate.to('/Booking and Availability'))
                ui.button('Close', on_click=dialog.close)
            ui.button("Doctor Tantan", on_click=dialog.open)
        with ui.expansion('Pediatrician', icon='medication').classes('w-full'):
            with ui.card().tight().style('width: 200px;'):
                ui.image(source="DSC00017.jpg")
            with ui.dialog() as dialog, ui.card():
                ui.label('Book an Appointment with Doctor Tantan:')
                ui.button('Call', icon='phone')
                ui.button('Book online', icon = 'laptop', on_click = lambda: ui.navigate.to('/Booking and Availability'))
                ui.button('Close', on_click=dialog.close)
            ui.button("Doctor Tantan", on_click=dialog.open)
        with ui.expansion('Pyschiatrist', icon='face').classes('w-full'):
            with ui.card().tight().style('width: 200px;'):
                ui.image(source="DSC00017.jpg")
            with ui.dialog() as dialog, ui.card():
                ui.label('Book an Appointment with Doctor Tantan:')
                ui.button('Call', icon='phone')
                ui.button('Book online', icon = 'laptop', on_click = lambda: ui.navigate.to('/Booking and Availability'))
                ui.button('Close', on_click=dialog.close)
            ui.button("Doctor Tantan", on_click=dialog.open)
        with ui.expansion('Gynaecologist', icon='favorite').classes('w-full'):
            with ui.card().tight().style('width: 200px;'):
                ui.image(source="DSC00017.jpg")
            with ui.dialog() as dialog, ui.card():
                ui.label('Book an Appointment with Doctor Tantan:')
                ui.button('Call', icon='phone')
                ui.button('Book online', icon = 'laptop', on_click = lambda: ui.navigate.to('/Booking and Availability'))
                ui.button('Close', on_click=dialog.close)
            ui.button("Doctor Tantan", on_click=dialog.open)
        with ui.expansion('Anesthesiologist', icon='vaccines').classes('w-full'):
            with ui.card().tight().style('width: 200px;'):
                ui.image(source="DSC00017.jpg")
            with ui.dialog() as dialog, ui.card():
                ui.label('Book an Appointment with Doctor Tantan:')
                ui.button('Call', icon='phone')
                ui.button('Book online', icon = 'laptop', on_click = lambda: ui.navigate.to('/Booking and Availability'))
                ui.button('Close', on_click=dialog.close)
            ui.button("Doctor Tantan", on_click=dialog.open)

with ui.tab_panels(tabs, value = home).classes("w-full"):
    with ui.tab_panel(home):
        greeting = ui.label("Hello!").style('font-size: 24px; font-weight: bold;')

        def greet_user(name):
            greeting.set_text(f"Hello, {name}!")

        ui.input(placeholder="Enter your name", on_change=lambda e: greet_user(e.value))

        with ui.column().style('align-items: center; justify-content: center; min-height: 0vh;'):  # Vertically and horizontally center
            with ui.row().style('display: flex; justify-content: center; width: fit-content; gap: 40px;'):  # Center row and add gap
                with ui.card().tight().style('width: 200px;'):
                    ui.image(source="DSC00017.jpg")
                    with ui.card_actions():
                        ui.button("Go to Home", on_click=lambda: tabs.set_value("Home"))

                with ui.card().tight().style('width: 200px;'):
                    with ui.card_actions():
                        ui.button("Go to About", on_click=lambda: tabs.set_value("About"))

                with ui.card().tight().style('width: 200px;'):
                    with ui.card_actions():
                        ui.button("Go to Contact", on_click=lambda: tabs.set_value("Contact"))

                with ui.card().tight().style('width: 200px;'):
                    with ui.card_actions():
                        ui.button("Go to Settings", on_click=lambda: tabs.set_value("Settings"))



ui.run(host="127.0.0.1", port=8003)