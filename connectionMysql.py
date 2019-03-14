import mysql.connector
import serial
import time
serial = serial.Serial('COM4', baudrate = 9600, timeout = 10)
#print "s"
while True:
    con = mysql.connector.connect(
    user = "root",
    password = "",
    host = "localhost",
    database = "db_traffic") or die ("Gagal menyambunbgkan kedatabase")

    m = con.cursor()
    q = "SELECT * FROM informasi ORDER by id DESC LIMIT 1"
    m.execute(q)

    rez = m.fetchall()
    
    for el in rez:
        data = el[1]+"|"+el[2]+"|"+el[3]
        print data
        
    serial.write(bytes(data))  
    try:
        
        a = serial.readline()
        print (a)
        con.close()
        time.sleep(2)
    except:
        print "Gagal"    
