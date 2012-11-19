Configo
=======

Easy way to use existing JSON, XML or YAML config files from bash shell/scripts

# How can i use it?
...

###Sample json config file
Lets say that this config file is located `/etc/myapp/config.json`

    {
      "config_version": "1.0",
      "application": "My Application",
      "webservers": {
        "api": {
          "host": "api.some.com",
          "port": "80",
          "apikey": "somekey",
          "apisecret": "somesecret"
        },

        "img": {
          "host": "img.some.com",
          "port": "8013",
          "apikey": "ihuu",
          "apisecret": "somesecret"
        },

        "video": {
          "host": "video.some.com",
          "port": "80",
          "apikey": "somekey",
          "apisecret": "somesecret"
        }
      },

      "databases": {
        "web": { "host": "db.web.some.com", "port": "3306", "username": "myuser", "password": "mypass" },
        "office": { "host": "db.office.some.com", "port": "3306", "username": "myuser", "password": "mypass" }
      }
    }

#Usage examples
These examples will show you several different ways about how you can work with your JSON config files in shell with ease.
All examples use the sample config file above.


### Syntax
 1. `configo from config get key`
 2. `configo get key` //more info below

### Shell example in standard way
    # configo from /etc/myapp/config.json get application
    //-> My Application

### Shell example in standard way with `nested` properties
    # configo from /etc/myapp/config.json get webservers.api.host
    //-> api.some.com

### Shell scripts example in standard way
    TARGET_CONF="/etc/myapp/config.json";
    CONFIGO="configo from $TARGET_CONF";
    VARNAME=`$CONFIGO get databases.office.password`;
    echo $VARNAME;
    //-> mypass

### Lazy example
If you want you can assign the path to your config file to `CONFIGO_CONF` variable and `configo` will use it without having to define it as an sargument every time.

    export CONFIGO_CONF=`/etc/myapp/config.json`

    API_WEBSERVER_HOSTNAME=`configo get webservers.api.host`
    //-> api.some.com

    OFFICE_DB_HOST=`configo get databases.office.host`
    //-> db.office.some.com

# Installation

from source

    # git clone git@github.com:mignev/configo.git
    # cd configo
    # python setup.py install


with pip

    # pip install configo

# Testing
All tests are located in `tests` dir. They are 2 different test suites. One test suit for `configo api` and another for the `command line tool`.

So what should we do to run tests:

    cd tests
    ln -s ../configo configo
    ln -s ../bin bin

If you want to run `configo api` tests just run:

    python configo_tests.py

If you run `command line tool` tests you must do the following:

    export CONFIGO_CONF=`pwd`/fixtures/config.json # this is necessary to work tests with lazy syntax

... and after that just run:

    python configo_executable_tests.py

# TODO
- Add xml support
- Add yaml support

# CHANGELOG

### 1.1:

- add tests for api and command line tool
- refactor configo api and command line tool

#Copyright
Copyright (c) 2012 Marian Ignev. See LICENSE for further details.