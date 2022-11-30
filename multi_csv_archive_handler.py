import multiprocessing
from lxml import etree
import zipfile
import csv
import time
import os

def mp_worker(big_filename):
    head_tail = os.path.split(big_filename)
    zipfile_path = head_tail[0]
    filename =  head_tail[1]
    zip = zipfile.ZipFile(zipfile_path)
    f = zip.open(filename)
    tree = etree.parse(f)
    f.close()
    vars_tags = tree.xpath("//root/var")
    data1 = [vars_tags[0].attrib['value'], vars_tags[1].attrib['value']]

    objects_tag = tree.xpath("//root/objects/object")
    data2 = []
    for object_tag in objects_tag:
        data2.append([data1[0], object_tag.attrib['name']])
    return data1, data2

def mp_handler():
    p = multiprocessing.Pool(8)
    
    mypath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'archives')
    zip_files = [f for f in os.listdir(mypath) if f.endswith('.zip')]
    header1 = ['id', 'level']
    header2 = ['id', 'object_name']

    with open('1.csv', 'w', encoding='UTF8', newline='') as f1, open('2.csv', 'w', encoding='UTF8', newline='') as f2:
        writer = csv.writer(f1)
        writer.writerow(header1)
        writer2 = csv.writer(f2)
        writer2.writerow(header2)

        for x in zip_files:
            zipfile_path = os.path.join(mypath, x)
            zip = zipfile.ZipFile(zipfile_path)
            filenames = zip.namelist()
            big_filenames = [os.path.join(zipfile_path, filiname) for filiname in filenames]
            for result in p.imap(mp_worker, big_filenames):
                writer.writerow(result[0])
                writer2.writerows(result[1])

if __name__=='__main__':
    startTime = time.time()
    mp_handler()
    executionTime = (time.time() - startTime)
    print('Execution time in seconds: ' + str(executionTime))