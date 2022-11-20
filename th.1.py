import mysql.connector

def koodilla(ident):
    sql = 'SELECT name, municipality FROM airport'
    sql += " WHERE ident='"+ident+"';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0:
        for rivi in tulos:
            print(f'Lentoasema {rivi[0]} sijaitsee kunnassa {rivi[1]}.')
    return

yhteys = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = '0095',
    autocommit = True
)

ident = input('Anna lentoaseman ICAO-koodi: ')

koodilla(ident)