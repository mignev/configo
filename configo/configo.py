#!/usr/bin/env python
from __future__ import with_statement
import json, sys, os, subprocess

class ConfigoNotExistingKeyError(Exception): pass

class Configo():
    def __init__(self):
        self.tmp_conf_name = os.environ.get('CONFIGO_CONF', None)

    def load_config(self, config_path):
        with open(config_path) as config:
            config_content = config.read()
            return config_content

    def get_key(self, config_path, keyname):
        config_content = self.load_config(config_path)
        json_object = json.loads(config_content)

        splited_key = keyname.split('.')

        result = ''
        iteration = 0

        for item in splited_key:
            if iteration == 0:
                result = self.get_value(json_object, item)
            else:
                result = self.get_value(result, item)

            iteration += 1

        return str(result)

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