#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import json
import urllib
import urllib2

from Config import Config

class Charger():
    config = None

    def __init__(self):
        conf_filename = "TransactionLoggerAPI.cfg"
        self.config = Config(conf_filename)
    
    def http_request(self, url, data, request_method):
        #******************** proxy used only ********************
        """
        proxy_url = dict([list(self.config.getConfigValues('PROXY')[0])])
        proxy = urllib2.ProxyHandler(proxy_url)
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
        """

        header = {'Content-Type': 'application/json'}
        request = urllib2.Request('http://118.89.148.204:7001/api/transaction', data, header)  
        request.get_method = lambda:request_method  
        request = urllib2.urlopen(request) 
        
        return request.read()
    
    def sendMessageToTransactionLogger(self, message):
        data = json.dumps(message)
        api_url = self.config.getConfigValues('URL', key = 'api_url')
        result = json.loads(self.http_request(api_url, data, 'POST'))

        return result

