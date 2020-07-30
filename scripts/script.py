# -------------------------------------------------------------------------------
# Name:        permits
# Author:      Noah Huntington
# Created:     7/28/2020
# Copyright:   (c) Noah 2020
# Licence:     <your licence>
# -------------------------------------------------------------------------------
import os
import time
import sys
import traceback
import gdal

# Allow for verbose exception reporting
gdal.UseExceptions()

orig_stdout = sys.stdout
f = open('log.txt', 'w')
sys.stdout = f

start_time = time.time()

#################################################################################
#################################################################################
# user defined variables
#################################################################################
#parcels to iterated
shapefile = r".\multiple parcels\parcel.shp"

#dem raster for analysis (epsg: 4326)
raster = 'srtm_17_07.tif'

#proj4 text from https://spatialreference.org/ for transformation
proj4 = '+proj=lcc +lat_1=28.38333333333333 +lat_2=30.28333333333334 +lat_0=27.83333333333333 +lon_0=-99 +x_0=600000.0000000001 +y_0=4000000 +ellps=GRS80 +datum=NAD83 +to_meter=0.3048006096012192 +no_defs '
#################################################################################
#################################################################################


driver = ogr.GetDriverByName("ESRI Shapefile")
dataSource = driver.Open(shapefile, 0)
layer = dataSource.GetLayer()
layerDefinition = layer.GetLayerDefn()
layer_list = []


def getfields():
    for i in range(layerDefinition.GetFieldCount()):
        layer_name = layerDefinition.GetFieldDefn(i).GetName()
        layer_list.append(layer_name)

    print layer_list[0]

    for x in layer_list:
        print 'This is the layer {}'.format(x)
        for feature in layer:
            feat = feature.GetField(x)
            print feat
            clipRaster(feat)
            calcSlope(feat)
        layer.ResetReading()  # reset the read position to the start


# exports geo tables to disk.
def clipRaster(fid):

    print 'Clipping Raster.'

    # Build the OGR SQL
    sql = "SELECT * FROM %s WHERE FID = %s" % ('parcel', fid)
    print sql

    #gdalwarp -s_srs EPSG:4326 -t_srs "+proj=lcc +lat_1=28.38333333333333 +lat_2=30.28333333333334 +lat_0=27.83333333333333 +lon_0=-99 +x_0=600000.0000000001 +y_0=4000000 +ellps=GRS80 +datum=NAD83 +to_meter=0.3048006096012192 +no_defs " -of GTiff -cutline ".\multiple parcels\parcel.shp" -csql "SELECT * FROM parcel WHERE FID = 14" -crop_to_cutline srtm_17_07.tif ".\results\clipped_14.tif"
    cmd = """gdalwarp -s_srs EPSG:4326 -t_srs "%s" -of GTiff -cutline "%s" -csql "%s" -cblend 4 -crop_to_cutline %s .\\clipped\\clipped_%s.tif -overwrite""" % (proj4, shapefile, sql, raster, fid)
    print cmd
    os.system(cmd)


def calcSlope(fid):
    # s = ratio of vertical units to horizontal. m/ft = 0.3048006
    cmd = """gdaldem slope clipped/clipped_%s.tif slope/slope_%s.tif -of GTiff -b 1 -s 0.3048006 -p"""% ( fid, fid)
    os.system(cmd)


if __name__ == '__main__':

    getfields()

    elapsed_time = time.time() - start_time
    print "Elapsed time: " + str(elapsed_time) + " secs"
