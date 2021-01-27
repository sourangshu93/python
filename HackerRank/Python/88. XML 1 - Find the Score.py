import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    count = len(root.attrib)
    elements = root.findall(".//*")
    print(elements)
    for item in elements:
        print(item)
        count += len(item.attrib)
    return  count
if __name__ == '__main__':
    N=int(input())
    xml=""
    for i in range(N):
        xml +=input()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))