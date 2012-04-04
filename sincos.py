'''
sincos.py - Test program for git practice.
'''

import math
import numpy

def sincos (x):
    '''Return (sin(x), cos(x)) as a tuple.'''
    s = math.sin (x)
    c = math.cos (x)
    rtn = (s, c)
    return rtn

def sincos_n (s_1, c_1, s_nm1, c_nm1):
    '''Calculate sin (nx), cos (nx) from sin (x), cos (x), sin ((n-1)x), cos ((n-1)x).'''
    sn = s_nm1 * c_1 + c_nm1 * s_1
    cn = c_nm1 * c_1 - s_nm1 * s_1
    rtn = (sn, cn)
    return rtn

def sincos_all (x, n):
    '''Calculate sin(m*x), cos (m*x) for m = 1..n'''
    rtn = numpy.empty ((n, 2))
    # rtn [i,0] = sin ((i+1)*x)
    # rtn [i,1] = cos ((i+1)*x)
    (s1, c1) = sincos (x)
    rtn [0, 0] = s1
    rtn [0, 1] = c1
    for i in range (2, n + 1):
        snm1 = rtn [i-2, 0]
        cnm1 = rtn [i-2, 1]
        (sn, cn) = sincos_n (s1, c1, snm1, cnm1)
        rtn [i-1, 0] = sn
        rtn [i-1, 1] = cn
    return rtn

def test ():
    '''Test driver.'''
    x = 2.718281828
    x = 0.01
    (s1,c1) = sincos (x)
    print ('sin (%d * %g) = %g, cos (%g) = %g' % (
        1, x, s1, x, c1))
    (s2,c2) = sincos_n (s1, c1, s1, c1)
    print ('sin (%d * %g) = %g, cos (%g) = %g' % (
        2, x, s2, x, c2))
    (s3,c3) = sincos_n (s1, c1, s2, c2)
    print ('sin (%d * %g) = %g, cos (%g) = %g' % (
        3, x, s3, x, c3))
    scn = sincos_all (x, 8)
    print 'scn=', scn

test ()
