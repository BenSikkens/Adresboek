import sqlite3

def create_sqlite_database(filename):
    """ create a database connection to an SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(filename)
        print(sqlite3.sqlite_version)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def create_tables(dbfile):
    sql_statements = [
        """CREATE TABLE IF NOT EXISTS telephonenumbers
             (tel_id INTEGER PRIMARY KEY AUTOINCREMENT,
              nat_nr TEXT NOT NULL,
              int_nr TEXT NOT NULL,
              nr_type TEXT,
              nr_usage TEXT
        );""",
        """CREATE TABLE IF NOT EXISTS contacts
            (contact_id INTEGER PRIMARY KEY AUTOINCREMENT, 
             first_name TEXT,
             family_name TEXT,
             family_name_prefix TEXT,
             birth_name TEXT,
             birth_name_prefix TEXT,
             sex TEXT,
             initials TEXT,
             adres_id INTEGER
        );""",
        """CREATE TABLE adressen
            (adres_id INTEGER PRIMARY KEY AUTOINCREMENT,
            straatnaam TEXT,
            huisnummer INTEGER,
            huisnummer_toevoeging TEXT,
            postcode INTEGER,
            plaatsnaam TEXT
        );""",
        """CREATE TABLE emailadresen
            (mail_id INTEGER PRIMARY KEY AUTOINCREMENT,
            emailadres TEXT,
            email_type TEXT
        );""",
        """CREATE TABLE categories
            (cat_id INTEGER PRIMARY KEY AUTOINCREMENT,
            cat_name TEXT NOT NULL
        );""",
        """CREATE TABLE contact_telephone_mapping
            (contact_id INTEGER,
            tel_id INTEGER,
            FOREIGN KEY(contact_id) REFERENCES contacts(contact_id)
            FOREIGN KEY(tel_id) REFERENCES telephonenumbers(tel_id)
            PRIMARY KEY(contact_id, tel_id)
        );""",
        """CREATE TABLE contact_email_mapping
            (contact_id INTEGER,
            mail_id INTEGER,
            FOREIGN KEY(contact_id) REFERENCES contacts(contact_id)
            FOREIGN KEY(mail_id) REFERENCES emailadressen(mail_id)
            PRIMARY KEY(contact_id, mail_id)
        );""",
        """CREATE TABLE category_contact_mapping
            (contact_id INTEGER,
            cat_id INTEGER,
            FOREIGN KEY(contact_id) REFERENCES contacts(contact_id)
            FOREIGN KEY(cat_id) REFERENCES categories(cat_id)
            PRIMARY KEY(contact_id, cat_id)
        );"""]

    # create a database connection
    try:
        with sqlite3.connect(dbfile) as conn:
            cursor = conn.cursor()
            for statement in sql_statements:
                cursor.execute(statement)

            conn.commit()
    except sqlite3.Error as e:
        print(e)



if __name__ == '__main__':
    create_sqlite_database("my.db")
    create_tables("my.db")