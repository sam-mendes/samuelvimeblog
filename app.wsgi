#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/samuelvimeblog/")

from samuelvimeblog import app as application
application.app.secret_key = 'Add your secret key'
