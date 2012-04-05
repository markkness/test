#!/home/mkness/epd/bin/python
'''
sincos.py - Test program for git practice.

Calculates sin(n*x), cos(n*x) for n=1..N using recurrence formula.
'''

import math
import random
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

#
# Nicely formatted printout of sin/cos array
#

def sincos_print(x, n, sc):
    '''Nicely print the sin,cos values.'''
    for i in range(n):
        j = i + 1        # angle multiple
        sj = sc[i, 0]
        cj = sc[i, 1]
        print('sin(%2d*%g) = % -12g,    cos(%2d*%g) = % -12g' % (
            j, x, sj, j, x, cj))

#
# Tests
#

# Calculate also with explicit trig formulas and compare to recurrence.

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

def sincos_all_error(x, n):
    '''Return a numpy array with the difference sincos_all() - sincos_all_test().

    If sincos_all() is correct, then this array should be essentially zeros.'''
    sc_a = sincos_all(x, n)
    sc_b = sincos_all_raw(x, n)
    d_sc = sc_a - sc_b
    return d_sc

def sincos_all_errmag(x, n):
    '''Return the sqrt(sum of squares of error) from sincos_all_error().'''
    err = sincos_all_error(x, n)
    err = err * err
    errsum = err.sum()
    errmag = math.sqrt(errsum)
    return errmag

def sincos_all_test(x, n, verbose=False, tol=1.0e-10):
    '''Return whether the error in sincos_all() is <= tol.'''
    errmag = sincos_all_errmag(x, n)
    if verbose:
        print('errmag = %g' % (errmag))
    ok = (errmag <= tol)
    return ok

# Check that sin*sin + cos*cos = 1

def sincos_check_unit(sc, verbose=False, tol=1.0e-10):
    '''Check that sin*sin + cos*cos = 1 for each row.'''
    shape = sc.shape
    if len (shape) != 2:
        # expecting 2d array
        return False
    (nrows, ncols) = shape
    if ncols != 2:
        # expecting 2 columns, sin,cos
        return False
    errsum = 0.0
    for irow in range(nrows):
        si = sc[irow, 0]
        ci = sc[irow, 1]
        one = si*si + ci*ci
        err = math.fabs (one - 1.0)
        errsum += err
        if err > tol:
            # error too large
            return False
    if verbose:
        print('errsum = %g' % (errsum))
    # all checks passed
    return True

def sincos_check_unit_test(x, n, verbose=False, tol=1.0e-10):
    '''Return whether the error in sincos_all() is <= tol.'''
    sc = sincos_all(x, n)
    rtn = sincos_check_unit(sc, verbose=verbose, tol=tol)
    return rtn

# Driver to run all tests for multiple cases

def sincos_all_test_many(m, verbose=False, tol=1.0e-10):
    '''Run m tests and return the count of success, failure as a tuple.'''
    random.seed()
    good = 0
    fail = 0
    for i in range(m):
        # get random angle and max index
        x = random.uniform(-10.0, 10.0)
        n = random.randint(1, 100)
        # test against explicit trig calls
        if verbose:
            print('Testing sincos(x=% -10g, n=%3d) ...' % (x, n)),
        ok = sincos_all_test(x, n, verbose, tol)
        if ok:
            good += 1
        else:
            fail += 1
        # test for sin*sin + cos*cos = 1
        if verbose:
            print('Testing sin*sin + cos*cos = 1 (x=% -10g, n=%3d) ...' % (x, n)),
        ok = sincos_check_unit_test(x, n, verbose, tol)
        if ok:
            good += 1
        else:
            fail += 1
            
    if verbose:
        print('Passed %d tests, Failed %d tests.' % (good, fail))
    rtn = (good, fail)
    return rtn
    
def test():
    '''Test driver.'''
    x = 2.718281828
    #x = 0.01
    # calculate for n=1..3
    sc3a = sincos_all(x, 3)
    sc3b = sincos_all_raw(x, 3)
    print('Calculations with recurrence formula...')
    sincos_print(x, 3, sc3a)
    print('Calculations with explicit trig...')
    sincos_print(x, 3, sc3b)
    # calculate for n=1..8
    sc8 = sincos_all(x, 8)
    print('Recurrence for n=1..8...')
    sincos_print(x, 8, sc8)
    # test case for n=1..8
    print('Test case for n=1..8...')
    sincos_all_error(x, 8)
    sincos_all_errmag(x, 8)
    ok = sincos_all_test(x, 8, verbose=True)
    print('ok = %s' % str(ok))
    # s*s + c*c = 1 test
    sincos_check_unit(sc8, verbose=True)
    # multiple test cases
    print('Multiple test cases...')
    sincos_all_test_many(10, verbose=True, tol=1.0e-10)
    
test()

