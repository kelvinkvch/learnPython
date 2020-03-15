import xml.etree.cElementTree as ET
import csv
import os
from time import time
t = time()


def traverse_path(file_path):
    # 遍历file_path下所有文件，包括子目录
    files = os.listdir(file_path)
    for fi in files:
        fi_d = os.path.join(file_path, fi)

        if os.path.isdir(fi_d):
            traverse_path(fi_d)
        else:
            if fi.endswith(".xml"):
                pass
                getOneXmlBom(fi, fi_d)


def getOneXmlBom(fileName, xmlFilePath):
    xmlDoc = ET.parse(xmlFilePath)
    drawNo = fileName.replace('.xml', '')
    firstNode = xmlDoc.find(".//item/[@type='part']")
    if firstNode != None:
        nodes = xmlDoc.findall(".//item")
        for partNode in nodes:
            partId = partNode.attrib["id"]
            partName = partNode.attrib['nomeBreve']
            partSize = partNode.attrib['sigla']
            partIndex = partNode.attrib['posizione']
            partCounts = partNode.attrib['quantitaMinima']
            csv_writer.writerow(
                [drawNo, partId, partName, partSize, partIndex, partCounts])


# folderPath = input("Please intput foulder path witch contain any .xml files:")
folderPath = r"E:\工作\BOM\h1000"
csvFile = open('result.csv', 'w', newline='')
csv_writer = csv.writer(csvFile)
csv_writer.writerow(['drawNo', 'partID', 'partName',
                     'partSize', 'partIndex', 'partCounts'])

traverse_path(folderPath)

csvFile.close()
print("{0}".format(time()-t))
