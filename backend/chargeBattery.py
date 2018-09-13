#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time

from Car import Car
from Charger import Charger
from OneNetAPI import OneNetAPI

def main():
    api = OneNetAPI()
    car = Car()
    charger = Charger()

    charger_device_id = api.search_device("192168110")['data']['devices'][0]['id']
    car_device_id = api.search_device("192168120")['data']['devices'][0]['id']
    
    #***********
    #    car
    #*********** send car first connection event ***********
    message = {}
    message['messageType'] = 'connect'
    message['deviceType'] = 'car'
    message['deviceId'] = car_device_id
    message['connectedDeviceId'] = charger_device_id
    message['connectedDeviceType'] = 'charger'
    message['connectionStatus'] = True

    time.sleep(5)
    result = car.sendMessageToTransactionLogger(message)
    print(result)

    #***********
    #  charger
    #*********** send charger auth message event ***********
    message = {}
    message['messageType'] = 'auth'
    message['deviceType'] = 'charger'
    message['deviceId'] = charger_device_id
    message['authDeviceId'] = car_device_id
    message['authDeviceType'] = 'car'
    message['authStatus'] = True
    
    time.sleep(5)
    result = charger.sendMessageToTransactionLogger(message)
    print(result)

    #***********
    #    car
    #*********** send car auth message event ***********
    message = {}
    message['messageType'] = 'auth'
    message['deviceType'] = 'car'
    message['deviceId'] = car_device_id
    message['authDeviceId'] = charger_device_id
    message['authDeviceType'] = 'charger'
    message['auth_status'] = True

    time.sleep(5)
    result = car.sendMessageToTransactionLogger(message)
    print(result)

    #***********
    #    car
    #*********** send balance is enough event ***********
    message = {}
    message['messageType'] = 'balance'
    message['deviceType'] = 'car'
    message['deviceId'] = car_device_id
    message['balanceStatus'] = True

    time.sleep(5)
    result = car.sendMessageToTransactionLogger(message)
    print(result)

    #***********
    #    car
    #*********** send transaction is done event ***********
    message = {}
    message['messageType'] = 'transaction'
    message['deviceType'] = 'car'
    message['deviceId'] = car_device_id
    message['transactionStatus'] = 'done'

    time.sleep(5)
    result = car.sendMessageToTransactionLogger(message)
    print(result)

    #***********
    #  charger
    #*********** send transaction is valid event ***********
    message = {}
    message['messageType'] = 'transaction'
    message['deviceType'] = 'charger'
    message['deviceId'] = charger_device_id
    message['transactionStatus'] = True

    time.sleep(5)
    result = charger.sendMessageToTransactionLogger(message)
    print(result)

    #***********
    #  charger
    #*********** send charging event ***********
    message = {}
    message['messageType'] = 'charging'
    message['deviceType'] = 'charger'
    message['deviceId'] = charger_device_id
    message['chargingStatus'] = True

    time.sleep(5)
    result = charger.sendMessageToTransactionLogger(message)
    print(result)

    #***********
    #    car
    #*********** send charging event ***********
    message = {}
    message['messageType'] = 'charging'
    message['deviceType'] = 'car'
    message['deviceId'] = car_device_id
    message['chargingStatus'] = True

    time.sleep(5)
    result = car.sendMessageToTransactionLogger(message)
    print(result)


if __name__ == "__main__":
    main()