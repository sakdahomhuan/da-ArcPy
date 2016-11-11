import arcpy
import string
from arcpy import env  
from arcpy.sa import *

def zstat(flderName):
    wkSpace = "C:/Workspace/spk/"+flderName+"/"
    arcpy.env.workspace = wkSpace
    maskDir = wkSpace
    fcs = arcpy.ListFeatureClasses()
    rasters = arcpy.ListRasters()
    for fc in fcs:
        for raster in rasters:    
            outZSaT = ZonalStatisticsAsTable(fc,"zcode", raster, maskDir+"z"+raster+".dbf", "NODATA", "MEAN")
            print(raster)
       
def deltable(flderName):
    wkSpace = "C:/Workspace/spk/"+flderName+"/"
    arcpy.env.workspace = wkSpace
    maskDir = wkSpace
    tbs = arcpy.ListTables()
    dropFields = ["ZONE_CODE","COUNT","AREA"]
    for tb in tbs:
        arcpy.DeleteField_management(tb, dropFields)        
        print(tb)
            
flders = ["_BanDong", "_HuaiHere", "_MuangJung", "_NaYang", "_PhoPrasart", "_WangNokAnt"]
#flders = ["_MuangJung"]        
for flder in flders:
    print(flder)
    zstat(flder)
    deltable(flder)
    
