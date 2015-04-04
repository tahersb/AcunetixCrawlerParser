__author__ = 'tahersb'

import xml.etree.ElementTree as ET

#Replace the argument to ET.parse with the XML file to parse
tree = ET.parse('Acunetix_Crawler_XML.xml')
Crawler = tree.getroot()

fileHandler = open('outfile.txt', 'a')

for FullURL in Crawler.iter('FullURL'):
    fileHandler.write(FullURL.text + "\n")
fileHandler.close()
#Results can be found in a file named outfile.txt












