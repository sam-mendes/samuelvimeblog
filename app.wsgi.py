#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApp/")

from samuelvimeblog import samuelvimeblog as application
application.secret_key = 'Add your secret key'
