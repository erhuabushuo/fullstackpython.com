# -*- coding: utf-8 -*-

AUTHOR = u'何文祥'
SITENAME = u'全站式 Python'
SITEURL = 'https://www.fullstackpython.cn'
TIMEZONE = 'Asia/Shanghai'

GITHUB_URL = 'https://github.com/erhuabushuo/fullstackpython.cn'
DISQUS_SITENAME = 'makaimc'
PDF_GENERATOR = False

DIRECT_TEMPLATES = ('index', 'sitemap', 'table-of-contents', 'email',
                    'blog', 'all')

ARTICLE_SAVE_AS = 'blog/{slug}.html'

SITEMAP_SAVE_AS = 'sitemap.xml'

FEED_DOMAIN = 'https://www.fullstackpython.cn'
FEED_RSS = 'feed'

BYLINE = '&copy; 2016 Matt Makai. All Rights Reserved.'
LINKS = ()

MARKUP = ('rst', 'markdown',)

SOCIAL = (
    ('Email', 'mailto:erhuabushuo@gmail.com'),
    ('GitHub', 'https://github.com/erhuabushuo'),
    ('Twitter', 'http://twitter.com/mattmakai'),
)

PROJECTS = ()

JINJA_EXTENSIONS = (['jinja2.ext.autoescape',])
