import arcpy

field = r'D:\GIS\610\Kerwin_Assignment3\Exercise 3.gdb\CallsforService'

count = arcpy.GetCount_management (field)

print(count[0])



