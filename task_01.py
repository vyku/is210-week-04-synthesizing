#! usr/bin/env python
# _*_ coding: utf-8 _*_

""" A color comparison """


BASE = raw_input('Which base color, "Seatle Gray" or "Manatee"?:' )
ACCENT = raw_input('Which accent color", "Platinum Mist" or "Spartum Sage"?:')
HIGHLIGHT = raw_input('Which high color," Fractical white" or "Not white"?: ')

RETSTR = ('{},{},{}')
print 'Your selected colors are {}' + RETSTR.format(BASE, ACCENT ,HIGHLIGHT)


