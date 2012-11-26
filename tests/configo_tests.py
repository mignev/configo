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

        self.json_config_path = "{0}/fixtures/config.json".format(cwd)
        self.yaml_config_path = "{0}/fixtures/config.yaml".format(cwd)
        self.configo = Configo()

    def test_json_get_key(self):
        result = self.configo.get_key(self.json_config_path, 'application')
        self.assertEqual(result, 'My Application')

    def test_json_get_netsted_key_from_dict(self):
        result = self.configo.get_key(self.json_config_path, 'webservers.api.host')
        self.assertEqual(result, 'api.some.com')

    def test_json_get_nested_key_from_list(self):
        result = self.configo.get_key(self.json_config_path, 'list.0')
        self.assertEqual(result, '1')

    def test_json_get_not_existing_key(self):
        with self.assertRaises(ConfigoNotExistingKeyError) as ex:
            self.configo.get_key(self.json_config_path, 'somenotexistingkey')

    def test_json_get_nested_key_from_list_with_not_existing_key(self):
        with self.assertRaises(ConfigoNotExistingKeyError) as ex:
            self.configo.get_key(self.json_config_path, 'list.10')

    def test_json_get_nested_key_from_dict_with_not_existing_key(self):
        with self.assertRaises(ConfigoNotExistingKeyError) as ex:
            self.configo.get_key(self.json_config_path, 'dict.some.key')

    def test_detect_config_type(self):
        json_config = '/home/blabla/some.conf.json'
        yaml_config = '/etc/project.project/configuration.yaml'
        xml_config  = '/some/xml.config.xml'

        self.assertEqual(self.configo.config_type(json_config), 'json')
        self.assertNotEqual(self.configo.config_type(xml_config), 'json')
        self.assertEqual(self.configo.config_type(xml_config), 'xml')
        self.assertEqual(self.configo.config_type(yaml_config), 'yaml')

    def test_yaml_get_key(self):
        result = self.configo.get_key(self.yaml_config_path, 'application')
        self.assertEqual(result, 'My Application')

    def test_yaml_get_netsted_key_from_dict(self):
        result = self.configo.get_key(self.yaml_config_path, 'webservers.api.host')
        self.assertEqual(result, 'api.some.com')

    def test_yaml_get_nested_key_from_list(self):
        result = self.configo.get_key(self.yaml_config_path, 'list.0')
        self.assertEqual(result, '1')

    def test_yaml_get_nested_key_from_list_1_with_diff_syntax(self):
        result = self.configo.get_key(self.yaml_config_path, 'list1.0')
        self.assertEqual(result, 'item1')

    def test_yaml_get_not_existing_key(self):
        with self.assertRaises(ConfigoNotExistingKeyError) as ex:
            self.configo.get_key(self.yaml_config_path, 'somenotexistingkey')

    def test_yaml_get_nested_key_from_list_with_not_existing_key(self):
        with self.assertRaises(ConfigoNotExistingKeyError) as ex:
            self.configo.get_key(self.yaml_config_path, 'list.10')

    def test_yaml_get_nested_key_from_dict_with_not_existing_key(self):
        with self.assertRaises(ConfigoNotExistingKeyError) as ex:
            self.configo.get_key(self.yaml_config_path, 'dict.some.key')

if __name__ == "__main__":
    unittest.main()