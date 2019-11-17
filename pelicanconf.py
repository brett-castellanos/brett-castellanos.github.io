#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = 'Flex'

PATH = 'content'
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'
STATIC_PATHS = ['images']
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

DEFAULT_LANG = 'en'
TIMEZONE = 'America/Los_Angeles'

AUTHOR = 'Brett Castellanos'
SITEURL = 'https://brett-castellanos.github.io'
SITENAME = 'Data Science Blog'
SITETITLE = 'Data Science Blog'
SITESUBTITLE = 'By Brett Castellanos'
SITEDESCRIPTION = 'My Portfolio'
SITELOGO = SITEURL + '/images/profile.png'
FAVICON = SITEURL + '/images/favicon.ico'

BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-brett-castellanos'
}
COPYRIGHT_YEAR = 2019

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}
CUSTOM_CSS = 'static/custom.css'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MAIN_MENU = True

LINKS_IN_NEW_TAB = 'external'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/brett-castellanos'),
         ('github', 'https://www.github.com/brett-castellanos'),)

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

DEFAULT_PAGINATION = 10

MARKUP = ('md', 'ipynb')



# if you create jupyter files in the content dir, snapshots are saved with the same
# metadata. These need to be ignored.
IGNORE_FILES = [".ipynb_checkpoints"]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
