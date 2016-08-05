import googlemaps
import unittest

def geocode_adress(ad):
	gmaps = googlemaps.Client(key='AIzaSyBZpb2c0Y6tM6oG5rAuWyBT7wBMJXCe2b8')
	location = gmaps.geocode(ad)
	lat = location[0]["geometry"]["location"]["lat"]
	lon = location[0]["geometry"]["location"]["lng"]
	return str(lat)+', '+str(lon)

def reversegeocode(rev):
	gmaps = googlemaps.Client(key='AIzaSyBZpb2c0Y6tM6oG5rAuWyBT7wBMJXCe2b8')
	reverse_geocode_result = gmaps.reverse_geocode(rev)
	return reverse_geocode_result[0]['formatted_address']

class testgeocoderers(unittest.TestCase):

    def testNormalAdress(self):
        result = geocode_adress('575 Corporate DriveMahwah, NJ')
        self.assertEquals(result, '41.083075, -74.15788')

    def testReverseGeocode(self):
    	result = reversegeocode((41.083075, -74.15788))
    	self.assertEquals(result, '575 Corporate Dr, Mahwah, NJ 07430, USA')

    def testNormalAdress2(self):
        result = geocode_adress('Raul Wallenberg St 22, Tel Aviv-Yafo')
        self.assertEquals(result, '32.1111724, 34.838567')

    def testReverseGeocode2(self):
    	result = reversegeocode((49.2868232, -123.1221176))
    	self.assertEquals(result, '1111 Melville St, Vancouver, BC V6E, Canada')

    def testfakeReverseCode(self):
    	result = reversegeocode((11.11, 22.22))
    	self.assertEquals(result, 'Negative Test st.')


    


if __name__ == '__main__':
		unittest.main(exit=False)
