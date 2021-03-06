from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase
from nokia import NokiaApi

from nokiaapp.utils import create_nokia, get_setting


class TestNokiaUtilities(TestCase):
    def test_create_nokia(self):
        """
        Check that the create_nokia utility creates a WithingnsApi object
        and an error is raised when the consumer key or secret aren't set.
        """
        with self.settings(NOKIA_CLIENT_ID=None, NOKIA_CONSUMER_SECRET=None):
            self.assertRaises(ImproperlyConfigured, create_nokia)
        with self.settings(NOKIA_CLIENT_ID='a', NOKIA_CONSUMER_SECRET=None):
            self.assertRaises(ImproperlyConfigured, create_nokia)
        with self.settings(NOKIA_CLIENT_ID=None, NOKIA_CONSUMER_SECRET='a'):
            self.assertRaises(ImproperlyConfigured, create_nokia)
        api = create_nokia(token_expiry=1534796425)
        self.assertEqual(type(api), NokiaApi)
        self.assertEqual(api.credentials.client_id,
                         get_setting('NOKIA_CLIENT_ID'))
        self.assertEqual(api.credentials.consumer_secret,
                         get_setting('NOKIA_CONSUMER_SECRET'))
        self.assertEqual(api.credentials.token_expiry, 1534796425)
        self.assertTrue(int(api.token['expires_in']) < 0)

    def test_get_setting_error(self):
        """
        Check that an error is raised when trying to get a nonexistent setting.
        """
        self.assertRaises(ImproperlyConfigured, get_setting, 'DOES_NOT_EXIST')
