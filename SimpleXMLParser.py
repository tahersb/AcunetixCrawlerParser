__author__ = 'TB00353682'

import xml.etree.ElementTree as ET

tree = ET.parse('Crawler_Mar15_XML.xml')
Crawler = tree.getroot()
print "Opening file for writing"
fileHandler = open('outfile.txt', 'a')
print "Writing FullURLs to outfile.txt"
for FullURL in Crawler.iter('FullURL'):
    fileHandler.write(FullURL.text + "\n")
print "Write complete"
print "Closing file"
fileHandler.close()












