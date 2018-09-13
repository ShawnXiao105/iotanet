#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Car import Car
from OneNetAPI import OneNetAPI

def main():
    car = Car()
    car_device_id = car.read_file('CAR_DEVICE_ID')
    

    #*********** send car first connection event ***********
    message = {}
    message['messageType'] = 'connect'
    message['deviceType'] = 'car'
    message['deviceId'] = car_device_id
    message['connectedTo'] = '456'
    message['connectionStatus'] = True

    result = car.sendMessageToTransactionLogger(message)
    print(result)
    
    #*********** send car auth message event ***********
    message = {}
    message['messageType'] = 'auth'
    message['deviceType'] = 'charger'
    message['deviceId'] = '456'
    message['auth_status'] = True

    result = car.sendMessageToTransactionLogger(message)
    print(result)

    #*********** send balance is enough event ***********
    message = {}
    message['messageType'] = 'balance'
    message['deviceType'] = 'car'
    message['deviceId'] = car_device_id
    message['balance_status'] = True

    result = car.sendMessageToTransactionLogger(message)
    print(result)
    
    #*********** send transaction is done event ***********
    message = {}
    message['messageType'] = 'transaction'
    message['deviceType'] = 'car'
    message['deviceId'] = car_device_id
    message['transaction_status'] = 'done'

    result = car.sendMessageToTransactionLogger(message)
    print(result)
    
    #*********** send charging event ***********
    message = {}
    message['messageType'] = 'charging'
    message['deviceType'] = 'car'
    message['deviceId'] = car_device_id
    message['charging_status'] = True

    result = car.sendMessageToTransactionLogger(message)
    print(result)


if __name__ == "__main__":
    main()
