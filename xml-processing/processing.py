#!/usr/bin/env python
__author__ = 'lorgio'
import time
import xml.etree.cElementTree as ET

def editandoXML(filename):
    tree = ET.ElementTree(file = filename)
    root = tree.getroot()

    for begin_time in root.iter("begin"):
        print begin_time.text
        begin_time.text = time.ctime(int(begin_time.text))

    tree = ET.ElementTree(root)
    with open("updated.xml", "w") as f:
        tree.write(f)

def lecturaXML(filename):
    tree = ET.ElementTree(file = filename)
    root = tree.getroot()

    for att in root.iter("Property"):
        for inatt in att:
            print "%s=%s" % (inatt.tag, inatt.text)
        print "-"*40


if __name__ == "__main__":
    lecturaXML("Properties_42001_2015_4_9_Changes.xml")