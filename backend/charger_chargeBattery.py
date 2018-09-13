#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Charger import Charger

def main():
    charger = Charger()

    #*********** send charger auth message event ***********
    message = {}
    message['messageType'] = 'auth'
    message['deviceType'] = 'car'
    message['deviceId'] = '123'
    message['auth_status'] = True

    result = charger.sendMessageToTransactionLogger(message)
    print(result)

    #*********** send transaction is valid event ***********
    message = {}
    message['messageType'] = 'transaction'
    message['deviceType'] = 'charger'
    message['deviceId'] = '456'
    message['transaction_status'] = True

    result = charger.sendMessageToTransactionLogger(message)
    print(result)

    #*********** send charging event ***********
    message = {}
    message['messageType'] = 'charging'
    message['deviceType'] = 'charger'
    message['deviceId'] = '456'
    message['charging_status'] = True

    result = charger.sendMessageToTransactionLogger(message)
    print(result)

if __name__ == "__main__":
    main()