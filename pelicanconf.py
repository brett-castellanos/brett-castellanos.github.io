#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


# AUTHOR = 'Brett Castellanos'
# SITENAME = 'Data Science Blog'
SITEURL = 'https://brett-castellanos.github.io'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = '/Users/brettcastellanos/projects/pelican-themes/Flex'
SITE_TITLE = 'Data Science Blog'
SITE_SUBTITLE = 'By Brett Castellanos'
SITELOGO = 'https://avatars2.githubusercontent.com/u/37988637?s=400&u=e7cb1181485f65bb4885ef38350bb3b12d35c6eb&v=4'

MAIN_MENU = True
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

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

# if you create jupyter files in the content dir, snapshots are saved with the same
# metadata. These need to be ignored.
IGNORE_FILES = [".ipynb_checkpoints"]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
