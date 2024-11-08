import sqlite3

from bottle import route, run, template, request, static_file  # , request, debug

# ---------------------------------------------------------------------------------------------------
# Structure of the Database (for referencing)
# ---------------------------------------------------------------------------------------------------
# TABLE telephonenumbers
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
#       (contact_id INTEGER, cat_id INTEGER);

# vars voor de routes




# voor de css
@route('/css/<filename>')
def send_css(filename):
    print('getting css')
    return static_file(filename, root='views/static/css')

# voor static files
@route('/static/<filename>')
def server_static(filename):
    print(f'getting static file {filename}')
    return static_file(filename, root='./views/static')

# get alle adressen
@route('/adressen')
def get_adressen():
    name="Ben's adresboek"
    routes = ["/index", "/adressen", "/new/contact"]
    print('get all addresses')
    conn = sqlite3.connect('my.db')
    c = conn.cursor()
    c.execute("SELECT c.first_name, c.family_name_prefix, c.family_name, c.contact_id, "
              "a.straatnaam, a.huisnummer, a.postcode, a.plaatsnaam "
              "FROM contacts c, adressen a where a.adres_id = c.adres_id ")
    data = c.fetchall()
    nawdata = list()
    for row in data:
        if row[1] is None:
            pfx = ''
        else:
            pfx = row[1]
        nawgegs = dict(id=row[3], voornaam=row[0], prefix=pfx, achternaam=row[2], straatnaam=row[4], huisnummer=row[5],
                       postcode=row[6], plaatsnaam=row[7])
        nawdata.append(nawgegs)
    print(nawdata)
    c.close()
    output = template('adreslijst', nawdata=nawdata, name=name, routes=routes)
    print(data)
    return output

# get specifiek adres
@route('/adres/<name:re:[a-zA-Z]+>')
def get_address(name):
    print(f'get address of name starting with {name}')
    conn = sqlite3.connect('my.db')
    c = conn.cursor()
    name = name + '%'
    c.execute("SELECT c.first_name, c.family_name_prefix, c.family_name, c.contact_id, "
              "a.straatnaam, a.huisnummer, a.postcode, a.plaatsnaam "
              "FROM contacts c, adressen a WHERE a.adres_id = c.adres_id AND" 
              " c.first_name LIKE ?", (name,))
    data = c.fetchall()
    nawdata = list()
    for row in data:
        if row[1] is None:
            pfx = ''
        else:
            pfx = row[1]
        nawgegs = dict(id=row[3], voornaam=row[0], prefix=pfx, achternaam=row[2], straatnaam=row[4], huisnummer=row[5],
                       postcode=row[6], plaatsnaam=row[7])
        print("id={nawgegs.voornaam} ")
        nawdata.append(nawgegs)
    print(nawdata)
    c.close()
    output = template('adreslijst', nawdata=nawdata)
    #output = template('index.tpl', name=name)
    print(data)
    return output

@route('/new/contact')
def form():
    print('enter form')
    routes = ["/index", "/adressen", "/new/contact"]
    return template('form', routes=routes)


# Route to handle form submission and insert data into the database
@route('/submit', method='POST')
def submit():
    print(f'submitting form with {request.forms.keys()}')

    first_name = request.forms.get('first_name')
    print(f'{first_name}')
    family_name = request.forms.get('family_name')
    family_name_prefix = request.forms.get('family_name_prefix')


    print(f'{first_name} {family_name_prefix} {family_name} ')
    if first_name and family_name :
        family_name_prefix = family_name_prefix if family_name_prefix else None

        conn = sqlite3.connect('my.db')
        c = conn.cursor()
        c.execute('INSERT INTO contacts (first_name, family_name, family_name_prefix) VALUES (?, ?, ?)', (first_name, family_name, family_name_prefix))
        c.close()
        conn.commit()
        conn.close()


        return f"Inserted name: {first_name}"
    else:
        return "Name cannot be empty!"

@route('/verhuizen/<>', method='GET')
def verhuizen():
    #get the adres_id from the person who is moving (thus corresponding to the old address)
    #get the new address from adressen.
    #if the new address does not exist create it.
    #update the adres_id of the person moving (die verhuist (in Dutch))
    #(optional) delete the old adres_id from adressen
    pass

@route('add_email/<>')
def add_email():
    pass

@route('/index')
@route('/')
def index():
    name="Ben's adresboek"
    routes = ["/index", "/adressen", "/new/contact"]
    return template('index.tpl', name=name, routes=routes)

routes = ["/index", "/adressen", "/new/contact"]
run(host='localhost', port=8080, debug=True, reloader=True)
