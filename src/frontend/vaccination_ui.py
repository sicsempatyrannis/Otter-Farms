import tkinter
from tkinter import ttk
from tkinter import messagebox
from typing import Any
from tkcalendar import DateEntry
from datetime import datetime
import pytz
import uuid

from backend.database_accesor import Database
DBNAME = "DarkSister.db"
_TABLE_NAME = "VaccinationDB"

class Vaccination:
    def __init__(self) -> None:
        self.vaccination_id = str(uuid.uuid4())
        self.vaccine = None
        self.dosage = None
        self.vaccine_type = None
        self.date_administered = None

    def open_vaccination_db_entry_window(self) -> None:
        window = tkinter.Tk()
        window.resizable()
        window.title("Data Entry Form")

        frame = tkinter.Frame(window)
        frame.pack()

        # Saving Vaccincation information
        vaccination_frame =tkinter.LabelFrame(frame, text="Vaccination Information")
        vaccination_frame.grid(row=0, column=0, padx=21, pady=10)

        vaccine_label = tkinter.Label(vaccination_frame, text="Vaccine")
        vaccine_label.grid(row=0, column=0)
        self.vaccine = tkinter.Entry(vaccination_frame) # Vaccine name entry
        self.vaccine.grid(row=1, column=0)

        dosage_label = tkinter.Label(vaccination_frame, text="Dosage (microL)")
        dosage_label.grid(row=0, column=1)
        self.dosage = tkinter.Entry(vaccination_frame) # Vaccine name entry
        self.dosage.grid(row=1, column=1)

        type_label = tkinter.Label(vaccination_frame, text="Type")
        type_label.grid(row=0, column=2)
        self.vaccine_type = ttk.Combobox(vaccination_frame, values=["Nasal Spray", "Injection", "Oral Suspension"])
        self.vaccine_type.grid(row=1, column=2)

        date_admin_label = tkinter.Label(vaccination_frame, text="Date of Administration")
        sel = tkinter.StringVar() # Allow for string input. Need the screen to update when it is entered.
        self.date_administered = DateEntry(vaccination_frame, selectmode='day', textvariable=sel)
        date_admin_label.grid(row=2, column=0)
        self.date_administered.grid(row=3, column=0)

        # AnimalID
        animal_label = tkinter.Label(vaccination_frame, text="Animal ID")
        animal_label.grid(row=2, column=1)
        self.animal_id = tkinter.Entry(vaccination_frame)
        self.animal_id.grid(row=3, column=1)


        # Button
        button = tkinter.Button(frame, text="Submit", command=self.insert_vaccination_db_record)
        button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

        window.mainloop()

    def insert_vaccination_db_record(self) -> None:
        db = Database(DBNAME)
        record = (self.vaccination_id, self.animal_id.get(), self.vaccine.get(), self.dosage.get(), self.vaccine_type.get(), self.date_administered.get())
        with db:
            db.insert_record(_TABLE_NAME, record)
