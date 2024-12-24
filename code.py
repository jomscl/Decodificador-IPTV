import time
import usb_hid
import microcontroller
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_httpserver import Server, Request, Response, POST

import os
import ipaddress
import wifi
import socketpool

def enviaK(kbd,num):
    nums=[Keycode.ZERO,
        Keycode.ONE, 
        Keycode.TWO, 
        Keycode.THREE,
        Keycode.FOUR,
        Keycode.FIVE,
        Keycode.SIX,
        Keycode.SEVEN,
        Keycode.EIGHT,
        Keycode.NINE]
    if 0<=num<=9:
        key=nums[num]
        kbd.send(key)
        time.sleep(0.2)
        kbd.release(key)

def webpage(numero):
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta http-equiv="Content-type" content="text/html;charset=utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
    <title>Pico W HTTP Server</title>
    <h1>Pico W HTTP Server</h1>
    <br>
    <p class="dotted">This is a Pico W running an HTTP server with CircuitPython.</p>
    <br>
    Texto enviado {numero}
    </body></html>
    """
    return html


# Codigo principal


# Set up a keyboard device.
kbd = Keyboard(usb_hid.devices)

# WIFI

print()
print("Connecting to WiFi")

#  set static IP address
ipv4 =  ipaddress.IPv4Address("192.168.2.88")
netmask =  ipaddress.IPv4Address("255.255.255.0")
gateway =  ipaddress.IPv4Address("192.168.2.1")
wifi.radio.set_ipv4_address(ipv4=ipv4,netmask=netmask,gateway=gateway)

#  connect to your SSID
wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID'), os.getenv('CIRCUITPY_WIFI_PASSWORD'))

print("Connected to WiFi")

pool = socketpool.SocketPool(wifi.radio)
server = Server(pool, "/static", debug=False)
#  prints MAC address to REPL
print("My MAC addr:", [hex(i) for i in wifi.radio.mac_address])

#  prints IP address to REPL
print("My IP address is", wifi.radio.ipv4_address)

#  pings Google
ipv4 = ipaddress.ip_address("8.8.4.4")
print("Ping google.com: %f ms" % (wifi.radio.ping(ipv4)*1000))
# Fin wifi



@server.route("/")
def base(request: Request):  # pylint: disable=unused-argument
    #  serve the HTML f string
    #  with content type text/html
    raw_text = request.raw_request.decode("utf8")
    #print(raw_text)
    pos=raw_text.find("?numero=")+8
    numero=raw_text[pos:pos+4]
    if numero!="0000":
        print(f"Mandando: {numero}")
        #numero="12344"
        for p in range(len(numero)):
            enviaK(kbd, int(numero[p]))
    else:
        enviaK(kbd, 0)
    return Response(request, f"{webpage(numero)}", content_type='text/html')

# Iniciar servidor web
print("starting server..")
# startup the server

try:
    server.start(str(wifi.radio.ipv4_address))
    print("Listening on http://%s:80" % wifi.radio.ipv4_address)
#  if the server fails to begin, restart the pico w
except OSError:
    time.sleep(5)
    print("restarting..")
    microcontroller.reset()
ping_address = ipaddress.ip_address("8.8.4.4")



# n=0
# while n<0:
#     nt="000"+str(n)
#     for p in range(len(nt)-4, len(nt)):
#         enviaK(kbd, int(nt[p]))
#     n+=1
#     kbd.press(Keycode.ENTER)
#     kbd.release_all()
#     time.sleep(0.2)



while True:
    try:

        #  poll the server for incoming/outgoing requests
        server.poll()

    except Exception as e:
            print(e)
            continue


