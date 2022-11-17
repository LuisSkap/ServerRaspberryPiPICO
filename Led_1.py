import network  # Importar librerías necesarias
import socket
import time
import secrets  # Librería con las credenciales de tu red Wi-Fi

from machine import Pin

#Asignación de pin para el LED
led = Pin(15, Pin.OUT)

# Configuración de red Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.config(pm = 0xa11140)

wlan.connect(secrets.SSID, secrets.PASSWORD)


# Página HTML
html_on = """<!DOCTYPE html>
<html>
    <head> <title>Raspberry pi Pico W</title>
    <style>html { font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}
    
    .buttonRed { background-color: #d11d53; border: 2px solid #000000;; color: white; padding: 15px 32px; text-align: center;
    text-decoration: none; display: font-size: 16px; margin: 4px 2px; cursor: pointer; }
    text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
    </style></head>
    <body> <center><h1>Server on a Pico W</h1></center><br><br>
        <form><center>
            <center> <button class="buttonRed" name="Apagar" value="Off" formaction="/light/off" type="submit">Apagar LED </button>
            <br><br>
            <center><p>%s</p>
        </center></form>
    </body>
</html>
"""

html_off = """<!DOCTYPE html>
<html>
    <head> <title>Raspberry pi Pico W</title>
    <style>html { font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}
    
    .button { background-color: #4CAF50; border: 2px solid #000000;; color: white; padding: 15px 32px; text-align: center;
    text-decoration: none; display: font-size: 16px; margin: 4px 2px; cursor: pointer; }
    text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
    </style></head>
    <body> <center><h1>Server on a Pico W</h1></center><br><br>
        <form><center>
            <center> <button class="button" name="Encender" value="On" formaction="/light/on" type="submit">Encender LED </button>
            <br><br>
            <center><p>%s</p>
        </center></form>
    </body>
</html>
"""

#Esperamos que la conexion WiFi se establezca o falle
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

# Error al conectar la red WiFi
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )
    print( 'Subnet = ' + status[1] )
    print( 'Gateway = ' + status[2] )
    print( 'DNS = ' + status[3] )

# Open socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

#Esperamos una conexion a nuestra pagina
while True:
    try:
        cl, addr = s.accept()
        print('client connected from', addr)
        request = cl.recv(1024)
        print(request)

        request = str(request)
        led_on = request.find('/light/on')
        led_off = request.find('/light/off')
        print( 'led on = ' + str(led_on))
        print( 'led off = ' + str(led_off))

        if led_on == 6:
            print("led on")
            led.value(1)
            stateis = "Encendido"
            response = html_on % stateis

        if led_off == 6:
            print("led off")
            led.value(0)
            stateis = "Apagado"
            response = html_off % stateis

        

        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()

    except OSError as e:
        cl.close()
        print('connection closed')
