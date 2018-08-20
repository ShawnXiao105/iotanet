import sys
import json
import urllib
import urllib2

from Config import Config

class OneNetAPI():
    config = None

    def __init__(self):
        self.config = Config()

    def http_request(self, url, parameter, data):
        proxy_url = dict([list(self.config.getConfigValues('PROXY')[0])])
        proxy = urllib2.ProxyHandler(proxy_url)
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)

        request = urllib2.Request(url + parameter, data)  
        request.add_header('api-key', self.config.getConfigValues('KEY', key = 'api-key'))  
        request.get_method = lambda:'POST'  
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
        else:
            print("Device {0} registered failed.\nError: {1}".format(values['title'], result['error']))
        

api = OneNetAPI()
api.register_device()