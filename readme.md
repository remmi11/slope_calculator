# Install Python and GDAL (1 time)

This is a Python (v2.7*) script for creating clipping rasters and running slope analysis (percent).

## Install Python 2.7 for Windows
Download the executable installer from [Python windows downloads](https://www.python.org/downloads/windows/). Then execute the installer. 
<img src="/images/python_windows.png" width="300" title="Proj4 link">

## Add the following items to 'path' variable in windows.
c:\python27;c:\python27\Scripts;c:\python27\Lib;

Click environmental variables |  Append to existing values
:-------------------------:|:-------------------------:
<img src="/images/path1.png" width="300" title="Proj4 link"> | <img src="/images/path2.png" width="300" title="Proj4 link">


## Install gdal from [GIS Internals](https://www.gisinternals.com/query.html?content=filelist&file=release-1911-x64-gdal-2-4-4-mapserver-7-4-3.zip).
<img src="/images/gdal1.png" width="300" title="Proj4 link">

## Add the following gdal items to 'path' variable in windows.
C:\Program Files\GDAL;C:\Program Files\GDAL\gdal-data

# Execute script

## Add variable values to script.
1) Path to parcels (shapefile variable). This is the relative path to parcels.shp (ie. - './parcels/parcels.shp')
2) Path to input DEM raster (raster variable). This is the relative path to dem raster (ie. - './myraster.tif')  
3) Proj4 text (proj4 variable) - Determine SPC Zone by viewing SPC zone layer in QGIS. Note the fips code for zone where parcels lie (ie. 4204). Search [spatialreference.org](https://spatialreference.org/) for your fips.  When found select the zone to view details.  From zone details select 'proj4' link. Image below.

<img src="/images/proj4.png" width="300" title="Proj4 link">

## Execute from cmd line.
1) Open cmd prompt.
2) 'cd' to project folder (ie. - cd c:\data\slope_calculator) 
3) Run script
```bash
python scripts\script.py
```