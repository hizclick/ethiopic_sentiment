import os

from xml.etree import ElementTree

from xml.etree import ElementTree
root = ElementTree.parse("1.xml").getroot()

def tager():
    sentence = ''
    result = dict()
    tag = ()
    part = []
    for item in root.findall("a"):
        if item.attrib['title'] == 'ORG':
            children = item.getchildren()
            for child in children:
                sentence = sentence + " " + str(child.text)
                tag = ('ORG', child.text)
                part.extend(tag)
        if item.attrib['title'] == 'LOC':
            children = item.getchildren()
            for child in children:
                sentence = sentence + " " + str(child.text)
                tag = ('LOC', child.text)
                part.extend(tag)
        elif item.attrib['title'] == 'TTL':
            children = item.getchildren()
            for child in children:
                sentence = sentence + " " + str(child.text)
                tag = ('TTL', child.text)
                part.extend(tag)
        elif item.attrib['title'] == 'TIME':
            children = item.getchildren()
            for child in children:
                sentence = sentence + " " + str(child.text)
                tag = ('TIME', child.text)
                part.extend(tag)
        elif item.attrib['title'] == 'PER':
            children = item.getchildren()
            for child in children:
                sentence = sentence + " " + str(child.text)
                tag = ('PER', child.text)
                part.extend(tag)

    result[sentence] = part
    return result

tager()
    
