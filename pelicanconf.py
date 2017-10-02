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
    ("archive","archive", "/everything/"),
    ("book","blog", "/categories/blog/"),
    ("terminal","dev", "/categories/dev/"),
    ("paperclip","resources", "/resources/"),
    ("user","about", "/about/"),
    ("laptop","project", "/project/"),
    ("code","the source code", "https://github.com/fundor333/fundor333.com"),
    ("rss","the feed", "https://fundor333.com/post/index.xml"),
)

# Social widget
SOCIAL = (
    ('facebook', 'https://www.facebook.com/fundor333'),
    ("twitter", "https://twitter.com/fundor333"),
    ("youtube", "https://www.youtube.com/user/Fundor333"),
    ("instagram", "https://www.instagram.com/fundor333/"),
    ("flickr", "https://www.flickr.com/people/fundor333/"),
    ("reddit", "https://www.reddit.com/user/fundor333"),
    ("linkedin", "https://it.linkedin.com/in/matteo-scarpa-78969263"),
    ("github", "https://github.com/fundor333"),
    ("gitlab", "https://gitlab.com/fundor333"),
    ('codepen','https://codepen.io/fundor333/'),
)

DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'theme'
MARKUP = ('md', 'ipynb')
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', 'sitemap'
                     ))
SITEMAP_SAVE_AS = 'sitemap.xml'

PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    'custom_article_urls',
    'ipynb.markup',
    'feed_summary',
    'embed_tweet',
     'tipue_search',
]

FEED_USE_SUMMARY = True

IPYNB_USE_META_SUMMARY = True
IGNORE_FILES = ['.ipynb_checkpoints']
IPYNB_IGNORE_CSS = True

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

EXTRA_PATH_METADATA = {'extras/CNAME': {'path': 'CNAME'},
                       'extras/.htaccess': {'path': '.htaccess'},
                       'extras/keybase.txt': {'path': 'keybase.txt'},
                       }
