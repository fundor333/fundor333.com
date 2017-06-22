#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Fundor333'
SITENAME = 'Fundor 333 💻'
SITESUBTITLE = 'import antigravity'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'it'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
    ('facebook', 'https://www.facebook.com/fundor333'),
    ("mastodon", "https://mastodon.social/@fundor333"),
    ("twitter", "https://twitter.com/fundor333"),
    ("youtube", "https://www.youtube.com/user/Fundor333"),
    ("instagram", "https://www.instagram.com/fundor333/"),
    ("reddit", "https://www.reddit.com/user/fundor333"),
    ("linkedin", "https://it.linkedin.com/in/matteo-scarpa-78969263"),
    ("github", "https://github.com/fundor333"),
    ("gitlab", "https://gitlab.com/fundor333"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'theme'

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["tag_cloud"]