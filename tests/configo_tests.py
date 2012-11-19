from __future__ import with_statement
from configo.configo import Configo, ConfigoNotExistingKeyError
import os
import unittest
import re

class ConfigoTest(unittest.TestCase):
    def setUp(self):

        if not re.search(r'/tests', os.getcwd()):
            cwd = '{0}/tests'.format(os.getcwd())
        else:
            cwd = os.getcwd()

        self.config_path = "{0}/fixtures/config.json".format(cwd)
        self.configo = Configo()

    def test_get_key(self):
        result = self.configo.get_key(self.config_path, 'application')
        self.assertEqual(result, 'My Application')

    def test_get_netsted_key_from_dict(self):
        result = self.configo.get_key(self.config_path, 'webservers.api.host')
        self.assertEqual(result, 'api.some.com')

    def test_get_nested_key_from_list(self):
        result = self.configo.get_key(self.config_path, 'list.0')
        self.assertEqual(result, '1')

    def test_get_not_existing_key(self):
        with self.assertRaises(ConfigoNotExistingKeyError) as ex:
            self.configo.get_key(self.config_path, 'somenotexistingkey')

    def test_get_nested_key_from_list_with_not_existing_key(self):
        with self.assertRaises(ConfigoNotExistingKeyError) as ex:
            self.configo.get_key(self.config_path, 'list.10')

    def test_get_nested_key_from_dict_with_not_existing_key(self):
        with self.assertRaises(ConfigoNotExistingKeyError) as ex:
            self.configo.get_key(self.config_path, 'dict.some.key')

if __name__ == "__main__":
    unittest.main()