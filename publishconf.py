#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = ''
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/feed.xml'
CATEGORY_FEED_ATOM = 'feeds/category/%s.xml'
TAG_FEED_ATOM = 'feeds/tag/%s.xml'
AUTHOR_FEED_ATOM = 'feeds/%s.rss.xml'
FEED_MAX_ITEMS = 15

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "fundor333"
#GOOGLE_ANALYTICS = ""
