import serial            
import sys                  
# still needs antistop
def convert_to_degrees(rawValue):
    decimalValue = rawValue/100.00
    degrees = int(decimalValue)
    hold = (decimalValue - int(decimalValue))/0.6
    position = degrees + hold
    position = "%.4f" %(position)
    return position

device = (serial.Serial("/dev/ttyS0"))
latitudeInDegrees = 0
longitudeInDegrees = 0
try:
    while True:
        Data = (str)(device.readline())                
        DataAvailable = Data.find("$GPGGA,")                    
        if (DataAvailable>0):
            GPGGAString = Data.split("$GPGGA,",1)[1]
            buffer = (GPGGAString.split(','))
            print("buffer" , buffer)
            try:
                nmea_latitude =  float(buffer[1])               
                nmea_longitude = float(buffer[3]) 
                numStatellites = float(buffer[6]) 
                Elivation = float(buffer[8])
                latitudeInDegrees  = convert_to_degrees(nmea_latitude)    
                longitudeInDegrees = convert_to_degrees(nmea_longitude)  
            except ValueError:
                print("connecting")
            print("lat in degrees:", latitudeInDegrees ," long in degree: ", longitudeInDegrees,
                " Number of Satellites: ", numStatellites ," Elivation: ", Elivation)                         
except KeyboardInterrupt:
    sys.exit(0)