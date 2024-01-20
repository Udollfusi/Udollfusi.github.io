#! /usr/bin/python
# -*- python -*-

import re, sys

def percent(c):
    return '%%%02X' % ord(c)

def ampersand(c):
    return '&#%03d;' % ord(c)

co = re.compile(r'[-._a-zA-Z0-9]')

outstr = ''
for c in sys.argv[1]:
    outstr = '%s%s' % (outstr, percent(c))

print outstr
