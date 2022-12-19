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


_ANIMALS = ["Rabbit", "Sheep", "Cow", "Chicken"]
_TABLES = ["VaccinationDB", "Birth", "AnimalDB", "MasterDB", "MilkDB"]
DBNAME = "DarkSister.db"
# Default values the primary keys
class DataEntryWidget:
    def __init__(self):
        self.table = None

        # Master
        self.master_id = None
        self.name = None
        self.animal_type = None
        self.gender = None
        self.dob = None
        self.history = None
        self.deleted = None

        # AnimalsDB
        self.animal_id = None
        self.castration_status = None
        self.breed = None
        self.birth_id = None
        

        # Vaccination
        self.vaccination_id = None
        self.vaccine = None
        self.dosage = None
        self.vaccine_type = None
        self.date_administered = None

        # Birth
        self.birth_id = None
        self.female_id = None
        self.male_id = None
        self.offspring_id = None
        self.pregnancy_count = None
        self.count_from_couple = None
        self.date_of_delivery = None

        #Milk
        self.female_id = None
        self.date_of_prod = None
        self.milk_produced = None


        self.db_accessor = None

    def submit_data(self) -> None:
        tkinter.messagebox.showwarning(title= "Check", message="Please double check all data.")
        table = self.table.get()
        if table == "MasterDB":
            self.insert_master_db_record()

        if table == "VaccinationDB":
            self.insert_vaccination_db_record()
            # User info
            # print(self.name.get())
            # print(self.animal_type.get())
            # print(self.gender.get())
            # print(self.dob.get())
            # print(self.history.get("1.0", "end"))

        if table == "MilkDB":
            self.insert_milk_prod_db_record()
            # print(self.female_id.get())
            # print(self.milk_produced.get())
            # print(self.date_of_prod.get())

    def select_table(self) -> None:
        table = self.table.get()
        if table == "MasterDB":
            self.open_master_db_entry_window()

        elif table == "VaccinationDB":
            self.open_vaccination_db_entry_window()

        elif table == "MilkDB":
            self.open_milk_production_db_window()

        
        
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
        self.dob = DateEntry(animal_id_frame, selectmode='day', textvariable=sel)
        dob_label.grid(row=2, column=0)
        self.dob.grid(row=3, column=0)
        
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
        button = tkinter.Button(frame, text="Submit", command=self.submit_data)
        button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
        
        window.mainloop()

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
        button = tkinter.Button(frame, text="Submit", command=self.submit_data)
        button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

        window.mainloop()

    def open_birth_db_entry_window(self) -> None:
        ...

    def open_animal_entry_db_window(self) -> None:
        ...

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
        button = tkinter.Button(frame, text="Submit", command=self.submit_data)
        button.grid(row=3, column=0, sticky="news", padx=20, pady=10)


    def insert_master_db_record(self) -> None:
        table = self.table.get()
        if table != "MasterDB":
            raise RuntimeError(f"Trying to insert record into the wrong table. Trying to insert into {table}, should be MasterDB")

        db = Database(DBNAME)
        dt = datetime.now()
        record = (str(uuid.uuid4()), self.name.get(), self.animal_type.get(), self.gender.get(), self.dob.get(), self.history.get("1.0", "end"), 0, dt)
        with db:
            db.insert_record(table, record)

    def insert_vaccination_db_record(self) -> None:
        table = self.table.get()
        if table != "VaccinationDB":
            raise RuntimeError(f"Trying to insert record into the wrong table. Trying to insert into {table}, should be VaccinationDB")

        db = Database(DBNAME)
        record = (str(uuid.uuid4()), self.animal_id.get(), self.vaccine.get(), self.dosage.get(), self.vaccine_type.get(), self.date_administered.get())
        with db:
            db.insert_record(table, record)

    def insert_milk_prod_db_record(self) -> None:
        table = self.table.get()
        if table != "MilkDB":
            raise RuntimeError(f"Trying to insert record into the wrong table. Trying to insert into {table}, should be MilkDB")

        db = Database(DBNAME)
        record = (str(uuid.uuid4()), self.female_id.get(), self.milk_produced.get(), self.date_of_prod.get())
        with db:
            db.insert_record(table, record)




w = DataEntryWidget()
w.open_table_selection_window()