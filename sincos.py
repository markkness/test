#!/home/mkness/epd/bin/python
'''
sincos.py - Calculates sin(n*x), cos(n*x) for n=1..N using recurrence formula.
'''

import math
import numpy

def sincos(x):
    '''Return (sin(x), cos(x)) as a tuple.'''
    s = math.sin(x)
    c = math.cos(x)
    rtn = (s, c)
    return rtn

def sincos_n(s_1, c_1, s_nm1, c_nm1):
    '''Return (sin (nx), cos (nx)) as a tuple using recurrence formula.

    Given:
        S1 = sin(x), C1 = cos(x), Sn-1 = sin((n-1)x), Cn-1 = cos((n-1)x),
    Calculate:
        Sn = Sn-1 * C1 + Cn-1 * S1
        Cn = Cn-1 * C1 - Sn-1 * S1
    This formula is based on the trig angle addition formulas.'''
    sn = s_nm1 * c_1 + c_nm1 * s_1
    cn = c_nm1 * c_1 - s_nm1 * s_1
    # uncomment line below to cause tests to fail
    ##cn = c_nm1 * c_1 + s_nm1 * s_1    # ERROR!!!
    rtn = (sn, cn)
    return rtn

def sincos_all(x, n):
    '''Calculate sin(m*x), cos(m*x) for m = 1..n, as a numpy array using recurrence.

    Returns numpy array rtn size (n, 2) where
        rtn[i,0] = sin((i+1)*x)
        rtn[i,1] = cos((i+1)*x)
    Thus the angle multiples 1..n map to rows 0..n-1,
    and the columns are sin, cos.'''
    rtn = numpy.empty((n, 2))
    (s1, c1) = sincos(x)
    rtn[0, 0] = s1
    rtn[0, 1] = c1
    for i in range(2, n+1):
        snm1 = rtn[i-2, 0]
        cnm1 = rtn[i-2, 1]
        (sn, cn) = sincos_n(s1, c1, snm1, cnm1)
        rtn[i-1, 0] = sn
        rtn[i-1, 1] = cn
    return rtn

def sincos_all_raw(x, n):
    '''Calculate sin(m*x), cos(m*x) for m = 1..n, as a numpy array, with explicit trig calls.

    This is intended as a test case for sincos_all() which should be more efficient.'''
    rtn = numpy.empty((n, 2))
    for i in range(1, n+1):
        th = i * x
        (sn, cn) = sincos(th)
        rtn[i-1, 0] = sn
        rtn[i-1, 1] = cn
    return rtn

def sincos_print(x, n, sc):
    '''Nicely formatted printout of the sin,cos array.'''
    for i in range(n):
        j = i + 1        # angle multiple
        sj = sc[i, 0]
        cj = sc[i, 1]
        print('sin(%2d*%g) = % -12g,    cos(%2d*%g) = % -12g' % (
            j, x, sj, j, x, cj))
