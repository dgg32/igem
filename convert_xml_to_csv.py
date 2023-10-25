import sys

from bs4 import BeautifulSoup
import os    
import re

#desired_headers = ['part_id', 'ok', 'part_name', 'short_desc', 'description', 'part_type', 'author', 'owning_group_id', 'status', 'dominant', 'informational', 'discontinued', 'part_status', 'sample_status', 
#                  'creation_date', 'm_datetime', 'uses', 'doc_size', 'works', 'favorite', 'deep_count', 
#                  'owner_id', 'has_barcode', 'notes', 'source', 'categories', 'sequence', 'sequence_update', 'review_result', 'review_count', 'review_total', 'flag', 'sequence_length', 'rating']


desired_headers = {'part_id': 'part_id', 'ok': 'is_OK', 'part_name': 'part_name', 'short_desc': 'short description', 'description': 'description', 
                   'part_type': 'part_type', 'author': 'author', 'status': 'status', 'dominant': 'dominant', 'informational': 'informational', 'part_status': 'part_status', 
                   'sample_status': 'sample_status', 'creation_date': 'creation_date', 'uses': 'amount_of_projects_used', 'works': 'does_the_part_work', 'favorite': 'amount_of_favorites', 
                   'default_scars': 'default_scars', 'has_barcode': 'has_barcode', 'notes': 'notes', 'source': 'source', 'nickname': 'nickname', 'categories': 'categories', 
                   'sequence': 'sequence', 'sequence_update': 'amount_of_sequence_updates', 'sequence_length': 'sequence_length', 'rating': 'rating'}


parts = []

keys = list(desired_headers.keys())

values = []
for k in keys:
    values.append(desired_headers[k])

print ("\t".join(values))
with open(sys.argv[1], 'r', errors='ignore', encoding="utf-8") as fp:
    soup = BeautifulSoup(fp, 'lxml')
    table = soup.find('table_data', {"name": "parts"})

    for row in table.find_all('row'):
        row_data = {}

        for cell in row.find_all('field'):
            header = cell['name'].strip()
            if header in keys:
                
                content = cell.text.replace("\n", " ").replace("\t", " ").strip()
                if (header == 'notes' or header == 'description' or header == 'source') and content:
                    content = re.sub(r'<.+?>','', content)
                
                row_data[header] = content
        
        #print (row_data)
        row_content = ""
        for h in keys:
            if h in row_data:
                row_content += row_data[h] + "\t"
            else:
                row_content += "\t"
        
        print (row_content[:-1])



