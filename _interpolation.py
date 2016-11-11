import arcpy
import string
from arcpy import env  
from arcpy.sa import *

wkSpace = "C:/Workspace/spk/tam/"
arcpy.env.workspace = wkSpace
maskDir = wkSpace
# Print to the Interactive window all the feature datasets in the
datasets = arcpy.ListFeatureClasses()
inRain = "D:/gdb_Meteo/EW_METEORain.shp"
outDir = "C:/Workspace/spk/_"

def intp(m, o):
    flds = arcpy.ListFields(inRain)    
    #List field
    for fld in flds:
        if fld.name[0]=="W":
            print(fld.name)
            arcpy.env.extent = m
            arcpy.env.mask = m
            print(m+" - "+o)
            outIDW = Idw(inRain, fld.name, 40, 2, \
                         RadiusVariable(10, 150000))
            outIDW.save(o+fld.name)

for dataset in datasets:
    if dataset == "BanDong.shp":
        print(dataset)
        maskShp = maskDir+dataset
        outDirIDW = outDir+"BanDong/"
        intp(maskShp, outDirIDW)
    elif dataset == "HuaiHere.shp":
        print(dataset)
        maskShp = maskDir+dataset
        outDirIDW = outDir+"HuaiHere/"
        intp(maskShp, outDirIDW)
    elif dataset == "MuangJung.shp":
        print(dataset)
        maskShp = maskDir+dataset
        outDirIDW = outDir+"MuangJung/"
        intp(maskShp, outDirIDW)
    elif dataset == "NaYang.shp":
        print(dataset)
        maskShp = maskDir+dataset
        outDirIDW = outDir+"NaYang/"
        intp(maskShp, outDirIDW)
    elif dataset == "PhoPrasart.shp":
        print(dataset)
        maskShp = maskDir+dataset
        outDirIDW = outDir+"PhoPrasart/"
        intp(maskShp, outDirIDW)
    elif dataset == "WangNokAnt.shp":
        print(dataset)
        maskShp = maskDir+dataset
        outDirIDW = outDir+"WangNokAnt/"
        intp(maskShp, outDirIDW)
    else :
        print("not ok")
        

            
