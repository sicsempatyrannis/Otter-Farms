import sys
from sys import path
import os

parent_path = os.getcwd()

path.append(parent_path + "\\frontend")
path.append(parent_path + "\\backend")

from data_entry_widget import DataEntryWidget


if __name__ == "__main__":
    
    w = DataEntryWidget()
    w.open_table_selection_window()