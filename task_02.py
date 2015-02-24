#! usr/bin/env python
# _*_ coding: utf-8 _*_

""" Alaram file """
ALARAM = False 
DAY=raw_input('What day is it?:').upper
TIME=int(raw_input('What time is it(plese enter as four digit)?:')))


SNOOZE = False if DAY is 'SAT' or 'SUN' and TIME < 0600 else True 

print 'BEEP!BEEP!BEEP!'.format(SNOOZE)




