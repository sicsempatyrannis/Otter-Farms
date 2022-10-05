from configparser import NoOptionError
import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime
import pytz


_ANIMALS = ["Rabbit", "Sheep", "Cow", "Chicken"]
# Default values the primary keys
class DataEntryWidget:
    def __init__(self):
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

    def submit_data(self):
        tkinter.messagebox.showwarning(title= "Check", message="Please double check all data.")
        
        if accepted=="Accepted":
            # User info
            firstname = first_name_entry.get()
            lastname = last_name_entry.get()
            
            if firstname and lastname:
                title = title_combobox.get()
                age = age_spinbox.get()
                nationality = nationality_combobox.get()
                
                # Course info
                registration_status = reg_status_var.get()
                numcourses = numcourses_spinbox.get()
                numsemesters = numsemesters_spinbox.get()
                
                print("First name: ", firstname, "Last name: ", lastname)
                print("Title: ", title, "Age: ", age, "Nationality: ", nationality)
                print("# Courses: ", numcourses, "# Semesters: ", numsemesters)
                print("Registration status", registration_status)
                print("------------------------------------------")
            else:
                tkinter.messagebox.showwarning(title="Error", message="First name and last name are required.")
        else:
            tkinter.messagebox.showwarning(title= "Error", message="You have not accepted the terms")            


    def open_animal_db_entry_window(self):
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

        self.animal_type = tkinter.Label(animal_id_frame, text="Animal Type")
        self.animal_type_combobox = ttk.Combobox(animal_id_frame, values=_ANIMALS)
        self.animal_type.grid(row=0, column=1)
        self.animal_type_combobox.grid(row=1, column=1)

        gender_label = tkinter.Label(animal_id_frame, text="Gender")
        gender_combobox = ttk.Combobox(animal_id_frame, values=["M", "F"])
        gender_label.grid(row=0, column=2)
        gender_combobox.grid(row=1, column=2)

        dob_label = tkinter.Label(animal_id_frame, text="Date of Birth")
        sel=tkinter.StringVar()
        cal=DateEntry(animal_id_frame, selectmode='day', textvariable=sel)
        dob_label.grid(row=2, column=0)
        cal.grid(row=3, column=0)
        
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


w = DataEntryWidget()
w.open_animal_db_entry_window()