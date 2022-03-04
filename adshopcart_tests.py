import unittest
import adshopcart_methods as methods
import adshopcart_locators as locators


class AdshopcartPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_adshopcart():
        methods.setUp()
        methods.check_homepage()
        methods.create_new_user()
        methods.check_my_account()
        methods.delete_new_account()
        methods.confirm_account_deletion()
        methods.tearDown()
