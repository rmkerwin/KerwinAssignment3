import arcpy
arcpy.env.overwriteOutput = True

arcpy.env.workspace = r"D:\GIS\610\Kerwin_Assignment3\Exercise 3.gdb"

arcpy.MakeFeatureLayer_management(r"D:\GIS\610\Kerwin_Assignment3\Exercise 3.gdb\General_Offense","offense_lyr","locationTranslation = 'Restaurant'")
print("selection made")

arcpy.CopyFeatures_management("offense_lyr", 'Crimes in Restaurants')



