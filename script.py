__author__='MEOS'
__title__='CountWindows'
from Autodesk.Revit.DB import FilteredElementCollector, ElementCategoryFilter, BuiltInCategory
doc = __revit__.ActiveUIDocument.Document
collector=FilteredElementCollector(doc)
filter=ElementCategoryFilter(BuiltInCategory.OST_Windows)
windows=collector.WherePasses(filter).WhereElementIsNotElementType().ToElements()
print ("Window counted is: {}".format(windows.Count))