import unittest
from client3 import getDataPoint
from client3 import getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
          stock, bid_price, ask_price, price = getDataPoint(quote)
          stockExpected = quote['stock']
          bid_priceExpected = quote['top_bid']['price']
          ask_priceExpected = quote['top_ask']['price']
          priceExpected = (bid_price + ask_priceExpected) / 2
          self.assertTupleEqual((stock, bid_price, ask_price, price),
                                (stockExpected, bid_priceExpected, ask_priceExpected, priceExpected))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            bid_priceExpected = quote['top_bid']['price']
            ask_priceExpected = quote['top_ask']['price']
            self.assertEqual((bid_price > ask_price), (bid_priceExpected > ask_priceExpected))

    """ ------------ Add more unit tests ------------ """

    def test_getRatio_calculateRatio(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        price_a = (quotes[0]['top_ask']['price'] + quotes[0]['top_bid']['price']) / 2
        price_b = (quotes[1]['top_ask']['price'] + quotes[1]['top_bid']['price']) / 2
        ratio = getRatio(price_a, price_b)
        self.assertAlmostEqual(ratio, 1.000543234234, places=5)


if __name__ == '__main__':
    unittest.main()
