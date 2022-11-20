import mysql.connector

def synkataan(maakoodi):
    sql = f'''SELECT airport.type, count(*)
    from airport
    where airport.iso_country = "{maakoodi}"
    group by type;'''
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulo = kursori.fetchall()
    if kursori.rowcount >0:
        print(f'Maan lentokenttatyypit: \n'
              f'Suljettuja: {tulo[0][1]}\n'
              f'Heliportteja: {tulo[1][1]}\n'
              f'Suuret lentokentat: {tulo[2][1]}\n'
              f'Keskikokoiset lentokentat: {tulo[3][1]}\n'
              f'Pienet lentokentat: {tulo[4][1]}')


yhteys = mysql.connector.connect(
    host= 'localhost',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = '0095',
    autocommit = True
)

maakoodi = input('Anna maakoodi: ')
synkataan(maakoodi.upper())