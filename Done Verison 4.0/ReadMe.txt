To run this you need to setup uart3, 
uart4, 
and I2C4 on pins(26,31)

To do this sudo nano into /boot/config.txt
add dtoverlay=uart3,9600 at the end of the file
add dtoverlay=uart4 at the end of the file after the above one
add dtoverlay=i2c4,pins(26,31)
control x
y and then enter
and then enter to save as that name

layout for raspberrypi 4 model B
uart3 = GPIO 4, Pin(7 ), TXD3
		GPIO 5, Pin(29), RXD3
			 
uart3 = GPIO 4, Pin(7 ), TXD3
		GPIO 5, Pin(29), RXD3
		
I2C4 = GPIO 7, pin(26), SCL4
I2C4 = GPIO 6, pin(31), SDA4

The rest of the layout is in the PDF file

-----------------------------------------------------------------------------------------------
Extra

To find uarts that you can setup run this in the cmd
sudo dtoverlay -a | grep uart

For the pins of the uarts
dtoverlay -h uart2

To find other aviavable ports such as the I2C4 used in this project
raspi-gpio funcs

------------------------------------------------------------------------------------------------
More Extra 

I2C pins need to be defined when enabling unlike uart becasue for example there are multiple I2C4's 
