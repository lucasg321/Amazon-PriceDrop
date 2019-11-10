import unittest
import PriceDrop


#unittest documentation https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug


#declare test class as an instance of unittest
class TestPriceDrop(unittest.TestCase):

    #first test function testing the api call
    def test_set_asin(self):
        PriceDrop.asinentry.insert(0,"B07BFH96M3")
        result = PriceDrop.set_asin()
        self.assertIsNotNone()

    #second test function testing the asin button
    def test_set_asin_real(self):
        PriceDrop.asinentry.insert(0,"B07BFH96M3")
        result = PriceDrop.set_asin_real()
        self.assertEquals(result, "RS Components Raspberry Pi 3 B+ Motherboard")

    #third test function testing the twilio Client object
    def test_send_twilio(self):
        PriceDrop.phone_num = "+14165552221"
        client = PriceDrop.send_twilio()
        self.assertEqual(client.from_, "+14165552221")

    #easily run the unit tests
#if __name__ == '__main__':
#    unittest.main()

