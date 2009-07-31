#    OpenProximity2.0 is a proximity marketing OpenSource system.
#    Copyright (C) 2009,2008 Naranjo Manuel Francisco <manuel@aircable.net>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation version 2 of the License.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
# Django settings for openproximity2.0
import os
from pluginsystem import pluginsystem

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

if os.path.isfile('/etc/openproximity2.conf'):
    inp = file('/etc/openproximity2.conf')
    for line in inp.readlines():
	if line.startswith('AIRCABLE_PATH'):
	    AIRCABLE_PATH=line.split('=', 1)[1].strip()
	    break
else:
    AIRCABLE_PATH='/tmp'

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = "%s/aircable.db" % AIRCABLE_PATH   # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '%s/aircable' % AIRCABLE_PATH

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'c%-hx%#@jh4)_zlbqco+v9lm6s0xgi%)vzs-qrbkn)_#ef@7!h'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'urls'

my_path=os.path.dirname(__file__)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(my_path, 'templates'),
    os.path.join(my_path, 'bluez', 'templates'),
    os.path.join(my_path, 'openproximity', 'templates'),
)

LOCALE_PATHS=(
    os.path.join(my_path, 'locale'),
    os.path.join(my_path, 'bluez', 'locale'),
    os.path.join(my_path, 'openproximity', 'locale'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.databrowse',
    'bluez',
    'openproximity',    
)

pluginsystem.find_plugins()
for plugin in pluginsystem.get_plugins():
    if plugin.provides.get('django', False) is False:
	continue
    
    if plugin.provides.get('TEMPLATE_DIRS', None) is not None :
	print plugin.name, "Provides templates"
	TEMPLATE_DIRS += ( os.path.join(plugin.__path__[0], plugin.provides['TEMPLATE_DIRS']), )
    if plugin.provides.get('LOCALE_PATHS', None) is not None:
	print plugin.name, "Provides locales"
	LOCALE_PATHS += ( os.path.join(plugin.__path__[0], plugin.provides['LOCALE_PATHS']), )
    if plugin.provides.get('INSTALLED_APPS', None) is not None:
	print plugin.name, "Provides applications"
	INSTALLED_APPS += ( '%s.%s.%s' % ('plugins', plugin.name, plugin.provides['INSTALLED_APPS']), )