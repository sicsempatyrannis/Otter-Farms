import sqlite3
import logging
from datetime import datetime
import pytz
import csv

from typing import Any, Optional

MASTER_TABLE_QUERY = '''
        CREATE TABLE IF NOT EXISTS MasterDB(
            ID TEXT PRIMARY KEY,
            Name TEXT,
            Type TEXT,
            Gender TEXT,
            DateOfBirth INTEGER,
            Hisory TEXT,
            Deleted INTEGER,
            DateAdded TEXT
        )
        '''

class Database:
    def __init__(self, database_name: str) -> None:
        self.database_name = database_name
        self.connection = None

    def __enter__(self):
        conn = sqlite3.connect(self.database_name, isolation_level=None)
        self.connection = conn
        return self

    def __exit__(self, exc_type: BaseException, exc_value: BaseException, exc_tb: BaseException) -> None:
        assert self.connection is not None, "No current open connection to DB"
        self.connection.close()
        self.connection = None

    def _execute_query(self, cursor: sqlite3.Cursor, query: str, parameters: Optional[Any]={}, many: bool=False) -> None:
        if not many:
            cursor.execute(query, parameters)

        else:
            cursor.executemany(query, parameters)
        logging.info("Executing query: %s. With parameters: %s", query, parameters)

    def create_master_table(self) -> None:
        cursor = self.connection.cursor()
        self._execute_query(cursor, MASTER_TABLE_QUERY)

    def create_animal_tables(self, animals_and_breeds: dict[str, list]):
        query = ""

        for animal, _ in animals_and_breeds.items():
            query = f'''
                CREATE TABLE IF NOT EXISTS {animal}DB(
                    {animal}ID INTEGER,
                    CastrationStatus INTEGER,
                    Breed TEXT,
                    BirthRecordID INTEGER,

                    FOREIGN KEY({animal}ID) REFERENCES MasterDB(ID),
                    FOREIGN KEY(BirthRecordID) REFERENCES BirthDB(BirthID),
                    )
                    '''


            cursor = self.connection.cursor()
            self._execute_query(cursor, query)

    def create_vaccination_table(self):
        # Need to remember to convert the dosage into a standard unit
        # likely will be microL or microG will likely be implemented on the frontend through the UI

        # Type refers to method of administration injected, nasal spray
        query = """
            CREATE TABLE IF NOT EXISTS VaccinationDB(
                VaccinationID INTEGER PRIMAYR KEY,
                AnimalID INTEGER,
                Vaccine TEXT,
                Dosage INT,
                Type TEXT,
                Date TEXT,

                FOREIGN KEY(VaccinationID) REFERENCES MasterDB(ID)
                )
                """

        cursor = self.connection.cursor()
        self._execute_query(cursor, query)


    # Initialise these values to zero so birth count and pairings count can be done automatically in backend.
    # Inlcude a female or male value for an external animal, like a way to record for them in birth records.
    def create_birth_record_table(self):
        query = """
            CREATE IF NOT EXISTS BirthDB(
                BirthID INTEGER PRIMAYR KEY,
                FemaleID INTEGER,
                MaleID INTEGER,
                OffSpringID INTEGER,
                PregnancyCount INTEGER,
                CountFromCouple INTEGER,
                DateOfDelivery TEXT

                FOREIGN KEY(FemaleID) REFERENCES MasterDB(ID)
                FOREIGN KEY(MaleID) REFERENCES MasterDB(ID)
                FOREIGN KEY(OffSpringID) REFERENCES MasterDB(ID)
                """

        cursor = self.connection.cursor()
        self._execute_query(cursor, query)

    # Convert milk produced into 
    def create_milk_production_table(self):
        query  = """
            CREATE TABLE IF NOT EXISTS MilkDB(
                MilkID INTEGER PRIMAYR KEY,
                FemaleID TEXT,
                MilkProduced INTEGER,
                Date TEXT,
                
                FOREIGN KEY(FemaleID) REFERENCES MasterDB(ID)
                )
                """

        cursor = self.connection.cursor()
        self._execute_query(cursor, query)

    def _get_column_names(self, table: str) -> tuple[str, int]:
        select_query = f"SELECT * FROM {table}"
        cursor = self.connection.cursor()
        self._execute_query(cursor, select_query)
        column_name = tuple(map(lambda x: x[0], cursor.description))
        str_column_names = str(column_name).replace("'", "")

        return str_column_names, len(column_name)

    def bulk_insert_records(self, csv_file_path: str, table: str) -> None:
        file = open(csv_file_path)
        records = csv.reader(file)
        num_of_records = len(list(csv.reader(open(csv_file_path))))
        
        logging.info(f"Inserting {num_of_records} records")

        #Return column headers of the table you're about to insert into
        column_names, number_of_columns = self._get_column_names(table)
        q_tuple = str(tuple("?"*number_of_columns)).replace("'", "")
        
        query = f"INSERT INTO {table} {str(column_names)} VALUES {q_tuple}"
        cursor = self.connection.cursor()
        self._execute_query(cursor, query, parameters=records, many=True)

    def insert_record(self, table: str, record: tuple[Any]) -> None:
        logging.info(f"Inserting a record. Table: {table} /nRecord: {record}")
    
        column_names, no_of_cols = self._get_column_names(table)
        q_tuple = str(tuple("?"*no_of_cols)).replace("'", "")

        query = f"INSERT INTO {table} {str(column_names)} VALUES {q_tuple}"
        cursor = self.connection.cursor()
        self._execute_query(cursor, query=query, parameters=record)

    # For testing
    def delete_table(self, table):
        query = f"DROP TABLE IF EXISTS {table}"
        cursor = self.connection.cursor()
        self._execute_query(cursor, query)

    # For testing
    def print_records(self, table):
        query = f"SELECT * FROM {table}"
        cursor = self.connection.cursor()
        records = cursor.execute(query).fetchall()

        print(records)

