###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###


import sys

VERSION = (1, 9, 8, 'alpha', 2)

if VERSION[3] and VERSION[4]:
    VERSION_TEXT = '{0}.{1}.{2}{3}{4}'.format(*VERSION)
else:
    VERSION_TEXT = '{0}.{1}.{2}'.format(*VERSION[0:3])

VERSION_EXTRA = ''
LICENSE = 'GPL3'
EDITION = ''  # Added in package names, after the version
KEYWORDS = "mvc, oop, module, python, framework, web, app"

PYVERSION_MA = sys.version_info.major
PYVERSION_MI = sys.version_info.minor


MIME_TYPES = [
    {"ext": ".html", "type": "text/html", "mode": "r"},

    {"ext": ".txt", "type": "text/plain", "mode": "r"},

    {"ext": ".jpg", "type": "image/jpg", "mode": "rb"},

    {"ext": ".jpeg", "type": "image/jpeg", "mode": "rb"},

    {"ext": ".mp4", "type": "audio/mp4", "mode": "rb"},

    {"ext": ".rtf", "type": "text/rtf", "mode": "r"},

    {"ext": ".zip", "type": "application/zip", "mode": "rb"},

    {"ext": ".gif", "type": "image/gif", "mode": "rb"},

    {"ext": ".png", "type": "image/png", "mode": "rb"},

    {"ext": ".js", "type": " 'application/javascript", "mode": "r"},

    {"ext": ".css", "type": "text/css", "mode": "r"},

    {"ext": ".ttf", "type": "application/x-font-ttf", "mode": "rb"},

    {"ext": ".woff2", "type": "application/x-font-woff2", "mode": "rb"},

    {"ext": ".woff", "type": "application/x-font-woff", "mode": "rb"},

    {"ext": ".wav", "type": "audio/wav", "mode": "rb"},

    {"ext": ".svg", "type": "image/svg+xml", "mode": "rb"},

    {"ext": ".xml", "type": "application/xml", "mode": "rb"},

    {"ext": ".xhtml", "type": "application/xhtml+xml", "mode": "rb"},

    {"ext": ".xht", "type": "application/xhtml+xml", "mode": "rb"},

    {"ext": ".mpe", "type": "audio/mpeg", "mode": "rb"},

    {"ext": ".mp3", "type": "audio/mpeg", "mode": "rb"},

    {"ext": ".mpeg", "type": "audio/mpeg", "mode": "rb"},

    {"ext": ".json", "type": "application/json", "mode": "rb"}
]
