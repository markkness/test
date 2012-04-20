'''
gdal_test.py - Test program for exploring GDAL.
'''

import numpy

import gdal
from gdalconst import *

def gdal_test_1():
    filename = 'gdal_test.tiff'
    #access = GA_ReadOnly
    access = GA_Update
    dataset = gdal.Open(filename, access)
    if dataset is none:
        print('dataset is none')
    else:
        print('EXISTS DATASET!!!')

def gdal_test_2():
    filename = 'gdal_test_2.tiff'
    driver = gdal.GetDriverByName('GTiff')
    # make up some data
    shape = (256, 256, 3)
    dummy_data = numpy.zeros(shape, dtype=numpy.float32)
    dummy_data.fill (0.5)
    if False:
        for i in range(shape[0]):
            f = float(i) / float(shape[0])
            print('i = %d, f = %g' % (i, f))
            dummy_data[i,:] = f
    print dummy_data

    dd_r = numpy.zeros((256, 256), dtype=numpy.uint8)
    dd_g = numpy.zeros((256, 256), dtype=numpy.uint8)
    dd_b = numpy.zeros((256, 256), dtype=numpy.uint8)

    dd_r.fill (200)
    dd_g.fill (0)
    dd_b.fill (100)
    for i in range(256):
        dd_r[i,:] = i

    
    # create output file
    #dst_ds = driver.Create(filename, shape[0], shape[1], 3, gdal.GDT_Float32)
    #dst_ds = driver.Create(filename, shape[0], shape[1], 1, gdal.GDT_Float32)
    #dst_ds = driver.Create(filename, shape[0], shape[1], 3, gdal.GDT_UInt16)
    dst_ds = driver.Create(filename, shape[0], shape[1], 3, gdal.GDT_Byte)
    # Write raster data sets
    if False:
        for i in range(3):
        #for i in range(1):
            outBand = dst_ds.GetRasterBand(i + 1)
            #outBand.WriteArray(data[i])
            outBand.WriteArray(dummy_data[:,:,i])
    out_r = dst_ds.GetRasterBand(1)
    out_r.WriteArray(dd_r)
    out_g = dst_ds.GetRasterBand(2)
    out_g.WriteArray(dd_g)
    out_b = dst_ds.GetRasterBand(3)
    out_b.WriteArray(dd_b)
    print('Test complete.')

def gdal_test():
    filename = 'gdal_test.tiff'
    driver = gdal.GetDriverByName('GTiff')
    # make up some data
    shape = (256, 256, 3)
    dummy_data = numpy.zeros(shape, dtype=numpy.uint8)
    dummy_data[:,:,0].fill(200)
    dummy_data[:,:,1].fill(0)
    dummy_data[:,:,2].fill(100)
    for i in range(256):
        #dummy_data[i,:,0] = 255 - i
        dummy_data[i,:,0] = i
    write_geotiff(filename, dummy_data)
    print('Test complete.')

def gdal_test_3():
    data = test_data_1()
    write_geotiff('gdal_test_3.tiff', data)

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
    gdal_test()
    gdal_test_3()

if __name__ == '__main__':
    main()

    
