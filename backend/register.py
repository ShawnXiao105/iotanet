#!/usr/bin/python
# -*- coding: UTF-8 -*-

from OneNetAPI import OneNetAPI

def main():
    api = OneNetAPI()
    #api.register_device()
    #device_id = api.add_device()
    #if device_id:
    #   api.write_file('DEVICE_ID', device_id)
    print api.search_device('39088078')

if __name__ == "__main__":
    main()