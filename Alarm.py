# Prorama: Guardian 1.0
# Fecha: 22 Abril 2016
# Autor: David del Rio / Mike Amezcua (Trabajo de instrupentacion)
# Descripcion: Alarma LCD I2C + Sensor EZ1 + Servo
import pyupm_i2clcd as lcd
import servo
import mraa
import time
import os

# Initialize Display I2C (RGB_ADDRESS)
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)

# Define pines de entrada Digital
touchPin = mraa.Gpio(4)
touchPin.dir(mraa.DIR_IN)

# Define pines de entrada Analogica
usonic=mraa.Aio(0)

# Define Servo motor
myServo=servo.Servo("First Servo")
myServo.attach(3)


# ********** FUNCIONES ************

# Funcion: medir
# Calcula 60 muestras por cada medicion y retorna distancia en cm
#
def medir():
        sum=0
        avrange=60

        for i in range(0,avrange):
                anVolt=usonic.read()
                sum=sum+anVolt

        inches=(sum/avrange)*0.497
        cm = inches*2.54
        return cm

# Funcion barrido
# Realiza un barrido de 90 grados y mide
# Retorna distancia minima
#
def barrido():
        x1=[]           #Almacena las mediciones

        for y in range(0,90,5):
                myServo.write(y)
                dist=medir()
                time.sleep(0.1)
                x1.insert(0,dist)
        return min(x1)



#
# Contador de intromiciones:
#
contador=0

time.sleep(20)


while 1:

        if  touchPin.read() == 1:
                # Clear
                myLcd.setColor(255, 0, 0)
                #myLcd.clear()
                myLcd.setCursor(0,0)
                myLcd.write("ALARMA INTRUSO")
                objeto=barrido()
                msg="Intruso a %.2f cm" % objeto
                myLcd.setCursor(1,0)
                myLcd.write(msg)
                time.sleep(1)
                contador=1

        else:

                # Clear
                contador = 0
                myLcd.setColor(255,255,255)
                #myLcd.clear()
                myLcd.setCursor(0,0)
                myLcd.write("   VIGILANDO  ")
                myLcd.setCursor(1,0)
                myLcd.write("               ")
                #time.sleep(0.5)


        if contador == 1 :

                banner="/home/root/pushover.sh/pushover.sh  %s " % msg
                os.system(banner)
                time.sleep(5)
