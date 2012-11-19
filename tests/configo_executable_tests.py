import os
import subprocess
import unittest
import re

class ConfigoExecutableTest(unittest.TestCase):

    def setUp(self):
        if not re.search(r'/tests', os.getcwd()):
            cwd = '{0}/tests'.format(os.getcwd())
        else:
            cwd = os.getcwd()

        self.config_path = "{0}/fixtures/config.json".format(cwd)

    def cmd(self, *args):
        process = subprocess.Popen(*args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = process.communicate()[0]
        return_code = process.wait()
        result = { "output": output, "return_code": return_code }
        return result


    def test_get_key_with_from_config_get_key_syntax(self):
        result = self.cmd(['bin/configo', 'from' , self.config_path, 'get', 'application'])
        self.assertEqual(result['output'], 'My Application')
        self.assertEqual(result['return_code'], 0)

    def test_get_not_existing_key_with_from_config_get_key_syntax(self):
        result = self.cmd(['bin/configo', 'from' , self.config_path, 'get', 'somenonexistingkey'])
        self.assertRegexpMatches(result['output'], r'Error: You are searching for not existing key')
        self.assertEqual(result['return_code'], 1)

    def test_execute_configo_without_any_arguments(self):
        result = self.cmd(['bin/configo'])
        self.assertRegexpMatches(result['output'], r'show help message and exit')
        self.assertEqual(result['return_code'], 0)

    def test_get_key_without_syntax_from_config_get_key(self):
        result = self.cmd(['bin/configo', self.config_path, 'application'])
        self.assertEqual(result['output'], 'My Application')
        self.assertEqual(result['return_code'], 0)

    def test_get_key_lazy_way(self):
        result = self.cmd(['bin/configo', 'get', 'application'])
        self.assertEqual(result['output'], 'My Application')
        self.assertEqual(result['return_code'], 0)

    def test_execute_configo_lazy_syntax_without_key(self):
        result = self.cmd(['bin/configo', 'get'])
        self.assertRegexpMatches(result['output'], r'configo get some.key')
        self.assertEqual(result['return_code'], 1)

    def test_execute_configo_with_from_config_get_key_syntax_without_key(self):
        result = self.cmd(['bin/configo', 'from' , self.config_path, 'get'])
        self.assertRegexpMatches(result['output'], r'Please tell me what key you want')
        self.assertEqual(result['return_code'], 1)

    def test_execute_configo_with_from_config_get_key_syntax_without_config_and_get_and_key(self):
        result = self.cmd(['bin/configo', 'from' ])
        self.assertRegexpMatches(result['output'], r'Please fill config path')
        self.assertEqual(result['return_code'], 1)


if __name__ == "__main__":
    unittest.main()