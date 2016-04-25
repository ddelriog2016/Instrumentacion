# Instrumentación
Proyecto de Instrumentación
Descripción: Alarma de vigilancia utilizando placa de desarrollo Edison de Intel.
Introducción: La placa de desarrollo Edison de Intel arrancara utilizando el sistema operativo Linux (Yocto) utilizando las siguientes características:

1. Conexión Wifi a un Hotspot establecido.
2. Sistema operativo Linux.
3. Un display LCD 20x2 utilizando el protocolo I2C
4. Un sensor PIR para la detección de intrusos.
5. Un sensor ultrasónico para cálculo de la distancia del intruso.
6. Un servomotor para girar el sensor ultrasónico.

Proceso de Arranque:
Hay un script definido en yocto para que sea ejecutado en el auto arranque, este script realiza la conexión a red e inicia el script en python del proyecto.

Script en Python.
El Script inicializa los sensores y en un bucle infinito realiza las siguientes tareas:
a) Muestra la en la pantalla vigilando si no al señal en el sensor PIR.
b) Si existe señal en el sensor PIR realiza lo siguiente:
  i. Despliega la palabra intruso en color rojo en el LCD.
  ii. Realiza un barrido con el sensor ultrasónico con ayuda del servomotor (Solo 90 grados)
  iii. Durante el barrido el sensor ultrasónico toma 60 muestras por posición y calcula la distancia.
  iv. Obtiene la distancia mina y la despliega en el LCD.
  v. Manda una señal de alerta por Internet al Celular de Usuario.
  vi. repite paso a)
  
  Notificación por Internet:
  Para uso práctico las notificaciones de alarma se utilizara https://pushover.net/ , servicio que es gratis por periodo de evaluación. Para obtener el servicio es necesario crear una cuenta e indexar el servicio a un teléfono celular, el cual puede ser de sistema operativo Android o IOS.
  Una vez configurando la cuenta, es posible mandar notificaciones al celular utilizando un simple script. (Ver ejemplo en el Codigo)

  
  
  
