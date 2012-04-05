#!/home/mkness/epd/bin/python
'''
sincos_test.py - Unit tests for sincos calculation via recurrence.

This is intended to be run via nosetests.
'''

import math
import random
import numpy

import sincos

#
# Tests
#

# Compare recurrence results to explicit trig formulas.

def sincos_all_error(x, n):
    '''Return a numpy array with the difference sincos_all() - sincos_all_test().

    If sincos_all() is correct, then this array should be essentially zeros.'''
    sc_a = sincos.sincos_all(x, n)
    sc_b = sincos.sincos_all_raw(x, n)
    d_sc = sc_a - sc_b
    return d_sc

def sincos_all_errmag(x, n):
    '''Return the sqrt(sum of squares of error) from sincos_all_error().'''
    err = sincos_all_error(x, n)
    err = err * err
    errsum = err.sum()
    errmag = math.sqrt(errsum)
    return errmag

def sincos_all_subtest(x, n, verbose=False, tol=1.0e-10):
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

def sincos_check_unit_subtest(x, n, verbose=False, tol=1.0e-10):
    '''Return whether the error in sincos_all() is <= tol.'''
    sc = sincos.sincos_all(x, n)
    rtn = sincos_check_unit(sc, verbose=verbose, tol=tol)
    return rtn

# Driver to run all tests for multiple cases

def sincos_all_subtest_many(m, verbose=False, tol=1.0e-10):
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
        ok = sincos_all_subtest(x, n, verbose, tol)
        if ok:
            good += 1
        else:
            fail += 1
        # test for sin*sin + cos*cos = 1
        if verbose:
            print('Testing sin*sin + cos*cos = 1 (x=% -10g, n=%3d) ...' % (x, n)),
        ok = sincos_check_unit_subtest(x, n, verbose, tol)
        if ok:
            good += 1
        else:
            fail += 1
            
    if verbose:
        print('Passed %d tests, Failed %d tests.' % (good, fail))
    assert (fail == 0)
    rtn = (good, fail)
    return rtn
    
def test():
    '''Test driver.'''
    x = 2.718281828
    #x = 0.01
    # calculate for n=1..3
    sc3a = sincos.sincos_all(x, 3)
    sc3b = sincos.sincos_all_raw(x, 3)
    print('Calculations with recurrence formula...')
    sincos.sincos_print(x, 3, sc3a)
    print('Calculations with explicit trig...')
    sincos.sincos_print(x, 3, sc3b)
    # calculate for n=1..8
    sc8 = sincos.sincos_all(x, 8)
    print('Recurrence for n=1..8...')
    sincos.sincos_print(x, 8, sc8)
    # test case for n=1..8
    print('Test case for n=1..8...')
    sincos_all_error(x, 8)
    sincos_all_errmag(x, 8)
    ok = sincos_all_subtest(x, 8, verbose=True)
    print('ok = %s' % str(ok))
    # s*s + c*c = 1 test
    sincos_check_unit(sc8, verbose=True)
    # multiple test cases
    print('Multiple test cases...')
    sincos_all_subtest_many(10, verbose=True, tol=1.0e-10)
    
if __name__ == '__main__':
    test()
else:
    print('Not main.')

