import sys
import logging

#Expand Python classes path with your app's path
sys.path.insert(0, "/var/www/FlaskApp")

from ItemCatalog import app as application
application.secret_key = 'super_secret_key'

