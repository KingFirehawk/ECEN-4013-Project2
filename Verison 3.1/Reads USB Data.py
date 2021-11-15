import time

import numpy as np
import pandas as pd
import serial
from numpy.core.numeric import count_nonzero

str1="" # initializers
count = 0
g=0
z=0
str3= ""
ser = serial.Serial('COM3',9600)
headers = np.array ([['Date ',0],['Time ',0],                                       # template 
                        ['Satelliates ',0],['Latitude ',0],['Longitude ',0],['Elivation(m) ',0],
                        ['X_Accel(m/s^2) ',0],['Y_Accel(m/s^2) ',0],['Z_Accel(m/s^2) ',0],
                        ['X_Mag(uT) ',0],['Y_Mag(uT) ',0],['Z_Mag(uT) ',0],
                        ['X_Gyro(rps) ',0],['Y_Gyro(rps) ',0],['Z_Gyro(rps) ',0]])
done = np.array ([['Date        ','Date         ',                                  # template 
                    'Date       ', 'Date     ', 'Date        ', 'Date      ',
                    'Date         ','Date         ','Date           ',
                    'Date           ', 'Date        ','Date       ',
                    'Date        ', 'Date        ','Date         ']])
while(1):
    while(ser.in_waiting != 0):              # waits for serial 
        a=ser.read()                         # read serial
        if(a.decode("utf-8") != "[" and a.decode("utf-8") != "'" and a.decode("utf-8") != "\n" and a.decode("utf-8") != "]"): # not wanted characters 
            str1 +=a.decode("utf-8")         # addes to string if not bad characters
        if(a.decode("utf-8") == " " or a.decode("utf-8") == "]"):   # if ] or " " then we know its a new number
            headers[count,1] = str1          # Add the number got to a array
            count += 1                       # count for a new array spot
            str1=""                          # reset string for new number
        if(a.decode("utf-8") == "q"):        # reset string, q is my new line character
            str1=""                          # reset string for new number
        if(a.decode("utf-8") == "w"):        # w is my end of the line character      
            z=0         
            for i in headers:                # sets i euqal to every spot in the array headers 1 by 1, didnt use i made my own
                str3 = headers[z,1]          # makes it to str for pandas dataframe
                done[0,z] = str3             # adds it to different resized array
                z +=1                        # instead of useing i, i made my own
            df = pd.DataFrame(done, columns = ['Date ','Time ','Satelliates ',      # makes datafram for a easier to read print out
                        'Latitude ','Longitude ','Elivation(m) ','X_Accel(m/s^2) ',
                        'Y_Accel(m/s^2) ','Z_Accel(m/s^2) ','X_Mag(uT) ',
                        'Y_Mag(uT) ','Z_Mag(uT) ','X_Gyro(rps) ',
                        'Y_Gyro(rps) ','Z_Gyro(rps) '])
            print(df)                        # prints dataframe
            print(" ")                       # new line
            count = 0                        # resets count
        g += 1                               # done need anymore
        

