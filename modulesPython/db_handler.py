import sqlite3

class DbSingleton():
    instance = None
    db_connection = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance =  super(DbSingleton, cls).__new__(cls)
        print(cls.instance)
        return cls.instance

    def __init__(self, db_name):
        if not self.db_connection:
            self.db_connection = sqlite3.connect(db_name)

mi_db = DbSingleton('PrimeraBase')
dos_database= DbSingleton('SegundaBase')
print(mi_db.db_connection)
print(dos_database.db_connection)

