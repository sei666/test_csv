import os
import zipfile
from os import listdir
from os.path import isfile, join
from lxml import etree
import csv


mypath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'archives')
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print(onlyfiles)

zipfile_path = os.path.join(mypath, onlyfiles[0])

zip = zipfile.ZipFile(zipfile_path)

# print (zip.namelist())

f = zip.open(zip.namelist()[0])

tree = etree.parse(f)

f.close()


# print (etree.tostring(root))

f.close()

vars_tags = tree.xpath("//root/var")


header = ['id', 'level']
with open('1.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    data = []
    for var_tag in vars_tags:
        # print(etree.tostring(var_tag, with_tail=False))
        print(var_tag.attrib)
        data.append(var_tag.attrib['value'])
    writer.writerow(data)


objects_tag = tree.xpath("//root/objects/object")
for object_tag in objects_tag:
    # print(etree.tostring(object_tag, with_tail=False))
    print(object_tag.attrib)


