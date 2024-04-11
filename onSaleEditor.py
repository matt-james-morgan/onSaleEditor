import csv
import pprint
from collections import defaultdict
import pdb; 
csv_files = ['./test_csv/all_items_test.csv', './test_csv/all_items_tags_test.csv', './test_csv/all_items_price_test.csv']

MSRP = "MSRP"
MSRP2 = "MSRP (2)"
DEFAULT = "Default (1)"
SALE = "Sale (3)"


data_dict = defaultdict(dict)

def join_csv_files(csv_files):

    for csv_file in csv_files:

        with open(csv_file, 'r') as file:

            csv_reader = csv.DictReader(file)

            # Iterate through each row in the CSV file
            for row in csv_reader:
                print(row)
                if 'System ID' in row:
                    system_sku = row.pop('System ID')
                    row["SystemSKU"] = system_sku
               
               
                system_sku = row['SystemSKU']

                # Add row data to the dictionary using System ID as key
            
                data_dict[system_sku].update(row)
               

    return data_dict



        

# This var stores all the files of price and tags all in on dict
joined_files = join_csv_files(csv_files)



#######CLEAN DATA#################

# if sale and msrp are empty, store the default value in SALE
for key, val in joined_files.items():
    if val[SALE] == '0' and val[MSRP2] == '0':
        val[SALE] = val[DEFAULT]


##################################

pprint.pprint("After cleaning:")
pprint.pprint(joined_files)

# This stores only files that have the add tag included
online_files = {}

for key, val in joined_files.items():
    if  "add" in val["Tags"]:
        online_files[key] = val

# pprint.pprint(online_files)

# This stores files where price is adjusted
online_adjusted_price = {}

for key, val in online_files.items():
    if  val["Sale (3)"] == val["Default (1)"]:
        online_adjusted_price[key] = val
        online_adjusted_price[key]["MSRP"] = 0
        online_adjusted_price[key]["MSRP (2)"] = 0
