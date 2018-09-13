#!/usr/bin/python
# -*- coding: UTF-8 -*-

from OneNetAPI import OneNetAPI

def main():
    #conf_filename = "OneNetAPI.cfg"

    device_info = {}
    device_info['title'] = 'car'
    device_info['desc'] = 'The Raspberry Car'
    device_info['protocol'] = 'HTTP'
    device_info['auth_info'] = '192168120'
    device_info['other'] = {'device_type': 'car'}

    api = OneNetAPI()
    
    device_id = api.add_device(device_info)['data']['device_id']
    #print(device_id)

    #print(api.search_device('41713878'))

    if device_id:
        api.write_file('CAR_DEVICE_ID', device_id)
    
if __name__ == "__main__":
    main()