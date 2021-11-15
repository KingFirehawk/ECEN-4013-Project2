import time

import numpy as np
import pandas as pd
import serial
from numpy.core.numeric import count_nonzero

str1=""
count = 0
g=0
z=0
str3= ""
ser = serial.Serial('COM3',9600)
headers = np.array ([['Date ',0],['Time ',0],
                        ['Satelliates ',0],['Latitude ',0],['Longitude ',0],['Elivation(m) ',0],
                        ['X_Accel(m/s^2) ',0],['Y_Accel(m/s^2) ',0],['Z_Accel(m/s^2) ',0],
                        ['X_Mag(uT) ',0],['Y_Mag(uT) ',0],['Z_Mag(uT) ',0],
                        ['X_Gyro(rps) ',0],['Y_Gyro(rps) ',0],['Z_Gyro(rps) ',0]])
done = np.array ([['Date        ','Date         ',
                    'Date       ', 'Date     ', 'Date        ', 'Date      ',
                    'Date         ','Date         ','Date           ',
                    'Date           ', 'Date        ','Date       ',
                    'Date        ', 'Date        ','Date         ']])
while(1):
    while(ser.in_waiting != 0):
        a=ser.read()
        if(a.decode("utf-8") != "[" and a.decode("utf-8") != "'" and a.decode("utf-8") != "\n" and a.decode("utf-8") != "]"):
            str1 +=a.decode("utf-8")
        if(a.decode("utf-8") == " " or a.decode("utf-8") == "]"):
            headers[count,1] = str1
            count += 1 
            str1=""
        if(a.decode("utf-8") == "q"):
            str1=""
        if(a.decode("utf-8") == "w"):
            z=0
            for i in headers:
                str3 = headers[z,1]
                done[0,z] = str3
                z +=1
            df = pd.DataFrame(done, columns = ['Date ','Time ','Satelliates ',
                        'Latitude ','Longitude ','Elivation(m) ','X_Accel(m/s^2) ',
                        'Y_Accel(m/s^2) ','Z_Accel(m/s^2) ','X_Mag(uT) ',
                        'Y_Mag(uT) ','Z_Mag(uT) ','X_Gyro(rps) ',
                        'Y_Gyro(rps) ','Z_Gyro(rps) '])
            print(df)
            print(" ")
            count = 0
        g += 1
        

