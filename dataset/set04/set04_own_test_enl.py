'''
enlarge dataset
'''
import csv
import pandas as pd
import os

FULL_FEATURES = ["D", "I", "PF", "RF", "NG"]
SUB_FEATURES = ["I", "PF", "RF", "NG"]
STAT_FEATURES = ["S", "M", "VAR", "SD"]

CHAR_COUNT = 8 # minimum value of 5
CYCLE = 0
NGRAPH_COUNT = 0
MIDDLE_NGRAPH = 3 # do not change value.
FEATURES_COL = 2

import_csv = pd.read_csv("05_pair_own/" + "own_test.csv")
export_csv_name = "pair_test_own1" + ".csv"
export_csv_path = os.path.join(os.getcwd(), "05_pair_own", export_csv_name)

headerList = ['Subject', 'Password']
for _ in range(2):
    CYCLE = CYCLE + 1
    NGRAPH_COUNT = CYCLE + 1

    headerList.append(f"T{NGRAPH_COUNT}-D|0")
    
    for position in range(CHAR_COUNT-CYCLE):
        for sub in range(len(SUB_FEATURES)):
            headerList.append(f"T{NGRAPH_COUNT}-{SUB_FEATURES[sub]}|{position}+{position+CYCLE}")
        headerList.append(f"T{NGRAPH_COUNT}-D|{position+CYCLE}")

    for stat in range(len(STAT_FEATURES)):
        for full in range(len(FULL_FEATURES)):
            headerList.append(f"T{NGRAPH_COUNT}-{FULL_FEATURES[full]}|{STAT_FEATURES[stat]}")

    for _ in range(CHAR_COUNT-MIDDLE_NGRAPH):
        CYCLE = CYCLE + 1
        NGRAPH_COUNT = NGRAPH_COUNT + 1
        for position in range(CHAR_COUNT-CYCLE):
            for sub in range(len(SUB_FEATURES)):
                headerList.append(f"T{NGRAPH_COUNT}-{SUB_FEATURES[sub]}|{position}+{position+CYCLE}")
        for stat in range(len(STAT_FEATURES)):
            for sub in range(len(SUB_FEATURES)):
                headerList.append(f"T{NGRAPH_COUNT}-{SUB_FEATURES[sub]}|{STAT_FEATURES[stat]}")

    CYCLE = CYCLE + 1
    NGRAPH_COUNT = NGRAPH_COUNT + 1

    for position in range(CHAR_COUNT-CYCLE):
        for sub in range(len(SUB_FEATURES)):
            headerList.append(f"T{NGRAPH_COUNT}-{SUB_FEATURES[sub]}|{position}+{position+CYCLE}")

    CYCLE = 0
    NGRAPH_COUNT = 0

with open(export_csv_path, 'w', newline='') as file:
    dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
    dw.writeheader()

    print(f"\nCSV file will be created: {export_csv_path}")

with open(export_csv_path, 'a', newline='') as file:
    writer = csv.writer(file)

    for body in range(0, 60, 5):
        for first in range(0, 5):
            for second in range(0, 5):
                if second == first:
                    pass
                else:    
                    first_row = body + first
                    placeholder = import_csv.iloc[first_row].values.tolist()
                    sec_row = body + second
                    placeholder.extend(import_csv.iloc[sec_row, FEATURES_COL:].values.tolist())
                    writer.writerow([*placeholder])
                    placeholder.clear()

print(f"\nCSV file has been enlarged and saved at: {export_csv_path}")