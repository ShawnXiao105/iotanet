#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import ConfigParser

class Config():
    config = None

    def __init__(self, conf_filename):
        current_path = os.path.dirname(os.path.abspath(__file__))
        config_file = os.path.join(current_path , conf_filename)
        self.config = ConfigParser.ConfigParser(allow_no_value = True)
        self.config.optionxform = str
        self.config.read(config_file)

    def getConfigValues(self, section, key = ""):
        result = None

        if key == "":
            result = self.config.items(section)
        else:
            result = self.config.get(section, key)

        return result

