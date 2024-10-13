%include('header.tpl', Title='Index')


<!--# TABLE telephonenumbers
#       (tel_id INTEGER,  nat_nr TEXT, int_nr TEXT, nr_type TEXT, nr_usage TEXT);
# TABLE contact_telephone_mapping
#       (contact_id INTEGER, tel_id INTEGER );
# TABLE contacts
#       (contact_id INTEGER, first_name TEXT, family_name TEXT, family_name_prefix TEXT,
#        birth_name TEXT, birth_name_prefix TEXT, sex TEXT, initials TEXT, adres_id INTEGER);
# TABLE adressen
#       (adres_id INTEGER, straatnaam TEXT, huisnummer INTEGER, huisnummer_toevoeging TEXT,
#        postcode INTEGER, plaatsnaam TEXT);
# TABLE emailadresen
#       (mail_id INTEGER PRIMARY KEY AUTOINCREMENT, emailadres TEXT, email_type TEXT);
# TABLE contact_email_mapping
#       (contact_id INTEGER, mail_id INTEGER);
# TABLE categories
#       (cat_id INTEGER, cat_name TEXT);
# TABLE category_contact_mapping
#       (contact_id INTEGER, cat_id INTEGER);-->

<h2>Enter your name:</h2>
<form action="/submit" method="post">
    Name: <input first_name="first_name" type="text" />
    Name: <input family_name="family_name" type="text" />
    Name: <input family_name_prefix="family_name_prefix" type="text" />
    <input value="Submit" type="submit" />
</form>


%include('footer.tpl')