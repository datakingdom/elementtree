import xml.etree.ElementTree as etree
import os
import sqlite3

# define our data file
data_file = 'modelDescription.xml'
# if os.path.exists(data_file)!= True:
#     # a means open for reading and writing
#     tmp = open(data_file,'a')
#     tmp.write("<list>\n</list>")
#     tmp.close()
xmlFile = etree.parse(data_file)
root = xmlFile.getroot()
print root.getchildren()[6]

# Print all Component level using ".iter"
print"\n Component Attribute: \n"
for Component in root.iter('Component'):
    print Component.attrib

# Print all ScalarVariable attributes level using ".iter"
print"\n ScalarVariable Attribute:\n"
for ScalarVariable in root.iter('ScalarVariable'):
    print ScalarVariable.attrib

# Print out all Tool attributes under ScalarVariable
print"\n Tool Attribute: \n"
root = root.getchildren()[6]
for Tool in root.iter('Tool'):
        print Tool.attrib

# print "root is: ", root.getchildren()
# for child in root:
#     print("Children are: "), child.attrib
# 'data'
# root.attrib
# {}
#
# print('')
# print "The root element is: \n", root
# print ('')
# print "The root's subelements are: \n", root.getchildren()
# print ('')
# print (root.getchildren()[6])
# print (root.getchildren()[6]).getchildren()
#
# print (root.getchildren()[5])
# Dig out trees
# print (root.getchildren()[5].getchildren()[0].getchildren()[0].getchildren())

# This method can only extract the same level component attributes
# Instead, we use below root.iter method for extracting all the 'Component' attributes
# for child in root.getchildren()[5].getchildren()[0].getchildren()[0].getchildren():
#      print child.tag, child.attrib

# First level
# for Component in root.iter('Component'):
#     print "Component attributes are: \n", Component.attrib
# print('')
# for ScalarVariable in root.iter('ScalarVariable'):
#     # print "ScalarVariable attributes are: \n", ScalarVariable.attrib.get('name')
#     print "ScalarVariable dependencies are: \n", ScalarVariable.attrib.get('dependencies')  # not working
#     print "ScalarVariable children: \n", ScalarVariable.iter('Tool')
#
# root = ScalarVariable.iter('Tool')
# for root in root:
#     print "Tool children: ", root.attrib
#

'''
    Database Part
'''
# create table if not exists components(
#     name text primary key,
#     class text
# );
# conn = sqlite3.connect('components.db')
# curs = conn.cursor()
# curs.execute('''CREATE TABLE components
#              (component_id, component_name, SV_name, variable_id, variable_type, causality, description, variability,
#              initial, start, unit, declaredType, min, derivative, dependencies, equation)''')

# print " \n Name are: \n"
# for Component in root.findall('name'):
#     name = Component.get('name')
#     print name
# curs.execute("INSERT INTO components VALUES ('Component.attrib')")
# curs.rowcount
# conn.commit()
#
# curs.execute("insert into component values(?, ?, ?, ?)", (2, "Carless", "Bishop", "SysEng"))
#
# create table if not exists equation(
#
# )
# Create a SQLite database in terminal??
#  sqlite3 modelDescription.sqlite3


# -----Here is the method to extract text between <attribute>----

# fmiModelDescription = etree.parse("modelDescription.xml")
# Models = fmiModelDescription.findall("ModelVariables")
# for ModelVariables in Models:
#     print ModelVariables.find("ScalarVariable").text
