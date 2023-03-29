from city_functions import city_country
import unittest


class TestCities(unittest.TestCase):
    def test_city_country(self):
        test = city_country('santiago', 'chile')
        self.assertEqual(test, 'Santiago,Chile')

    def test_city_country_population(self):
        test = city_country('santiago', 'chile', 5000000)
        self.assertEqual(test, 'Santiago,Chile-population 5000000')


if __name__ == '__main__':
    unittest.main()
