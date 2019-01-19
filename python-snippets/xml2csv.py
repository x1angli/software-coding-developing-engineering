__author__ = 'x1ang.li'

import os
import codecs
import csv
import xml.etree.ElementTree as ET

base_dir = os.path.join(os.path.dirname(__file__), 'data')
fin_name = os.path.join(base_dir, 'input1.xml')
fout_name = os.path.join(base_dir, 'output1.csv')

root = ET.parse(fin_name).getroot()

# First, we populate and prepare the header / fieldnames
fieldnames = []
for firstrowcell in root[0]:
    fieldnames.append(firstrowcell.tag)

# Then, we populate the data
rows = []
for row_elem in root:
    row_csv = {}
    for cell_elem in row_elem: # populating the cell
        row_csv[cell_elem.tag] = cell_elem.text
    rows.append(row_csv)

# Finally, we write the output into the .csv file
with codecs.open(fout_name, 'w', 'utf-8-sig') as csv_file: # must write BOM first!
 #  so that MicroSoft Excel will be able to recognize non-ASCII characters
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
