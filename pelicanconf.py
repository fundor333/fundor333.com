#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Fundor333'
SITENAME = u'Fundor 333'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'Italian'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('facebook', 'https://www.facebook.com/fundor333'),
          ('twitter', 'https://twitter.com/fundor333'),
          ('linkedin', 'https://it.linkedin.com/in/matteo-scarpa-78969263'),
          ('github', 'https://github.com/fundor333'),
          ('gitlab', 'https://gitlab.com/fundor333'),)

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Specify theme

THEME = "theme"

# Specify the plugins

PLUGIN_PATHS = ["pelican-plugins.git"]
PLUGINS = ['tag_cloud',
           'custom_article_urls']

# For the landing page
TEMPLATE_PAGES = {
    '../theme/templates/home.html': 'index.html',
}
