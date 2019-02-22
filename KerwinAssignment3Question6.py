import arcpy
from arcpy import env
arcpy.env.overwriteOutput = True

arcpy.env.workspace = r'D:\GIS\610\Kerwin_Assignment3\Exercise 3.gdb'
arcpy.AddField_management ('CallsforService', 'Crime_Explanation', 'TEXT')

def classifyBurglary():
    if 'CFSType' == 'Burglary Call':
        arcpy.CalculateField_management('CallsforService', 'Crime_Explanation', classifyBurglary)
        return 'This is a burglary'
        