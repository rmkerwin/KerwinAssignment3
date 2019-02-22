import arcpy


from arcpy import env
env.overwriteOutput = True


#create file geodatabase
arcpy.CreateFileGDB_management(r'D:\GIS\610\Kerwin_Assignment3\KerwinAssignment3Question5', 'Question5GDB')

featureList = ['CapitalCities', 'Landmarks', 'HistoricPlaces', 'StateNames', 'Nationalities', 'Rivers']
#set workspace environment
arcpy.env.workspace = r'D:\GIS\610\Kerwin_Assignment3\KerwinAssignment3Question5/Question5GDB.gdb'
for layerName in featureList: 
    #Create the Feature Class for the list
    arcpy.CreateFeatureclass_management(r'D:\GIS\610\Kerwin_Assignment3\KerwinAssignment3Question5/Question5GDB.gdb', layerName, 'POINT', '', 'DISABLED', 'DISABLED')
   


