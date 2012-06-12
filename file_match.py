'''
Created on Jun 12, 2012

@author: Mark Kness

Compare files to see if they are exact matches.

'''

import os
import hashlib

def file_hash(filename):
    '''Return a printable SHA-1 hash of the contents of the file.'''
    with open(filename, 'rb') as f:
        data = f.read()
        m = hashlib.sha1()
        m.update(data)
        digest = m.hexdigest()
    return digest

def files_match(pathname1, pathname2):
    '''Are the two files the same?'''
    hash1 = file_hash(pathname1)
    hash2 = file_hash(pathname2)
    rtn = hash1 == hash2
    if rtn:
        print('Files %s, %s match ok' % (pathname1, pathname2))
    else:
        print('*** FAILURE *** Files %s, %s do NOT match' % (pathname1, pathname2))
    return rtn

def filelists_match(rootpath, nameslist, verbose=False):
    '''Compare a list of files.'''
    for name1, name2 in nameslist:
        pathname1 = os.path.join(rootpath, name1)
        pathname2 = os.path.join(rootpath, name2)
        if verbose:
            print 'Comparing {0:s} vs {1:s}...'.format(pathname1, pathname2)
        files_match(pathname1, pathname2)

def filelists_match_test():
    '''Debug test that only makes sense on mkness machine.'''
    #rootpath = r'c:\enthought\shell\CVX_ST_TTI'
    rootpath = r'c:\enthought\shell\CVX_ST_TTI\ref_shift'
    nameslist = [
        #('develop_ascii_1_1.tif', 'feature_ascii_1_1.tif'),
        #('develop_ascii_3_3.tif', 'feature_ascii_3_3.tif'),
        #('develop_ascii_1_1.tif', 'feature_int_1_1.tif'),
        #('develop_ascii_3_3.tif', 'feature_int_3_3.tif'),
        #('develop_ascii_1_1.tif', 'pickflag_intb_1_1.tif'),
        #
        #('filter_A_1.tif', 'filter_A_3.tif'),
        #('filter_0_1.tif', 'filter_0_3.tif'),
        #('filter_1_1.tif', 'filter_1_3.tif'),
        #('filter_2_1.tif', 'filter_2_3.tif'),
        #('filter_3_1.tif', 'filter_3_3.tif'),
        #('filter_4_1.tif', 'filter_4_3.tif'),
        #
        #('test_9.tif',  'new_9.tif'),
        #('test_-9.tif', 'new_-9.tif'),
        #
        #('shift_90.tif', 'shift_new_90.tif'),
        ('ref_shift_36.tif',  'ref_shift_array_36.tif'),
        ('ref_shift_-36.tif', 'ref_shift_array_-36.tif'),
    ]
    filelists_match(rootpath, nameslist)

if __name__ == '__main__':
    filelists_match_test()
    
    
