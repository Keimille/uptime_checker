import unittest
from checker import site_is_online

class TestGetWebsiteUrls(unittest.TestCase):
    def test_get_website_url_success(self):
        actual = site_is_online("astronomy.com")
        self.assertEqual(actual, True)
    
    def test_get_website_url_exception(self):
        with self.assertRaises(Exception):
            site_is_online("not a url")


if __name__ == '__main__':
    unittest.main()
    