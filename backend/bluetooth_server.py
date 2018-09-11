#!/usr/bin/python
# -*- coding: UTF-8 -*-

import bluetooth

from subprocess import call

class Bluetooth():
    def __init__(self):
        pass

    def lookupBluetoothDevice(self):
        print("performing inquiry...")

        nearby_devices = bluetooth.discover_devices(lookup_names = True)

        print("found %d devices" % len(nearby_devices))

        #for addr, name in nearby_devices:
        #    print("  %s - %s" % (addr, name))
        
        return nearby_devices

    def receiveMessage(self):
        port = 12345
        server_sock = None
        client_sock = None
        
        call(["/bin/hciconfig", "hci0", "piscan"])
        
        while(True):

            try:
                #server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
                server_sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)
                server_sock.bind(("", port))
                server_sock.listen(1)

                client_sock, address = server_sock.accept()
                print("Accepted connection from " + str(address))

                data = client_sock.recv(1024)
                print("received [%s]" % data)
            except Exception as e:
                print("ERROR: %s" % e)
        #else:
        #    client_sock.close()
        #    server_sock.close()

    def sendMessage(self, targetBluetoothMacAddress):
        port = 12345
        sock = None

        try:
            #sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)
            sock.connect((targetBluetoothMacAddress, port))
            sock.send("hello!!")
        except Exception as e:
            print("ERROR: %s" % e)
        else:
            sock.close()
    
bt = Bluetooth()
#print bt.lookupBluetoothDevice()
bt.receiveMessage()