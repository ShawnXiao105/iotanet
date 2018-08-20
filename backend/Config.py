import os
import ConfigParser

class Config():
    current_path = os.path.dirname(os.path.abspath(__file__))
    config = None
    config_file = os.path.join(current_path , "api.cfg")

    def __init__(self):
        self.config = ConfigParser.ConfigParser(allow_no_value = True)
        self.config.optionxform = str
        self.config.read(self.config_file)

    def getConfigValues(self, section, key = ""):
        result = None

        if key == "":
            result = self.config.items(section)
        else:
            result = self.config.get(section, key)

        return result

