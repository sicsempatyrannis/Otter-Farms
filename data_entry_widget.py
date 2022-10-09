from configparser import NoOptionError
import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime
import pytz


_ANIMALS = ["Rabbit", "Sheep", "Cow", "Chicken"]
_TABLES = ["Vaccination", "Birth", "AnimalDB", "MasterDB"]
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

    def submit_data(self) -> None:
        tkinter.messagebox.showwarning(title= "Check", message="Please double check all data.")
        
        # User info
        print(self.name.get())
        print(self.animal_type.get())
        print(self.gender.get())
        print(self.dob.get())
        print(self.history.get("1.0", "end"))

    def select_table(self):
        table_func_mapping = {"MasterDB": self.open_master_db_entry_window(), "VaccinationDB": self.open_vaccination_db_entry_window()}

        table_func_mapping[self.table.get()]

        
        
    def open_table_selection_window(self) -> None:
        window = tkinter.Tk()
        window.resizable()
        window.title("Entry Selection Form")

        frame = tkinter.Frame(window)
        frame.pack()

        table_selection_frame =tkinter.LabelFrame(frame, text="Select Table")
        table_selection_frame.grid(row=0, column=0, padx=21, pady=10)

        table_label = tkinter.Label(table_selection_frame, text="Animal Type")
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
        self.gender .grid(row=1, column=2)

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
        ...

    def open_birth_db_entry_window(self) -> None:
        ...

    def open_animal_entry_db_window(self) -> None:
        ...


w = DataEntryWidget()
w.open_table_selection_window()