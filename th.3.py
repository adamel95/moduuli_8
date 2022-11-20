import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
    host ='localhost',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = '0095',
    autocommit = True
)

def getAirportPos(yhteys, ICAO):
    kursori = yhteys.cursor()
    kursori.execute(f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident='{ICAO}';")
    return kursori.fetchone()

kentta1=getAirportPos(yhteys, input('Anna ensimmäisen lentokentän ICAO koodi: ').upper())
kentta2=getAirportPos(yhteys, input('Anna toisen lentokentän ICAO koodi: ').upper())
print(f'Kentät ovat {float(distance.distance(kentta1, kentta2).km):.1f} kilometrin päässä toisistaan')
