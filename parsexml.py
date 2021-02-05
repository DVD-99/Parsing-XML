import sys
import xml.etree.ElementTree as ET
import json
import xmltodict

from xml.dom.minidom import parseString

#sys arguments list takes in the commands which you type in cmd.
if(sys.argv[1] == "-h" or sys.argv[1] == "--help"):
    print ("USAGE: Python3 {} inputfile.xml".format(sys.argv[0]))
# The first element of the list is always the name of the python file 
    sys.exit()
    
fileToParse = sys.argv[1]   #assigning the value to the list

print("File to Parse: {}".format(fileToParse))
#It parses the data into tree variable
tree = ET.ElementTree(file = fileToParse)
print("******")
print("Tree Root:")
# Root has tag and attrib, the tag reperents the element type
# Attrib is a dictionary which has the keys and values of that tag
root = tree.getroot()
print("root tag:{}, root attribute:{}".format(root.tag, root.attrib))

print("******")
print("Children of root")
#printing the sub-elements that are associated with root 
for element in root:
    print(element.tag, element.attrib, element.keys(), element.text)
#it prints tag, attribute, keys, text which is inbetween the tags
print("******")
itemsInTree = len(root)
#stores the length of root and displaying the tags and attributes of items using that length
print("Print Indexed Items")
print("First Item tag:{}, First Item attribute:{}".format(root[0].tag,root[0].attrib))
print("Second Item tag:{}, Second Item attribute:{}".format(root[1].tag,root[1].attrib))
print("Last Item tag:{}, Last Item attribute:{}".format(root[itemsInTree-1].tag,root[itemsInTree-1].attrib))

print("******")
print("Iterate through entire tree, providing a list of branch/sub-branch tags")
#helps in printing the tree .findall function-finds all the tags which has sub-branch
for element in tree.findall("branch/sub-branch"):
    print(element.tag, element.attrib)
    
print("******")
print("Deleting second item")
root.remove(root[1])
#It removes the second item in root

print("******")
print("Insert an item at the end")
print("Last Item:")

newElement = ET.Element("branch")   #adds a tag with branch
newElement.set("name","Newly Added Name")   #adds an attribute with Newly Added Name 
newElement.text = "This is a test"  #adds a text in the new created tag
root.append(newElement)     #adding the the element to the root


outfile = open('testxmlout.xml','w')    #opens the file into writing mode 
print("******")
print("Print a formatted tree (reflecting changes)")
xmlstrPretty = parseString(ET.tostring(root)).toprettyxml(indent = "    ", newl = ' ')
#printing the xml data after changes in structured format
print(xmlstrPretty)
outfile.write(xmlstrPretty) #writes into the file what is printed on output

print("******")
print("Convert to Dict")
xmlFile = open('testxml.xml',"rb") #reads the file in binary mode
dictObject = xmltodict.parse(xmlFile, xml_attribs = True)
print(dictObject)   #prints all the data in xml as a dictionary
print(dictObject['doc']['branch'][0]['#text'])  #prints the text of the first element

for branch in dictObject['doc']['branch']:
    print(branch['@name'], "\t", branch['#text'])   #prints the branch name and it's coressponding text

print("******")
print("Convert to json and back to a dictionary")
jsonObject = json.dumps(dictObject, indent = 4) #converting dictionary into json object by passing the dictObject
dictJsonObject = json.loads(jsonObject) #converting into dictionary from json object
print(dictJsonObject)
print(dictJsonObject['doc']['branch'][0]['#text'])


