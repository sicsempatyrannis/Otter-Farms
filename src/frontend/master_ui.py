import tkinter
from tkinter import ttk
from tkinter import messagebox
from typing import Any
from tkcalendar import DateEntry
from datetime import datetime
import pytz
import uuid

from backend.database_accesor import Database, DBNAME

_ANIMALS = ["Rabbit", "Sheep", "Cow", "Chicken"]
_TABLE_NAME = "MasterDB"
class Master:
    def __init__(self) -> None:
        self.master_id = str(uuid.uuid4())
        self.name = None
        self.animal_type = None
        self.gender = None
        self.date_of_birth = None
        self.history = None
        self.deleted = None

    def open_master_db_entry_window(self) -> None:
        window = tkinter.Tk()
        window.resizable()
        window.title("Data Entry Form")

        frame = tkinter.Frame(window)
        frame.pack()

        # Saving Animal information
        animal_id_frame =tkinter.LabelFrame(frame, text="Animal Information")
        animal_id_frame.grid(row=0, column=0, padx=21, pady=10)

        name_label = tkinter.Label(animal_id_frame, text="Name")
        name_label.grid(row=0, column=0)
        self.name = tkinter.Entry(animal_id_frame) # Name Entry
        self.name.grid(row=1, column=0)

        animal_type_label = tkinter.Label(animal_id_frame, text="Animal Type")
        self.animal_type = ttk.Combobox(animal_id_frame, values=_ANIMALS)
        animal_type_label.grid(row=0, column=1)
        self.animal_type.grid(row=1, column=1)

        gender_label = tkinter.Label(animal_id_frame, text="Gender")
        self.gender = ttk.Combobox(animal_id_frame, values=["M", "F"])
        gender_label.grid(row=0, column=2)
        self.gender.grid(row=1, column=2)

        dob_label = tkinter.Label(animal_id_frame, text="Date of Birth")
        sel = tkinter.StringVar() # Allow for string input. Need the screen to update when it is entered.
        self.date_of_birth = DateEntry(animal_id_frame, selectmode='day', textvariable=sel)
        dob_label.grid(row=2, column=0)
        self.date_of_birth.grid(row=3, column=0)
        
        history_label = tkinter.Label(animal_id_frame, text="History")
        self.history = tkinter.Text(animal_id_frame, width=20, height=4)
        self.history.grid(row=3, column=1)
        history_label.grid(row=2, column=1)

        date_added_label = tkinter.Label(animal_id_frame, text="Date and Time of Entry")
        tz = pytz.timezone("Africa/Kampala")
        dt = datetime.now(tz=tz)

        autofilled_date = tkinter.Label(animal_id_frame, text=dt.strftime("%m/%d/%Y %H:%M:%S"))
        date_added_label.grid(row=2, column=2)
        autofilled_date.grid(row=3, column=2)
        


        for widget in animal_id_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        # Button
        button = tkinter.Button(frame, text="Submit", command=self.insert_master_db_record)
        button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
        
        window.mainloop()

    def insert_master_db_record(self) -> None:
        db = Database(DBNAME)
        dt = datetime.now()
        record = (self.master_id, self.name.get(), self.animal_type.get(), self.gender.get(), self.date_of_birth.get(), self.history.get("1.0", "end"), 0, dt)
        with db:
            db.insert_record(_TABLE_NAME, record)
