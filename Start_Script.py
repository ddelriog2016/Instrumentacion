# Prorama: Guardian 1.0
# Fecha: 22 Abril 2016
# Autor: David del Rio / Mike Amezcua (Trabajo de instrupentacion)
# Descripcion: Programa de Inicializacion en Yocto Edison

# Define librerias a Utilizar
import pyupm_i2clcd as lcd
import os
import time

# Inicializa el LCD I2C en  0x3E (LCD_ADDRESS)  0x62 (RGB_ADDRESS)
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
time.sleep(2)
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
time.sleep(2)


# RGB En Blanco
myLcd.setColor(255, 255, 255)
myLcd.clear()

# Inicia desplegando Creditos
myLcd.setCursor(0,0)
myLcd.write("David del Rio")
myLcd.setCursor(1,0)
myLcd.write("Mike Amezcua")
time.sleep(5)

# En Amarillo
myLcd.setColor(255, 255, 0)
myLcd.clear()

myLcd.setCursor(0,0)
myLcd.write("Proyecto1")
myLcd.setCursor(1,0)
myLcd.write("Instrumentacion")
time.sleep(10)

# En Verde
myLcd.setColor(0, 255, 0)
myLcd.clear()

myLcd.setCursor(0,0)
myLcd.write(" RED...")


# Espera a que Yocto tenga el servicio de RED
while 1:

        f = os.popen('ifconfig wlan0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1')
        IP= f.read().strip()
        if IP != "" : break
        time.sleep(2)

myLcd.setCursor(0,0)
myLcd.write(IP)

# Publica la IP al Usuario
msg="Iniciando con IP %s" %IP
banner="/home/root/pushover.sh/pushover.sh  %s " % msg
os.system(banner)
time.sleep(10)

