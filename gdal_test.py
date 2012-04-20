'''
gdal_test.py - Test program for exploring GDAL.
'''

import numpy

import gdal
from gdalconst import *

def gdal_test_exist(filename):
    access = GA_ReadOnly
    #access = GA_Update
    dataset = gdal.Open(filename, access)
    if dataset is None:
        print('dataset is none')
    else:
        print('EXISTS DATASET!!!')

def gdal_test_3():
    data = test_data_1()
    write_geotiff('gdal_test.tiff', data)

def gdal_test_2():
    data = test_data_2()
    write_geotiff('gdal_test_2.tiff', data)

def test_data_1():
    '''Get some test data to write as a GeoTIFF file.'''
    shape = (256, 256, 3)
    dummy_data = numpy.zeros(shape, dtype=numpy.uint8)
    dummy_data[:,:,0].fill(200)
    dummy_data[:,:,1].fill(0)
    dummy_data[:,:,2].fill(100)
    for i in range(256):
        #dummy_data[i,:,0] = 255 - i
        dummy_data[i,:,0] = i
    return dummy_data

def test_data_2():
    '''Get some test data to write as a GeoTIFF file.'''
    shape = (512, 512, 3)
    dummy_data = numpy.zeros(shape, dtype=numpy.uint8)
    dummy_data[:,:,0].fill(200)
    dummy_data[:,:,1].fill(125)
    dummy_data[:,:,2].fill(10)
    for i in range(256):
        #dummy_data[i,:,0] = 255 - i
        dummy_data[i,:,0] = i
    return dummy_data


def write_geotiff(filename, dataset):
    '''Write the data in dataset as a GeoTIFF file.

    filename is the output filename.
    dataset  is the data to write. It should be 3D with the first two dims the image size,
             and the third dimension 3 with each index representing red, green, blue.
    '''
    shape = dataset.shape
    nx, ny, nbands = shape
    assert nbands == 3, 'GeoTIFF data must be 3D for red,green,blue.'
    driver = gdal.GetDriverByName('GTiff')
    out_ds = driver.Create(filename, nx, ny, nbands, gdal.GDT_Byte)
    for i in range(nbands):
        out_band = out_ds.GetRasterBand(i + 1)
        out_band.WriteArray(dataset[:,:,i])

def main():
    print('GDAL test.')
    gdal_test_2()
    gdal_test_3()
    gdal_test_exist('gdal_test.tiff')

if __name__ == '__main__':
    main()

    
