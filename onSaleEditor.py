import csv
import pprint
from collections import defaultdict
import pdb; 
csv_files = ['./csv/all_items_test.csv', './csv/all_items_tags_test.csv', './csv/all_items_price_test.csv']


data_dict = defaultdict(dict)

def join_csv_files(csv_files):

    for csv_file in csv_files:

        with open(csv_file, 'r') as file:

            csv_reader = csv.DictReader(file)

            # Iterate through each row in the CSV file
            for row in csv_reader:

                if 'System ID' in row:
                    system_sku = row.pop('System ID')
                    row["SystemSKU"] = system_sku
               
               
                system_sku = row['SystemSKU']

                # Add row data to the dictionary using System ID as key
            
                data_dict[system_sku].update(row)
               

    return data_dict



        

# This var stores all the files of price and tags all in on dict
joinedFiles = join_csv_files(csv_files)

pprint.pprint("JOINED")    

pprint.pprint(joinedFiles)    

# This stores only files that have the add tag included
filtered_files = {}

for key, val in joinedFiles.items():
    if  "add" in val["Tags"]:
        filtered_files[key] = val

# pprint.pprint(filtered_files)

# This stores files where price is adjusted
adjusted_price = {}

for key, val in filtered_files.items():
    if  val["Sale (3)"] == val["Default (1)"]:
        adjusted_price[key] = val
        adjusted_price[key]["MSRP"] = 0
        adjusted_price[key]["MSRP (2)"] = 0




  
