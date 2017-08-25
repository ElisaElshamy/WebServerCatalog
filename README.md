# About

Video Game Catalog allows users to log in using their Google account to contribute to 
a catalog of video games.  Video Games are categorized by genre.  Box art upload is not 
available in this version and will be added at a later time.

# Install

Go to your browser and visit http://ec2-34-205-92-238.compute-1.amazonaws.com/ to see the 
home page and login.

# How to use

Click the Google Sign-in button to log in using an existing Google account or to create one.
This credential is what will allow you to add genres and video games accordingly.
You must allow this site to access your Google account.  This site collects your
Google email address, Google user ID, Google profile picture, name and username as it is saved in
Google.  Information used on this site is secure and will not be used in any way other than
protecting the data you enter on this site.

# Development

Video Game Catalog is a Python project that uses Flask and SQLAlchemy.  Authentication is 
secured using oauth 2.0 and Google's services.

Video Game Catalog is hosted on an Amazon Lightsail server installed with Ubuntu.  To 
configure the app to be served via Apache's mod_wsgi a .wsgi file was created.  This file
is located in the /FlaskApp directory and contains the following contents:

```
import sys
import logging

#Expand Python classes path with your app's path
sys.path.insert(0, "/var/www/FlaskApp")

from ItemCatalog import app as application
application.secret_key = 'super_secret_key'
``` 

Where ```ItemCatalog``` is the directory inside FlaskApp containing the app's files.
The main python file must be renamed to ```__init__.py```

Then in the ```/etc/apache2/sites-available/catalog.conf``` file the following was added:

```
<VirtualHost *:80>
                ServerName mywebsite.com
                ServerAdmin admin@mywebsite.com
                WSGIScriptAlias / /var/www/FlaskApp/catalog.wsgi
                <Directory /var/www/FlaskApp/>
                        Order allow,deny
                        Allow from all
                </Directory>
                ErrorLog ${APACHE_LOG_DIR}/error.log
                LogLevel warn
                CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

Then the default .conf was disabled and the catalog.conf file was enabled using:
```
sudo a2dissite 000-default.conf
sudo a2ensite catalog.conf
```
Apache was then set to restart using: 

```sudo apache2ctl restart```


## Libraries & Software

- **Python 2.7.12**
- **Flask 0.9** - http://flask.pocoo.org
- **SQLAlchemy 1.1.11** - http://www.sqlalchemy.org
- **OAuth 2.0 Client** - http://github.com/google/oauth2client
- **Amazon Lightsail** - https://amazonlightsail.com/
- **Apache** - https://www.apache.org/
- **mod_wsgi** - https://modwsgi.readthedocs.io/en/develop/
- **PostgreSQL** - https://www.postgresql.org/
