import tkinter
from tkinter import ttk
from tkinter import messagebox
from typing import Any
from tkcalendar import DateEntry
from datetime import datetime
import pytz
import uuid

from database_accesor import Database

_TABLE_NAME = "BirthDB"

class Birth:
    def __init__(self):
        # Birth
        self.birth_id = str(uuid.uuid4())
        self.female_name = None
        self.male_name = None
        self.offspring_name = None
        self.date_of_delivery = None
        self.offspring_gender = None

    def open_birth_db_entry_window(self) -> None:
        window = tkinter.Tk()
        window.resizable()
        window.title("Data Entry Form")

        frame = tkinter.Frame(window)
        frame.pack()

        # Saving Animal information
        birth_record_frame =tkinter.LabelFrame(frame, text="Birth Record")
        birth_record_frame.grid(row=0, column=0, padx=21, pady=10)

        male_name_label = tkinter.Label(birth_record_frame, text="Male Name")
        male_name_label.grid(row=0, column=0)
        self.male_name = tkinter.Entry(birth_record_frame) # Name Entry
        self.male_name.grid(row=1, column=0)

        female_name_label = tkinter.Label(birth_record_frame, text="Female Name")
        female_name_label.grid(row=0, column=1)
        self.female_name = tkinter.Entry(birth_record_frame)
        self.female_name.grid(row=1, column=1)

        offspring_name_label = tkinter.Label(birth_record_frame, text="Offspring Name")
        offspring_name_label.grid(row=0, column=2)
        self.offspring_name = tkinter.Entry(birth_record_frame)
        self.offspring_name.grid(row=1, column=2)

        gender_label = tkinter.Label(birth_record_frame, text="Offspring Gender")
        self.offspring_gender = ttk.Combobox(birth_record_frame, values=["M", "F"])
        gender_label.grid(row=2, column=0)
        self.offspring_gender.grid(row=3, column=0)

        dob_label = tkinter.Label(birth_record_frame, text="Date of Birth")
        sel = tkinter.StringVar() # Allow for string input. Need the screen to update when it is entered.
        self.date_of_delivery = DateEntry(birth_record_frame, selectmode='day', textvariable=sel)
        dob_label.grid(row=2, column=1)
        self.date_of_delivery.grid(row=3, column=1)

        # Button
        button = tkinter.Button(frame, text="Submit", command=self.insert_brith_db_record)
        button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

    def insert_brith_db_record(self) -> None:
        db = Database("DarkSister.db")
        record = (self.birth_id, self.female_name.get(), self.male_name.get(), self.offspring_name.get(), self.date_of_delivery.get(), self.offspring_gender.get())
        with db:
            db.insert_record(_TABLE_NAME, record)
