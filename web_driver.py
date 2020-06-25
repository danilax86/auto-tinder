from selenium import webdriver
import os
import subprocess

from location_manager import LocationManager


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

class WebDriver:
    location = LocationManager()
    if os.name == "nt":
        pass
    else:
        subprocess.call('chmod', '0755', './geckodriver.exe')
    executable_path = r'./geckodriver.exe'

    geoAllowed = webdriver.FirefoxOptions()
    geoAllowed.set_preference('geo.prompt.testing', True)
    geoAllowed.set_preference('geo.prompt.testing.allow', True)
    geoAllowed.set_preference('geo.provider.network.url',
                              'data:application/json,{"location": {"lat": ' + str(
                                  location.get_lat()) + ', "lng": ' + str(location.get_lng()) + '}, "accuracy": 100.0}')

    def __init__(self):
        pass

    def get_options(self):
        return self.geoAllowed

    def get_executable_path(self):
        return self.executable_path
