import xml.etree.ElementTree as etree

#def depth(elem,level):
#    global maxdepth
#    mytree=etree.fromstring(xml)

if __name__=="__main__":
    N=int(input())
    xml=""
    for n in range (N):
        xml=xml+input()+"\n"
    mytree=etree.fromstring(xml)
    