import sys

headers_for_graph = ['id', 'part_id', 'part_name', 'categories']

tsv_file = sys.argv[1]

headers = []

category_category = set()
category_part = set()

category = {}
part = {}

n = 0
for line in open(tsv_file, 'r'):
    fields = line.strip().split('\t')
    
    if n == 0:
        headers = fields
    else:
        part_id =  ""
        part_name = ""
        cate = ""
        for h, f in zip(headers, fields):
            if h == "part_id":
                part_id = f
            if h == "part_name":
                part_name = f
            if h == "categories":
                #//chassis/prokaryote/ecoli/nissle //collections/probiotics //collections/probiotics/biocontainment
                cate = f

        if part_id != "" and part_name != "" and cate != "":
            ca = cate.split('//')
            for c in ca:
                
                categories = [x.strip() for x in c.split('/') if x.strip()]

                #print (categories)

                for i, c in enumerate(categories):
                    if i < len(categories) - 1:
                        current = "|".join(categories[:i+1])
                        next = "|".join(categories[:i+2])
                        category_category.add((current, next))
                        category[current] = {"name": c}
                
                    elif i == len(categories) - 1:
                        current = "|".join(categories[:i+1])
                        category_part.add((current, part_id))
                        category[current] = {"name": c}
                        part[part_id] = part_name
    
    n += 1

                            
output_folder = "for_neo4j"

with open(f'{output_folder}/category_category.tsv', 'w') as f:
    f.write("from\tto\n")
    for s in category_category:
        f.write(f"{s[0]}\t{s[1]}\n")

with open(f'{output_folder}/category_part.tsv', 'w') as f:
    f.write("from\tto\n")
    for s in category_part:
        f.write(f"{s[0]}\t{s[1]}\n")

with open(f'{output_folder}/category.tsv', 'w') as f:
    f.write("id\tname\n")
    for s in category:
        f.write(f"{s}\t{category[s]['name']}\n")

with open(f'{output_folder}/part.tsv', 'w') as f:
    f.write("part_id\tname\n")
    for s in part:
        f.write(f"{s}\t{part[s]}\n")