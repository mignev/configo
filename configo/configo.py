#!/usr/bin/env python
from __future__ import with_statement
from os import environ
import json
import yaml
import sys

class ConfigoNotExistingKeyError(Exception): pass

class Configo():
    def __init__(self):
        self.tmp_conf_name = environ.get('CONFIGO_CONF', None)

    def load_config(self, config_path):
        config_content = ""

        if config_path.startswith('stdin'):
            config_content = sys.stdin.read()
        else:
            with open(config_path) as config:
                config_content = config.read()

        return config_content

    def config_type(self, config_path):
        return config_path.split('.')[-1]

    def config_object(self, config_path):
        config_content = self.load_config(config_path)
        config_type = self.config_type(config_path)

        result = ''

        if config_type == 'json':
            result = json.loads(config_content)
        elif config_type == 'xml':
            raise NotImplementedError
        elif config_type == 'yaml':
            result = yaml.load(config_content)

        return result

    def keyname(self, keyname, config_object):
        splited_key = keyname.split('.')

        result = ''
        iteration = 0

        for item in splited_key:
            if iteration == 0:
                result = self.get_value(config_object, item)
            else:
                result = self.get_value(result, item)

            iteration += 1
        return result

    def get_value(self, obj, item):
        result = ''
        try:
            if type(obj) == list:
                result = obj[int(item)]
            elif type(obj) == dict:
                result = obj[item]
        except (KeyError, IndexError):
            raise ConfigoNotExistingKeyError()

        return result

    def get_key(self, config_path, keyname):

        config_object = self.config_object(config_path)
        the_key = self.keyname(keyname, config_object)

        return str(the_key)
