from opencage.geocoder import OpenCageGeocode

key = "93b99ad99b774f6a8ecc87bf9568f209"
geocoder = OpenCageGeocode(key)


class LocationManager:
    latitude: str = ""
    longitude: str = ""
    query: str = ""

    def __init__(self):
        self.set_location()

    def set_location(self):
        self.query = str(input("Provide your city: ")) + ', ' + str(input("Provide your country: "))

    def get_lat(self) -> str:
        self.latitude = (geocoder.geocode(self.query))[0]['geometry']['lat']
        return self.latitude

    def get_lng(self) -> str:
        self.longitude = (geocoder.geocode(self.query))[0]['geometry']['lng']
        return self.longitude
