#!/usr/bin/python
# -*- coding: UTF-8 -*-

from OneNetAPI import OneNetAPI

def main():
    conf_filename = "OneNetAPI.cfg"
    api = OneNetAPI(conf_filename)
    #api.register_device()
    #device_id = api.add_device()
    #if device_id:
    #   api.write_file('DEVICE_ID', device_id)
    #print(api.search_device('39088078'))
    print(api.search_device('390880781'))

if __name__ == "__main__":
    main()