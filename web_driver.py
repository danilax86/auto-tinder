from selenium import webdriver

from location_manager import LocationManager


class WebDriver:
    location = LocationManager()

    executable_path = r'C:\Program Files\Selenium\geckodriver.exe'
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
