import tkinter
from tkinter import ttk
from tkinter import messagebox
from typing import Any
from tkcalendar import DateEntry
from datetime import datetime
import pytz
import uuid

from database_accesor import Database
DBNAME = "DarkSister.db"

class Milk:
    def __init__(self) -> None:
        self.table = "MilkDB"
        self.milk_id = str(uuid.uuid4())
        self.female_id = None
        self.date_of_prod = None
        self.milk_produced = None

    def open_milk_production_db_window(self) -> None:
        window = tkinter.Tk()
        window.resizable()
        window.title("Data Entry Form")

        frame = tkinter.Frame(window)
        frame.pack()

        # Saving Milk information
        milk_frame =tkinter.LabelFrame(frame, text="Milk Production Information")
        milk_frame.grid(row=0, column=0, padx=21, pady=10)

        # FemaleID
        female_label = tkinter.Label(milk_frame, text="Female ID")
        female_label.grid(row=0, column=0)
        self.female_id = tkinter.Entry(milk_frame)
        self.female_id.grid(row=1, column=0)

        # Milk produced
        milk_prod_label = tkinter.Label(milk_frame, text="Milk Produced (ml)")
        milk_prod_label.grid(row=0, column=2)
        self.milk_produced = tkinter.Entry(milk_frame)
        self.milk_produced.grid(row=1, column=2)

        # Date label
        date_label = tkinter.Label(milk_frame, text="Date of Milking")
        sel = tkinter.StringVar() # Allow for string input. Need the screen to update when it is entered.
        self.date_of_prod = DateEntry(milk_frame, selectmode='day', textvariable=sel)
        date_label.grid(row=2, column=0)
        self.date_of_prod.grid(row=3, column=0)

        # Button
        button = tkinter.Button(frame, text="Submit", command=self.insert_milk_prod_db_record)
        button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

    def insert_milk_prod_db_record(self) -> None:
        db = Database("DarkSister.db")
        record = (self.milk_id, self.female_id.get(), self.milk_produced.get(), self.date_of_prod.get())
        with db:
            db.insert_record(self.table, record)