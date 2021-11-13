import smbus,time

def MPU6050_start():
    samp_rate_div = 0 
    bus.write_byte_data(MPU6050_ADDR, SMPLRT_DIV, samp_rate_div)
    time.sleep(0.1)
    bus.write_byte_data(MPU6050_ADDR,PWR_MGMT_1,0x00)
    time.sleep(0.1)
    bus.write_byte_data(MPU6050_ADDR, PWR_MGMT_1, 0x01)
    time.sleep(0.1)
    bus.write_byte_data(MPU6050_ADDR, Config , 0)
    time.sleep(0.1)
    gyro_config_sel = [0b00000,0b010000,0b10000,0b11000] 
    gyro_config_vals = [250.0,500.0,1000.0,2000.0] 
    gyro_indx = 0
    bus.write_byte_data(MPU6050_ADDR, GyroConfig , int(gyro_config_sel[gyro_indx]))
    time.sleep(0.1)
    accel_config_sel = [0b00000,0b01000,0b10000,0b11000] 
    accel_config_vals = [2.0,4.0,8.0,16.0] 
    accel_indx = 0                            
    bus.write_byte_data(MPU6050_ADDR, AccelConfig, int(accel_config_sel[accel_indx]))
    time.sleep(0.1)
    bus.write_byte_data(MPU6050_ADDR, Enable , 1)
    time.sleep(0.1)
    return gyro_config_vals[gyro_indx],accel_config_vals[accel_indx]
    
def read_raw_bits(register):
    high = bus.read_byte_data(MPU6050_ADDR, register)
    low = bus.read_byte_data(MPU6050_ADDR, register+1)
    value = ((high << 8) | low)

    if(value > 32768):
        value -= 65536
    return value

def mpu6050_conv():
    acc_x = read_raw_bits(AccelXOut)
    acc_y = read_raw_bits(AccelYOut)
    acc_z = read_raw_bits(AccelZout)
    gyro_x = read_raw_bits(GyroXOut)
    gyro_y = read_raw_bits(GyroYOut)
    gyro_z = read_raw_bits(GyroZOut)

    a_x = (((acc_x/(2.0**15.0))*accel_sens)*9.80665)
    a_y = (((acc_y/(2.0**15.0))*accel_sens)*9.80665)
    a_z = (((acc_z/(2.0**15.0))*accel_sens)*9.80665)

    w_x = (((gyro_x/(2.0**15.0))*gyro_sens)*0.017448352875489)
    w_y = (((gyro_y/(2.0**15.0))*gyro_sens)*0.017448352875489)
    w_z = (((gyro_z/(2.0**15.0))*gyro_sens)*0.017448352875489)

    return a_x,a_y,a_z,w_x,w_y,w_z

def AK8963_start():
    bus.write_byte_data(AK8963_ADDR,AK8963_CNTL,0x00)
    time.sleep(0.1)
    AK8963_bit_res = 0b0001 
    AK8963_samp_rate = 0b0110 
    AK8963_mode = (AK8963_bit_res <<4)+AK8963_samp_rate 
    bus.write_byte_data(AK8963_ADDR,AK8963_CNTL,AK8963_mode)
    time.sleep(0.1)
    
def AK8963_reader(register):
    low = bus.read_byte_data(AK8963_ADDR, register-1)
    high = bus.read_byte_data(AK8963_ADDR, register)
    value = ((high << 8) | low)
    if(value > 32768):
        value -= 65536
    return value

def AK8963_conv():
    loop_count = 0
    while 1:
        mag_x = AK8963_reader(HXH)
        mag_y = AK8963_reader(HYH)
        mag_z = AK8963_reader(HZH)

        if bin(bus.read_byte_data(AK8963_ADDR,AK8963_ST2))=='0b10000':
            break
        loop_count+=1
        
    m_x = (mag_x/(2.0**15.0))*mag_sens
    m_y = (mag_y/(2.0**15.0))*mag_sens
    m_z = (mag_z/(2.0**15.0))*mag_sens

    return m_x,m_y,m_z
    
# MPU6050 Registers
MPU6050_ADDR = 0x68
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
Config       = 0x1A
GyroConfig  = 0x1B
AccelConfig = 0x1C
Enable   = 0x38
AccelXOut = 0x3B
AccelYOut = 0x3D
AccelZout = 0x3F
TempOut   = 0x41
GyroXOut  = 0x43
GyroYOut  = 0x45
GyroZOut  = 0x47
#AK8963 registers
AK8963_ADDR   = 0x0C
AK8963_ST1    = 0x02
HXH          = 0x04
HYH          = 0x06
HZH          = 0x08
AK8963_ST2   = 0x09
AK8963_CNTL  = 0x0A
mag_sens = 4900.0 

bus = smbus.SMBus(1) 
gyro_sens,accel_sens = MPU6050_start() 
AK8963_start() 