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
        try:
            self.latitude = (geocoder.geocode(self.query))[0]['geometry']['lat']
            return self.latitude
        except IndexError:
            print("Provide correct location\n")
            self.set_location()

    def get_lng(self) -> str:
        try:
            self.longitude = (geocoder.geocode(self.query))[0]['geometry']['lng']
            return self.longitude
        except IndexError:
            print("Provide correct location\n")
            self.set_location()
