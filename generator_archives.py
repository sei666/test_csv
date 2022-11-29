from lxml import etree
from lxml.etree import tostring
import uuid
import zipfile
import os
from random import randint

def generate_xml():
    root = etree.Element('root')

    var_tag = etree.Element('var')
    var_tag.attrib['name'] = 'id'
    var_tag.attrib['value'] = str(uuid.uuid4())
    root.append(var_tag)

    var_tag = etree.Element('var')
    var_tag.attrib['name'] = 'level'
    var_tag.attrib['value'] = str(randint(1, 100))
    root.append(var_tag)


    objects_tag = etree.Element('objects')
    for i in range(randint(1,10)):
        etree.SubElement(objects_tag, 'object', 
                                        name=uuid.uuid4().hex)
    root.append(objects_tag)

    # pretty string
    s = etree.tostring(root, pretty_print=True)
    return s


def create_zip(name):
    zf = zipfile.ZipFile(os.path.join(PROJ_DIR, "%s.zip" % name), "w",
                         zipfile.ZIP_DEFLATED)
    for i in range(100):
        zf.writestr(f'file{i+1}.xml', generate_xml())
    zf.close()


PROJ_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'archives')

for j in range(50):
    create_zip(j+1)

