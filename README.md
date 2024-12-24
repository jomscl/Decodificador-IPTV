Proyecto que prueba combinaciones de teclas para el docodificador de IPTV Arris VIP524W

En resumen, se prueban las combinaciones de claves usando un Raspebbry pi pico w, comandado y coordinado por el pc usando Python. Esto solo funciona porque el decodificador acepta un teclado USB como imput, además de no tener tiempo de espera por intentos fallidos.

Setup:
- Raspberry pi pico W.
  - La placa raspberry pi pico W se le carga el binario base de circuitpython.
  - Se configurado el wifi para la red de cada uno.
  - Se le debe cargar el código code.py y las librerías contenidas en la carpeta lib
  - En el archivo code.py se puede especificar un ip fijo para hacer mas fácil la comunicación. Debe ser en la misma red y segemento que el pc donde se ejecuta python. Debe ser un ip que no exista previamente en la red local.
- Se conecta por un cable USB el decodificador y la placa Rasperry pi pico W.
- La salida HDMI del decodificador debe ir como imput al PC. En mi caso usé un capturador HDMI a USB. Esto permite a python capturar la pantalla.
- El codigo deco.py se debe ejecutar en el pc. Debiera dar lo mismo si se ejecuta en Linux o Windows.

Configuración:
- Además de la red wifi del raspberry, se debe configurar el sector de pantalla donde python va a observar si la clave funciona o no. Eso se debe configurar en la sección bounding box y en la seccion captura. Queda en dos partes por separado ya que se guarda una captura de cada intento, para analisis posterior.
- Al iniciar el raspberry pi pico va a intentar conectar a la red wifi configurada previamente.
- En python se debe especificar el ip usado por el raspberry pi pico w

Testing del raspberry pi pico W.
- Conectando la placa a un pc, abrir un editor de texto y dejar el cursor listo para escribir.
- Usando OTRO equipo en la misma red (o celular por wifi), se accede a la dirección http://{ip}:5000/?numero=1234. Se debieran escribir los números 1234 en el block de notas. Este código no admite letras o mas digitos que 4.

Uso:
- Se prende la aplicación para abrir la cámara de fotos. En Windows 10, 11 se puede usar la aplicación Cámara, usada para ver webcams, pero se puede cambiar para ver el output del capturador HDMI.
- Se prende el decodificador y hay que presionar el boton home en el proceso de inicio, para entrar al modo de administrador, donde pide la clave.
- En ese momento se puede hacer a andar python en el pc, probando 1 a una las claves hasta que se acepte.
