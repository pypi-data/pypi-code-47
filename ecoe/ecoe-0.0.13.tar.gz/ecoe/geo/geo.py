def PrintRasterInfo(self,raster):
    print('Projection:', raster.crs)         # Projection
    print('Shape:' ,raster.shape)
    print('Width:', raster.width)
    print('Height:', raster.height)
    print('Count:',raster.count)
    print('Bounds:',raster.bounds)
    print('Driver:',raster.driver)
    print('NoData Values:',raster.nodatavals)
    print('Meta:',raster.meta)
    return
        

def ClipRasterToCoordBoundingBox(self,raster,min_x,min_y,max_x,max_y): 
    # clip the the region of interest, coordinate must match raster projection

    # make the bounding box for clipping
    bbox = box(min_x, min_y, max_x, max_y)
    geo = gpd.GeoDataFrame({'geometry': bbox}, index=[0], crs=raster.crs)
    coords = getFeatures(geo)   # get geometry coordinates
    clpRaster, out_transform = mask(raster, coords, crop=True, indexes=1)   # clip to the bounding box
    return clpRaster, out_transform

def ClipRasterToRowColBoundingBox(self,raster,min_row, min_col, max_row, max_col): 
    # clip the the region of interest, uses cell indices (row/col)scoordinate must match raster projection
    # return 2D array of data, transform of clipped data
    clpRaster = raster[min_row:max_row+1][min_col:max_col+1]
    #clpRaster, out_transform = mask(raster, coords, crop=True, indexes=1)   # clip to the bounding box
    return clpRaster #, out_transform

def ClipRasterToFeatures(self, raster, features):
    return
