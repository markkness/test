#!/home/mkness/epd/bin/python
'''
sincos_test.py - Unit tests for sincos calculation via recurrence.

This is intended to be run via nosetests.
'''

import math
import random
import numpy

import sincos

# Compare recurrence results to explicit trig formulas.

def sincos_compare_recur_trig(sc_recur, sc_trig):
    '''Return the sqrt(sum of squares) of the difference between recurrence and trig calculations.'''
    err = sc_recur - sc_trig
    errsqd = err * err
    errsum = errsqd.sum()
    errmag = math.sqrt (errsum)
    return errmag

def sincos_all_subtest(x, n, verbose=False, tol=1.0e-10):
    '''Test that the error in sincos_all() is <= tol.'''
    if verbose:
        print('Testing sincos(x=% -10g, n=%3d) ...' % (x, n)),
    # calculate with recurrence
    sc_r = sincos.sincos_calc_recur(x, n)
    # calculate with trig
    sc_t = sincos.sincos_calc_trig(x, n)
    # compare
    errmag = sincos_compare_recur_trig(sc_r, sc_t)
    if verbose:
        print('errmag = %g' % (errmag))
    ok = (errmag <= tol)
    assert ok

# Check that sin*sin + cos*cos = 1

def sincos_check_unit(sc, verbose=False, tol=1.0e-10):
    '''Check that sin*sin + cos*cos = 1 for each row, and return the sum of errors for all rows.'''
    shape = sc.shape
    if len (shape) != 2:
        # expecting 2d array
        assert False
    (nrows, ncols) = shape
    if ncols != 2:
        # expecting 2 columns, sin,cos
        assert False
    errsum = 0.0
    for irow in range(nrows):
        si = sc[irow, 0]
        ci = sc[irow, 1]
        one = si*si + ci*ci
        err = math.fabs (one - 1.0)
        errsum += err
        if err > tol:
            # error too large
            assert False
    return errsum

def sincos_check_unit_subtest(x, n, verbose=False, tol=1.0e-10):
    '''Return whether the error in sincos_all() is <= tol.'''
    if verbose:
        print('Testing sin*sin + cos*cos = 1 (x=% -10g, n=%3d) ...' % (x, n)),
    sc = sincos.sincos_calc_recur(x, n)
    errsum = sincos_check_unit(sc, verbose=verbose, tol=tol)
    if verbose:
        print('errsum = %g' % (errsum))

# Driver to run all tests for multiple cases

def subtest_init(seed=None):
    '''Setup for tests.'''
    random.seed(seed)

def subtest_1():
    '''Some specific test cases.'''
    x = 2.718281828
    #x = 0.01
    # calculate for n=1..3
    print('Calculations with recurrence formula...')
    sc3a = sincos.sincos_calc_recur(x, 3)
    sincos.sincos_print(x, 3, sc3a)
    print('Calculations with explicit trig...')
    sc3b = sincos.sincos_calc_trig(x, 3)
    sincos.sincos_print(x, 3, sc3b)
    # calculate for n=1..8
    print('Recurrence for n=1..8...')
    sc8 = sincos.sincos_calc_recur(x, 8)
    sincos.sincos_print(x, 8, sc8)
    # test case for n=1..8
    print('Test case for n=1..8...')
    sincos_all_subtest(x, 8, verbose=True)
    # s*s + c*c = 1 test
    sincos_check_unit(sc8, verbose=True)

# Drivers to run all test cases.
# The main driver is a generator that yields all the test cases.
# This is run by nosetests, or can be explicitly run via sim_nosetests.

def test_generator(m=10):
    '''Generator that produces test case function calls for nosetests.

    Each yielded result is a function plus its arguments.'''
    # setup - this is probably not quite the way to do this
    seed = None
    if True:
        # use fixed seed
        seed = 0xdeadbeef
    yield(subtest_init, seed)
    # fixed test cases
    yield(subtest_1,)
    # end after one?
    #return
    # test cases with varying arguments
    for i in range(m):
        # get random angle and max index
        x = random.uniform(-10.0, 10.0)
        n = random.randint(1, 100)
        # optional verbose and tolerance
        verbose = True
        tol = 1.0e-10
        # comparison against trig
        yield(sincos_all_subtest, x, n, verbose, tol)
        # check that sin*sin + cos*cos = 1
        yield(sincos_check_unit_subtest, x, n, verbose, tol)

def sim_nosetests(m=10):
    '''Call the test cases supplied by the generator test_generator.

    This duplicates the behavior of nosetests but can be run without it.'''
    good = 0
    fail = 0
    for i in test_generator(m):
        func = i[0]
        args = i[1:]
        try:
            func(*args)
            good += 1
        except:
            print('FAILURE...')
            fail += 1
            #raise
    print('Passed %d tests, Failed %d tests.' % (good, fail))
    
if __name__ == '__main__':
    sim_nosetests()
