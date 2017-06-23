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
LINKS = (
    ("📚archive", "/everything/"),
    ("📓blog", "/categories/blog/"),
    ("👨‍💻dev", "/categories/dev/"),
    ("🔗resources", "/resources/"),
    ("🤵🏻about", "/about/"),
    ("💻project", "/project/"),
    ("📌the source code", "https://github.com/fundor333/fundor333.com"),
    ("📰the feed", "https://fundor333.com/post/index.xml"),
)

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
PLUGINS = [
    'summary',
    'custom_article_urls',
]

CATEGORY_URL = 'categories/{slug}/'
CATEGORY_SAVE_AS = 'categories/{slug}/index.html'
ARTICLE_URL = 'post/{category}/{slug}/'
ARTICLE_SAVE_AS = 'post/{category}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
INDEX_SAVE_AS = 'everything/index.html'
INDEX_URL = 'everything/'

TEMPLATE_PAGES = {
    '../theme/templates/home.html': 'index.html',
}

HOME_TEXT = '''Chi sono? Sono un programmatore 💻 appasionato di Python 🐍, Docker 🐋 e del mondo Open Source.
Nel tempo libero cerco di migliorare il mondo, per quanto posso, supportando attività di volontariato e il mondo Open Source.
Ho un passato oscuro da PFY e qualche esperienza nel coordinare gruppi di viaggio e volontariato...

Questo vuole essere il mio spazio personale/bacheca publica/blog personale dove metto esperienza, progetti e idee... Insomma un diario di un informatico mai cresciuto.

Fundor333
'''

EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/.htaccess': {'path': '.htaccess'},
                       'extra/keybase.txt': {'path': 'keybase.txt'},
                       }
