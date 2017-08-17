#!/usr/bin/env python

from lxml import etree
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

xml = '''\
<root>
    <a id="1">aaaaa</a>
    <b id="2" />
    <c id="3">
        <b id="1-1" />
    </c>
</root>
'''

class ATarget:
    events = []
    def start(self, tag, attr):
        self.events.append(('start', tag, attr))

    def end(self, tag):
        self.events.append(('end', tag))

    def close(self):
        events, self.events = self.events, []
        return events

def use_target():
    parser = etree.XMLParser(target=ATarget())
    res = etree.fromstring(xml, parser)

    help(res[0][2])

def use_iter(str_xml=None):
    from StringIO import StringIO
    context = etree.iterparse(StringIO(xml if str_xml is None else str_xml))
    event, ele = context.next()
    print event

def use_iter2(str_xml=None):
    from StringIO import StringIO
    tree = ET.parse(StringIO(xml if str_xml is None else str_xml))
    root = tree.getroot()
    for ele in root.iter(('b')):
        print("%s - %r" % (ele.tag, ele.text))
    print '-' * 20
    root = etree.fromstring(xml if str_xml is None else str_xml)
    for element in root.iter('b', etree.Comment):
        if isinstance(element.tag, basestring):
            print("%s - %r" % (element.tag, element.text))
        else:
            print("SPECIAL: %s - %r" % (element, element.text))

def create_ele(pp=True):
    root = etree.Element('root')
    elea = etree.SubElement(root, 'a', id='1')
    eleb = etree.SubElement(root, 'b', id='2')
    elec = etree.SubElement(root, 'c', id='3')
    elea.append(etree.Entity("#234"))
    eleb.append(etree.Comment("some comment"))
    for element in root.iterchildren('*', etree.Comment, reversed=True):
        if isinstance(element.tag, basestring):
            print("%s - %s" % (element.tag, element.text))
        else:
            print("SPECIAL: %s - %s" % (element, element.text))
    print '-' * 20
    return etree.tostring(root, pretty_print=pp)

def use_bs4():
    soup = BeautifulSoup(xml, 'lxml')
    from bs4 import Comment
    x = soup.new_string('xxx', Comment)
    soup.a.append(x)
    print soup
#print soup.a.clear(True)
    soup.root.unwrap()
    print '-' * 10
    print soup
#help(soup)
    help(soup.a)

if __name__ == '__main__':
    #use_iter2(create_ele(False))
    use_bs4()
