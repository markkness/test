'''
sincos.py - Test program for git practice.
'''

import math

def sincos (x):
    '''Return (sin(x), cos(x)) as a tuple.'''
    s = math.sin (x)
    c = math.cos (x)
    rtn = (s, c)
    return rtn

def test ():
    '''Test driver.'''
    x = 2.718281828
    (s,c) = sincos (x)
    print ('sin (%g) = %g, cos (%g) = %g' % (
        x, s, x, c))

test ()
