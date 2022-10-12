'''
enlarge dataset
'''
import csv
import pandas as pd
import os

FULL_FEATURES = ["D", "I", "PF", "RF", "NG"]
SUB_FEATURES = ["I", "PF", "RF", "NG"]
STAT_FEATURES = ["S", "M", "VAR", "SD"]
DATASET_TYPE = ["IR", "DR"]

CHAR_COUNT = 10 # minimum value of 5
CYCLE = 0
NGRAPH_COUNT = 0
MIDDLE_NGRAPH = 3 # do not change value.

for type in range(len(DATASET_TYPE)):

    import_csv = pd.read_csv(f"01_original/" + "test_" + DATASET_TYPE[type] + ".csv")
    export_csv_name = "pair_test_" + DATASET_TYPE[type] + ".csv"
    export_csv_path = os.path.join(os.getcwd(), "02_pair", export_csv_name)

    headerList = ['Subject', 'Class', 'Sequence']
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
            
        for body in range(0, 80, 8):
            # class three
            for first in range(0, 2):
                for second in range(2, 8):
                    first_row = body + first
                    placeholder = import_csv.iloc[first_row].values.tolist()
                    
                    sec_row = body + second
                    placeholder.extend(import_csv.iloc[sec_row, 3:].values.tolist())

                    writer.writerow([*placeholder])
                    placeholder.clear()

            # class four
            for first in range(2, 4):
                for second in range(0, 2):
                    first_row = body + first
                    placeholder = import_csv.iloc[first_row].values.tolist()
                    
                    sec_row = body + second
                    placeholder.extend(import_csv.iloc[sec_row, 3:].values.tolist())

                    writer.writerow([*placeholder])
                    placeholder.clear()

                for second in range(4, 8):
                    first_row = body + first
                    placeholder = import_csv.iloc[first_row].values.tolist()
                    
                    sec_row = body + second
                    placeholder.extend(import_csv.iloc[sec_row, 3:].values.tolist())

                    writer.writerow([*placeholder])
                    placeholder.clear()

            # class five
            for first in range(4, 6):
                for second in range(0, 4):
                    first_row = body + first
                    placeholder = import_csv.iloc[first_row].values.tolist()
                    
                    sec_row = body + second
                    placeholder.extend(import_csv.iloc[sec_row, 3:].values.tolist())

                    writer.writerow([*placeholder])
                    placeholder.clear()

                for second in range(6, 8):
                    first_row = body + first
                    placeholder = import_csv.iloc[first_row].values.tolist()
                    
                    sec_row = body + second
                    placeholder.extend(import_csv.iloc[sec_row, 3:].values.tolist())

                    writer.writerow([*placeholder])
                    placeholder.clear()

            # class six
            for first in range(6, 8):
                for second in range(0, 6):
                    first_row = body + first
                    placeholder = import_csv.iloc[first_row].values.tolist()
                    
                    sec_row = body + second
                    placeholder.extend(import_csv.iloc[sec_row, 3:].values.tolist())

                    writer.writerow([*placeholder])
                    placeholder.clear()

    print(f"\nCSV file has been enlarged and saved at: {export_csv_path}")