#8.1

import mysql.connector

def getAirportsNameLocation(Given_code):
    sql = "SELECT ident, name, municipality FROM airports WHERE indent='" + Given_code + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"Airport's name: {row[1]} and it is located in: {row[2]}")
    return

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='PassWord',
         autocommit=True
         )

ICAO_code = input("Enter ICAO code of an aiport: ")
getAirportsNameLocation(ICAO_code)

#8.2

import mysql.connector
def AirportsInArea(Given_code):
    sql = "SELECT type, name, iso_country,  FROM airports WHERE iso_country='" + Given_code + "'ORDER BY type DESC"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"Airport's type: {row[0]} and name: {row[1]}")
    return

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='PassWord',
         autocommit=True
         )

Area_code = input("Enter an area code: ")
AirportsInArea(Area_code)

#8.3

import mysql.connector
from geopy.distance import geodesic

def calculation(Given_code):

    sql = "SELECT ident, latitude_deg, longitude_deg FROM airports WHERE ident='" + Given_code + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            CoordinatesLocation = (row[1],row[2])
            return CoordinatesLocation

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='PassWord',
         autocommit=True
         )

ICAO_code1 = input("Enter the first ICAO code: ")
ICAO_code2 = input("Enter the second ICAO code: ")
Location1 = calculation(ICAO_code1)
Location2 = calculation(ICAO_code2)
DistanceFinal = geodesic(Location1, Location2)
print(f"The distance between airports is: {DistanceFinal} km.")

