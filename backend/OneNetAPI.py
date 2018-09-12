#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import json
import urllib
import urllib2

from Config import Config

class OneNetAPI():
    config = None

    def __init__(self):
        conf_filename = "OneNetAPI.cfg"
        self.config = Config(conf_filename)

    def http_request(self, url, parameter, data, request_method):
        #******************** proxy used only ********************
        """
        proxy_url = dict([list(self.config.getConfigValues('PROXY')[0])])
        proxy = urllib2.ProxyHandler(proxy_url)
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
        """

        request = urllib2.Request(url + parameter, data)  
        request.add_header('api-key', self.config.getConfigValues('KEY', key = 'api-key'))  
        request.get_method = lambda:request_method  
        request = urllib2.urlopen(request) 

        return request.read()
        
    def register_device(self, device_info):
        #values = {}
        #values['sn'] = '456666'
        #values['title'] = '454545454'
        data = json.dumps(device_info)
        register_url = self.config.getConfigValues('URL', key = 'register_url')
        register_code = self.config.getConfigValues('KEY', key = 'register_code')
        parameter = {}
        parameter['register_code'] = register_code
        
        result = json.loads(self.http_request(register_url, urllib.urlencode(parameter), data, 'POST'))

        if result['errno'] == 0:
            print("Device {0} registered successfully.".format(result['data']['device_id']))
            
            #return result['device_id']
            return result

        else:
            print("Device {0} registered failed.\nError: {1}".format(result['data']['device_id'], result['error']))
        
        return False

    def add_device(self, device_info):
        #values = {}
        #values['title'] = '456666'
        #values['desc'] = '454545454'
        #values['protocol'] = 'HTTP'
        #values['auth_info'] = '112'
        data = json.dumps(device_info)
        add_url = self.config.getConfigValues('URL', key = 'add_url')
        parameter = {}
        
        result = json.loads(self.http_request(add_url, urllib.urlencode(parameter), data, 'POST'))

        if result['errno'] == 0:
            #return result['data']['device_id']
            print("Device {0} added successfully.".format(result['data']['device_id']))
            return result
        else:
            print("Device {0} registered failed.\nError: {1}".format(result['data']['device_id'], result['error']))

        return False
    
    def search_device(self, auth_info):
        search_url = self.config.getConfigValues('URL', key = 'search_url')
        parameter = {}
        parameter['auth_info'] = auth_info
      
        result = json.loads(self.http_request(search_url, urllib.urlencode(parameter), None, 'GET'))

        if result['errno'] == 0:
            return result

        return False
    
    def write_file(self, name, content):
        with open(name, 'w') as file:
            file.write(content)
    
    def check_file_is_exist(self, name):
        is_exist = os.path.exists(name)

        return is_exist

