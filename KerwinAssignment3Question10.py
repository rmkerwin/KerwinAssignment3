import arcpy

from arcpy import env
env.overwriteOutput = True
target_features = r'D:\GIS\610\Kerwin_Assignment3\Exercise 3.gdb/Tracts'
join_features = r'D:\GIS\610\Kerwin_Assignment3\Exercise 3.gdb/General_Offense'
out_feature_class = r'D:\GIS\610\Kerwin_Assignment3\Exercise 3.gdb/Join_Offense_Tracts'
arcpy.SpatialJoin_analysis (target_features, join_features, out_feature_class)