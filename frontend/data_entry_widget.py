from configparser import NoOptionError
import tkinter
from tkinter import ttk
from tkinter import messagebox
from typing import Any
from tkcalendar import DateEntry
from datetime import datetime
import pytz
import uuid

from database_accesor import Database
from milk_ui import Milk
from vaccination_ui import Vaccination
from master_ui import Master

_TABLES = ["VaccinationDB", "Birth", "AnimalDB", "MasterDB", "MilkDB"]
DBNAME = "DarkSister.db"
# Default values the primary keys
class DataEntryWidget:
    def __init__(self):
        self.table = None

        #Grouped
        self.master = Master()
        self.vaccination = Vaccination()
        self.milk = Milk()

        # Birth
        self.birth_id = None
        self.female_id = None
        self.male_id = None
        self.offspring_id = None
        self.pregnancy_count = None
        self.count_from_couple = None
        self.date_of_delivery = None

    def select_table(self) -> None:
        table = self.table.get()
        if table == "MasterDB":
            self.master.open_master_db_entry_window()

        elif table == "VaccinationDB":
            self.vaccination.open_vaccination_db_entry_window()

        elif table == "MilkDB":
            self.milk.open_milk_production_db_window()

        
        
    def open_table_selection_window(self) -> None:
        #Test code
        db = Database(DBNAME)
        with db:
            db.delete_table("MasterDB")
            db.delete_table("VaccinationDB")
            db.delete_table("MilkDB")
            db.create_master_table()
            db.create_vaccination_table()
            db.create_milk_production_table()
        #Delete code above this point

        window = tkinter.Tk()
        window.resizable()
        window.title("Entry Selection Form")

        frame = tkinter.Frame(window)
        frame.pack()

        table_selection_frame =tkinter.LabelFrame(frame, text="Select Table")
        table_selection_frame.grid(row=0, column=0, padx=21, pady=10)

        table_label = tkinter.Label(table_selection_frame, text="Table")
        self.table = ttk.Combobox(table_selection_frame, values=_TABLES)
        table_label.grid(row=0, column=1)
        self.table.grid(row=1, column=1)

        # Button
        button = tkinter.Button(frame, text="Enter Data", command=self.select_table)
        button.grid(row=2, column=0, sticky="news", padx=20, pady=10)
        
        window.mainloop()

    def open_birth_db_entry_window(self) -> None:
        ...
