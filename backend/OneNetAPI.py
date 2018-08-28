import sys
import json
import urllib
import urllib2

from Config import Config

class OneNetAPI():
    config = None

    def __init__(self):
        self.config = Config()

    def http_request(self, url, parameter, data, request_method):
        #proxy_url = dict([list(self.config.getConfigValues('PROXY')[0])])
        #proxy = urllib2.ProxyHandler(proxy_url)
        #opener = urllib2.build_opener(proxy)
        #urllib2.install_opener(opener)

        request = urllib2.Request(url + parameter, data)  
        print url + parameter
        request.add_header('api-key', self.config.getConfigValues('KEY', key = 'api-key'))  
        request.get_method = lambda:request_method  
        request = urllib2.urlopen(request) 

        return request.read()
        
    def register_device(self):
        values = {}
        values['sn'] = '456666'
        values['title'] = '454545454'
        data = json.dumps(values)
        register_url = self.config.getConfigValues('URL', key = 'register_url')
        register_code = self.config.getConfigValues('KEY', key = 'register_code')
        parameter = {}
        parameter['register_code'] = register_code
        
        result = json.loads(self.http_request(register_url, urllib.urlencode(parameter), data))

        if result['errno'] == 0:
            print("Device {0} registered successfully.".format(values['title']))
            
            return result['device_id']
        else:
            print("Device {0} registered failed.\nError: {1}".format(values['title'], result['error']))
        
        return False

    def add_device(self):
        values = {}
        values['title'] = '456666'
        values['desc'] = '454545454'
        values['protocol'] = 'HTTP'
        values['auth_info'] = '112'
        data = json.dumps(values)
        add_url = self.config.getConfigValues('URL', key = 'add_url')
        #register_code = self.config.getConfigValues('KEY', key = 'register_code')
        parameter = {}
        #parameter['register_code'] = register_code
        
        result = json.loads(self.http_request(add_url, urllib.urlencode(parameter), data))

        if result['errno'] == 0:
            print "OK"
            return result['data']['device_id']
        
        return False
    
    def search_device(self):
        values = {}
        #values['title'] = '456666'
        data = json.dumps(values)
        search_url = self.config.getConfigValues('URL', key = 'search_url')
  
        parameter = {}
        parameter[''] = '39088078'
        #parameter['title'] = 'myedpdevice'

        result = json.loads(self.http_request(search_url, '39088078', data, 'GET'))

        print result

    def write_file(self, name, content):
        with open(name, 'w') as file:
            file.write(content)



api = OneNetAPI()
#api.register_device()
#device_id = api.add_device()

#if device_id:
#   api.write_file('DEVICE_ID', device_id)

api.search_device()