import sqlite3

def populate_tables(dbfile):
    sql_statements = [
         """INSERT INTO contacts (first_name,family_name,adres_id) 
             VALUES ("John", "Doe", 1 );""",
         """INSERT INTO adressen (straatnaam,huisnummer,postcode,plaatsnaam) 
             VALUES ("laantje", 2, 1234, "Jipsinboermussel");""",
        """INSERT INTO contacts (first_name,family_name,adres_id) 
            VALUES ("James", "Doe", 1 );"""
    ]
    #"INSERT INTO telephonenumbers (nat_nr,int_nr,nr_type) VALUES ()"
    #"INSERT INTO contact_telephone_mapping (tel_id,status) VALUES ()"
    try:
        with sqlite3.connect(dbfile) as conn:
            cursor = conn.cursor()
            for statement in sql_statements:
                cursor.execute(statement)

            conn.commit()
    except sqlite3.Error as e:
        print(e)


if __name__ == '__main__':
    populate_tables("my.db")