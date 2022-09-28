#8.1

import mysql.connector

def getAirportsNameLocation(ICAO_code):
    sql = "SELECT name, municipality, gps_code FROM airport_file WHERE gps_code='" + ICAO_code + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"Airport's name: {row[0]} and it is located in: {row[1]}")
    return

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='airports',
         user='root',
         password='PassWord',
         autocommit=True
         )

ICAO_code = input("Enter ICAO code of an aiport: ")
getAirportsNameLocation(ICAO_code)

#8.2

