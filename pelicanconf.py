#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Basic Settings
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'post'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
# DOCUTILS_SETTINGS = {}
DELETE_OUTPUT_DIRECTORY = False
# OUTPUT_RETENTION = []
# JINJA_ENVIRONMENT = {'trim_blocks': True, 'lstrip_blocks': True}
# JINJA_FILTERS = {}
# LOG_FILTER = []
# READERS = {}
IGNORE_FILES = [".ipynb_checkpoints", '__pycache__']
# MARKDOWN = {}
# OUTPUT_PATH = 'output/'
PATH = 'content'
PAGE_PATHS = ['pages']
# PAGES_EXCLUDES = []
ARTICLE_PATHS = ['blog', 'portfolio']
# ARTICLE_EXCLUDES = []
# OUTPUT_SOURCES = False
# OUTPUT_SOURCES_EXTENSION = '.text'
PLUGINS = ['ipynb.markup']
PLUGIN_PATHS = ['./plugins']
MARKUP = ('md', 'ipynb')
SITENAME = 'Data Science Blog'
SITEURL = 'http://localhost:8000'
STATIC_PATHS = ['images', 'static']
# STATIC_EXCLUDES = []
# # STATIC_EXCLUDE_SOURCES = True
# STATIC_CREATE_LINKS = False
# STATIC_CHECK_IF_MODIFIED = False
# TYPOGRIFY = False
# TYPOGRIFY_IGNORE_TAGS = []
# SUMMARY_MAX_LENGTH = 50
# WITH_FUTURE_DATES = True
# INTRASITE_LINK_REGEX = '[{|](?P<what>.*?)[|}]'
# PYGMENTS_RST_OPTIONS = []
# SLUGIFY_SOURCE = 'title'
# CACHE_CONTENT = False
# CONTENT_CACHING_LAYER = 'reader'
# CACHE_PATH = 'cache'
# GZIP_CACHE = True
# CHECK_MODIFIED_METHOD = 'mtime'
# LOAD_CONTENT_CACHE = False
# WRITE_SELECTED = []
# FORMATTED_FIELDS = ['summary']
# PORT = 8000
# BIND = ''

# URL settings
# RELATIVE_URLS = False
# ARTICLE_URL = '{date:%Y}/{slug}.html'
# ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
# ARTICLE_LANG_URL = '{slug}-{lang}.html'
# ARTICLE_LANG_SAVE_AS = '{slug}-{lang}.html'
# DRAFT_URL = 'drafts/{slug}.html'
# DRAFT_SAVE_AS = 'drafts/{slug}.html'
# DRAFT_LANG_URL = 'drafts/{slug}-{lang}.html'
# DRAFT_LANG_SAVE_AS = 'drafts/{slug}-{lang}.html'
# PAGE_URL = 'pages/{slug}.html'
# PAGE_SAVE_AS = 'pages/{slug}.html'
# PAGE_LANG_URL = 'pages/{slug}-{lang}.html'
# PAGE_LANG_SAVE_AS = 'pages/{slug}-{lang}.html'
# DRAFT_PAGE_URL = 'drafts/pages/{slug}.html'
# DRAFT_PAGE_SAVE_AS = 'drafts/pages/{slug}.html'
# DRAFT_PAGE_LANG_URL = 'drafts/pages/{slug}-{lang}.html'
# DRAFT_PAGE_LANG_SAVE_AS = 'drafts/pages/{slug}-{lang}.html'
# AUTHOR_URL = 'author/{slug}.html'
# AUTHOR_SAVE_AS = 'author/{slug}.html'
# CATEGORY_URL = 'category/{slug}.html'
# CATEGORY_SAVE_AS = 'category/{slug}.html'
# TAG_URL = 'tag/{slug}.html'
# TAG_SAVE_AS = 'tag/{slug}.html'
# YEAR_ARCHIVE_URL = ''
# YEAR_ARCHIVE_SAVE_AS = ''
# MONTH_ARCHIVE_URL = ''
# MONTH_ARCHIVE_SAVE_AS = ''
# DAY_ARCHIVE_URL = ''
# DAY_ARCHIVE_SAVE_AS = ''
# ARCHIVES_SAVE_AS = 'archives.html'
# AUTHORS_SAVE_AS = 'authors.html'
# CATEGORIES_SAVE_AS = 'categories.html'
# TAGS_SAVE_AS = 'tags.html'
# INDEX_SAVE_AS = 'index.html'
# SLUG_REGEX_SUBSTITUTIONS = [
#     (r'[^\w\s-]', ''), # remove non-alphabetical/whitespace/'-' chars
#     (r'(?u)\A\s*', ''), # strip leading whitespace
#     (r'(?u)\s*\Z', ''), # strip trailing whitespace
#     (r'[-\s]+', '-'), # reduce multiple whitespace or '-' to single '-'
# ]
# AUTHOR_REGEX_SUBSTITUTIONS = SLUG_REGEX_SUBSTITUTIONS
# CATEGORY_REGEX_SUBSTITUTIONS = SLUG_REGEX_SUBSTITUTIONS
# TAG_REGEX_SUBSTITUTIONS = SLUG_REGEX_SUBSTITUTIONS

# Time and Date Options
TIMEZONE = 'America/Los_Angeles'
# DEFAULT_DATE = 'fs'
# DEFAULT_DATE_FORMAT = '%a %d %B %Y'
# # DATE_FORMATS = {}
DEFAULT_LANG = 'en'
# LOCALE = 'en_US'

# Template Pages
# TEMPLATE_PAGES = None
# TEMPLATE_EXTENSIONS = ['.html']
# DIRECT_TEMPLATES = [
#     'index', 'authors', 'categories', 'tags', 'archives'
# ]

# Metadata
AUTHOR = 'Brett Castellanos'
# DEFAULT_METADATA = {}
# FILENAME_METADATA = r'(?P<date>d{4}-d{2}-d{2}).*'
# PATH_METADATA = ''
# EXTRA_PATH_METADATA = {
#     'extra/custom.css': {'path': 'static/custom.css'},
# }
# Set in Flex Theme Custom Settings

# Feed Settings
# FEED_DOMAIN = None
# FEED_ATOM = None
# FEED_ATOM_URL = None
# FEED_RSS = None
# FEED_RSS_URL = None
# FEED_ALL_ATOM = 'feeds/all.atom.xml'
# FEED_ALL_ATOM_URL = None
# FEED_ALL_RSS = None
# FEED_ALL_RSS_URL = None
# CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
# CATEGORY_FEED_ATOM_URL = None
# CATEGORY_FEED_RSS = None
# CATEGORY_FEED_RSS_URL = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = 'feeds/{slug}.rss.xml'
# AUTHOR_FEED_RSS_URL = None
# TAG_FEED_ATOM = None
# TAG_FEED_ATOM_URL = None
# TAG_FEED_RSS = None
# FEED_MAX_ITEMS - Unrestricted by default
RSS_FEED_SUMMARY_ONLY = True

# Pagination
# DEFAULT_ORPHANS = 0
DEFAULT_PAGINATION = 10
# PAGINATED_TEMPLATES = {
#      'index': None, 'tag': None,
#      'category': None, 'author': None
# }


# Tranlations
# DEFAULT_LANG = 'en'
# ARTICLE_TRANSLATION_ID = 'slug'
# PAGE_TRANSLATION_ID = 'slug'
# TRANSLATION_FEED_ATOM = 'feeds/all-{lang}.atom.xml'
# TRANSLATION_FEED_ATOM_URL = None
# TRANSLATION_FEED_RSS = None
# TRANSLATION_FEED_RSS_URL = None

# Ordering Content
NEWEST_FIRST_ARCHIVES = True
REVERSE_CATEGORY_ORDER = False
ARTICLE_ORDER_BY = 'reversed-date'
PAGE_ORDER_BY = 'basename'

# Themes
THEME = 'Flex'
THEME_STATIC_DIR = 'theme'
THEME_STATIC_PATHS = ['static']
# THEME_TEMPLATES_OVERRIDES = []
CSS_FILE = 'main.css'
# SITESUBTITLE = '' - Set in Flex Theme Settings
# DISQUS_SITENAME = 
GITHUB_URL = 'https://www.github.com/brett-castellanos'
# GOOGLE_ANALYTICS = 
# GA_COOKIE_DOMAIN = 
# GOSQUARED_SITENAME
MENUITEMS = (
    ('Archives', '/archives.html'),
    ('Categories', '/categories.html'),
    ('Tags', '/tags.html'),
)
# PIWIK_URL
# PIWIK_SSL_URL
# PIWIK_SITE_ID
# LINKS = (
#   ('a link', 'an url' )
# )
SOCIAL = (
    ('linkedin', 'https://www.linkedin.com/in/brett-castellanos'),
    ('github', 'https://www.github.com/brett-castellanos'),
)
TWITTER_USERNAME = 'bcas1984'
# LINKS_WIDGET_NAME = 
# SOCIAL_WIDGET_NAME =

# Logging
# import logging
# LOG_FILTER = []

# FLEX THEME CUSTOM SETTINGS
SITETITLE = 'Data Science Blog'
SITESUBTITLE = 'Brett Castellanos'
SITELOGO = SITEURL + '/images/profile.png'
SITEDESCRIPTION = 'My Data Science Blog'
BROWSER_COLOR = '#333'
OG_LOCALE = 'en_US'
COPYRIGHT_NAME = 'Brett Castellanos'
COPYRIGHT_YEAR = 2019
CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-brett-castellanos'
}
ROBOTS = 'index, follow'
HOME_HIDE_TAGS = False
DISABLE_URL_HASH = True
PAGES_SORT_ATTRIBUTE = 'title'
MAIN_MENU = True
# MENUITEMS - SET ABOVE
# LINKS - SET ABOVE
# SOCIAL - SET ABOVE
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}
CUSTOM_CSS = 'static/custom.css'
USE_LESS = False
FAVICON = SITEURL + '/images/favicon.ico'
# PYGMENTS_STYLE
ARTICLE_HIDE_TRANSLATION = False
LINKS_IN_NEW_TAB = 'external'
