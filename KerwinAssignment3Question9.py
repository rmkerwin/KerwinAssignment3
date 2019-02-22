import arcpy

from arcpy import env
env.overwriteOutput = True

arcpy.CreateFileGDB_management(r'D:\GIS\610\Kerwin_Assignment3\KerwinAssignment3Question9', 'GDB_Number9')

arcpy.env.workspace = r'D:\GIS\610\Kerwin_Assignment3\KerwinAssignment3Question9\GDB_Number9.gdb'

arcpy.CreateFeatureclass_management(r'D:\GIS\610\Kerwin_Assignment3\KerwinAssignment3Question9\GDB_Number9.gdb', 'Feature_Number9', 'POINT', '', 'DISABLED', 'DISABLED')
arcpy.AddField_management ('Feature_Number9', 'Fruit', 'TEXT')
arcpy.CreateDomain_management(r'D:\GIS\610\Kerwin_Assignment3\KerwinAssignment3Question9/GDB_Number9.gdb', 'Fruit_Code', 'Fruit_Type', 'TEXT', 'CODED', 'DUPLICATE', 'DEFAULT')

arcpy.AddCodedValueToDomain_management(r'D:\GIS\610\Kerwin_Assignment3\KerwinAssignment3Question9/GDB_Number9.gdb', 'Fruit_Code', 'A', 'Fruit')
arcpy.AddCodedValueToDomain_management(r'D:\GIS\610\Kerwin_Assignment3\KerwinAssignment3Question9/GDB_Number9.gdb', 'Fruit_Code', 'B', 'Vegetable')
arcpy.AddCodedValueToDomain_management(r'D:\GIS\610\Kerwin_Assignment3\KerwinAssignment3Question9/GDB_Number9.gdb', 'Fruit_Code', 'C', 'Meat')
arcpy.AddCodedValueToDomain_management(r'D:\GIS\610\Kerwin_Assignment3\KerwinAssignment3Question9/GDB_Number9.gdb', 'Fruit_Code', 'D', 'Bread')
arcpy.AddCodedValueToDomain_management(r'D:\GIS\610\Kerwin_Assignment3\KerwinAssignment3Question9/GDB_Number9.gdb', 'Fruit_Code', 'E', 'Dessert')
