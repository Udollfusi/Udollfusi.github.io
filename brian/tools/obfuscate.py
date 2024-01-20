#! /usr/bin/python
# -*- python -*-

import sys, whrandom

def percent(c):
    return '%%%02X' % ord(c)

def ampersand(c):
    return '&#%03d;' % ord(c)

gen = whrandom.whrandom()

outstr = ''
for c in sys.argv[1]:
    if c == '@':
        outstr = '%s%s' % (outstr, ampersand(c))
    else:
        outstr = '%s%s' % (outstr, gen.choice((c, ampersand(c))))

print outstr
