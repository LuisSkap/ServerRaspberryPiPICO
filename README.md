# ServerRaspberryPiPICO

Aprende a programar una aplicación IoT en la nueva Raspberry Pi PICO W
Título sugerido: Programa tu propia aplicación IoT con la nueva Raspberry Pi PICO W  
La nueva tarjeta diseñada y fabricada por Raspberry Pi está enfocada en el desarrollo de proyectos y dispositivos que van desde proyectos escolares y dispositivos IoT, hasta señalizacion y procesos de fabricación dentro de la industria, esta tarjeta te permite controlar todo tipo de aplicaciones domésticas, industriales y de pasatiempos.
Estas nuevas tarjetas Raspberry Pi PICO se pueden programar en C y MicroPython, puedes adaptarla  a una gran gama de aplicaciones, niveles de habilidad y conocimiento; y comenzar es tan sencillo como arrastrar un archivo a una USB.
Una vez que domines los primeros pasos con esta tarjeta, puedes hacer uso de sus periféricos más avanzados, como lo son SPI, I2C y ocho máquinas de estado de E/S programables para compatibilidad con periféricos personalizados.
Descubre la nueva versión mejorada de la Raspberry Pi PICO, ahora con conectividad WiFi integrada para poder desarrollar tu proyecto IoT de manera muy sencilla.
En este blog te vamos a mostrar como hacer tu primer programa IoT dentro de una Raspberry Pi PICO W. Comenzamos por mostrarte el entorno de programación Thonny, un desarrollo de software libre, diseñado para compilar tus programas de Python y MicroPython.
Para comenzar necesitamos instalar el IDE Thonny de libre uso.
Puedes descargar el IDE en el siguiente link:
    IDE Thonny (Poner el link de abajo)
    https://thonny.org
    
# LISTA DE MATERIALES:
El material necesario es el siguiente. 
   Raspberry Pi PICO W (Poner el link de abajo)
   https://www.agelectronica.com/detalle.php?p=RASPBERRY-PI-PICO-W 
   CABLE MICRO USB A USB TIPO (A) PARA RASPBERRY PI  (Poner el link de abajo) 
   https://www.agelectronica.com/detalle.php?p=RPI-CABLE-USB-A-MICRO-USB
   CONFIGURANDO EL IDE THONNY:
En nuestro editor Thonny vamos a actualizar los controladores de la tarjeta Raspberry Pi Pico W
 
Entramos en la pestaña Herramientas > Opciones
 
En la pestaña Intérprete seleccionamos la opción de Micro Python y en Puerto dejamos la opción de < intentar detectar el puerto automáticamente>.
Antes de conectar la tarjeta. Primero presionamos el botón “BOOTSEL” en la tarjeta, y sin soltarlo conectamos al PC.
Soltamos el botón de la PICO y presionamos en la PC el botón de “instalar o actualizar el firmware”.
 
Una vez que termine el proceso de actualización en la misma pestaña de Puerto aparecerá un nuevo COM con nuestra Raspberry Pi Pico W.
Presionamos Ok para regresar al editor.

# CREAR UN NUEVO PROYECTO EN THONNY:

 Una vez terminado, en el archivo nuevo que aparece en pantalla, escribimos nuestras credenciales para acceder a tu red Wi-Fi
 
Le damos click en guardar en los iconos de arriba. Y aparecerá una ventana como esta
 
Guardamos en Raspberry Pi Pico con el nombre de “secrets.py” y damos click en “Ok”
 
Creamos un nuevo archivo en el icono de “+” sobre el editor
 
Pegamos el código de ejemplo que está al final de este blog.
 
Volvemos a guardar de la misma manera el documento pero esta vez lo nombramos como “Led_1.py”.

Una vez que esté guardado, damos click en “Ejecutar el script actual”
 
Una vez que observamos en la pestaña de consola que conectó correctamente. Obtendremos la información que necesitaremos para controlar vía remota nuestra app.
 
# VERIFICANDO EL FUNCIONAMIENTO:
 
Abrimos un navegador Web y asegurándonos que estamos dentro de la misma red WiFi. Buscamos la siguiente dirección web “XX.XX.XX.XX/light/on”. Donde XX.XX.XX.XX Es la dirección ip que despliega en consola tu Raspberry Pi PICO W
Y veremos una página como la que sigue

Si tenemos un LED conectado en el pin 15 y a GND veremos como enciende y apaga con el botón de la página web.

