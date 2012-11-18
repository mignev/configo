Configo
=======

Easy way to use existing JSON, XML or YAML config files from bash

configo config.json/yaml/xml some.key
configo config.json/yaml/xml some.other.key

configo from config.json/yaml/xml get some.key

#Sample json example

{
  "list": [1,2,3],
  "pingable": "192.168.2.1",
  "port": "8080",
  "user_ssl": "true",
  "user": { "username": "migi", "first_name": "marian", "last_name": "ignev", "some": {"test": "test_value"} }
}

# Example 1
VARNAME=`configo from config.json get some.key`

# Example 2
TARGET_CONF="/etc/some/conf.json"
CONFIGO="configo from $TARGET_CONF"
VARNAME=`$CONFIGO get some.key.value`

# Example 3
export CONFIGO_CONF=`/some/config/path/conf.json`
VARNAME=`configo get some.key`
VARNAME1=`configo get anoter.key`

# TODO
- Add tests
- Add xml support
- Add yaml support