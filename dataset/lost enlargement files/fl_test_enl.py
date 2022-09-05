'''
increase dataset
'''
import time
import csv
import pandas as pd
import os
from sys import exit


FEATURES_COL = 2
export_dir_path = os.path.join(os.getcwd(), "export")

# csv_name = "flm2m_rand194_test" + ".csv"
# csv_path = os.path.join(export_dir_path, csv_name)
# small_df = pd.read_csv("dataset/" + "rand97_test.csv")

# csv_name = "flm2m_fr194_test_fixed" + ".csv"
# csv_path = os.path.join(export_dir_path, csv_name)
# small_df = pd.read_csv("dataset/" + "fr97_test_fixed.csv")

# csv_name = "flm2m_fr194_test_flex" + ".csv"
# csv_path = os.path.join(export_dir_path, csv_name)
# small_df = pd.read_csv("dataset/" + "fr97_test_flex.csv")

# csv_name = "flm2m_rand291_test" + ".csv"
# csv_path = os.path.join(export_dir_path, csv_name)
# small_df = pd.read_csv("dataset/" + "rand97_test.csv")

# csv_name = "flm2m_fr291_test_fixed" + ".csv"
# csv_path = os.path.join(export_dir_path, csv_name)
# small_df = pd.read_csv("dataset/" + "fr97_test_fixed.csv")

# csv_name = "flm2m_fr291_test_flex" + ".csv"
# csv_path = os.path.join(export_dir_path, csv_name)
# small_df = pd.read_csv("dataset/" + "fr97_test_flex.csv")

headerList = ['Subject', 'Sequence']
for _ in range(3):
    headerList.append(f"D|0")
    for _ in range(5-1):
        headerList.append(f"I|{_}+{_+1}")
        headerList.append(f"PF|{_}+{_+1}")
        headerList.append(f"RF|{_}+{_+1}")
        headerList.append(f"DT|{_}+{_+1}")
        headerList.append(f"D|{_+1}")
    headerList.append(f"T2-D-S")
    headerList.append(f"T2-I-S")
    headerList.append(f"T2-PF-S")
    headerList.append(f"T2-RF-S")
    headerList.append(f"T2-DT-S")

    headerList.append(f"T2-D-M")
    headerList.append(f"T2-I-M")
    headerList.append(f"T2-PF-M")
    headerList.append(f"T2-RF-M")
    headerList.append(f"T2-DT-M")

    headerList.append(f"T2-D-VAR")
    headerList.append(f"T2-I-VAR")
    headerList.append(f"T2-PF-VAR")
    headerList.append(f"T2-RF-VAR")
    headerList.append(f"T2-DT-VAR")

    headerList.append(f"T2-D-SD")
    headerList.append(f"T2-I-SD")
    headerList.append(f"T2-PF-SD")
    headerList.append(f"T2-RF-SD")
    headerList.append(f"T2-DT-SD")

    for _ in range(5-2):
        headerList.append(f"T3_I|{_}+{_+2}")
        headerList.append(f"T3_PF|{_}+{_+2}")
        headerList.append(f"T3_RF|{_}+{_+2}")
        headerList.append(f"T3_G|{_}+{_+2}")

    headerList.append(f"T3-I-S")
    headerList.append(f"T3-PF-S")
    headerList.append(f"T3-RF-S")
    headerList.append(f"T3-G-S")

    headerList.append(f"T3-I-M")
    headerList.append(f"T3-PF-M")
    headerList.append(f"T3-RF-M")
    headerList.append(f"T3-G-M")

    headerList.append(f"T3-I-VAR")
    headerList.append(f"T3-PF-VAR")
    headerList.append(f"T3-RF-VAR")
    headerList.append(f"T3-G-VAR")

    headerList.append(f"T3-I-SD")
    headerList.append(f"T3-PF-SD")
    headerList.append(f"T3-RF-SD")
    headerList.append(f"T3-G-SD")

    for _ in range(5-3):
        headerList.append(f"T4_I|{_}+{_+3}")
        headerList.append(f"T4_PF|{_}+{_+3}")
        headerList.append(f"T4_RF|{_}+{_+3}")
        headerList.append(f"T4_G|{_}+{_+3}")

    headerList.append(f"T4-I-S")
    headerList.append(f"T4-PF-S")
    headerList.append(f"T4-RF-S")
    headerList.append(f"T4-G-S")

    headerList.append(f"T4-I-M")
    headerList.append(f"T4-PF-M")
    headerList.append(f"T4-RF-M")
    headerList.append(f"T4-G-M")

    headerList.append(f"T4-I-VAR")
    headerList.append(f"T4-PF-VAR")
    headerList.append(f"T4-RF-VAR")
    headerList.append(f"T4-G-VAR")

    headerList.append(f"T4-I-SD")
    headerList.append(f"T4-PF-SD")
    headerList.append(f"T4-RF-SD")
    headerList.append(f"T4-G-SD")

    for _ in range(5-4):
        headerList.append(f"T5_I|{_}+{_+4}")
        headerList.append(f"T5_PF|{_}+{_+4}")
        headerList.append(f"T5_RF|{_}+{_+4}")
        headerList.append(f"T5_G|{_}+{_+4}")

with open(csv_path, 'w', newline='') as file:
    dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
    dw.writeheader()

    print(f"CSV file will be created: {csv_path}")

with open(csv_path, 'a', newline='') as file:
    writer = csv.writer(file)

    for outer in range(0, 80, 10):
        for first in range(0, 10):
            for second in range(0, 10):
                if second == first:
                    pass
                else:    
                    first_row = outer + first
                    placeholder = small_df.iloc[first_row].values.tolist()
                    sec_row = outer + second
                    placeholder.extend(small_df.iloc[sec_row, FEATURES_COL:].values.tolist())
                    writer.writerow([*placeholder])
                    placeholder.clear()

    # for outer in range(0, 80, 10):
    #     for first in range(0, 10):
    #         for second in range(0, 10):
    #             for third in range(0, 10):
    #                 if second == first or third == first or third == second:
    #                     pass
    #                 else:    
    #                     first_row = outer + first
    #                     placeholder = small_df.iloc[first_row].values.tolist()
    #                     sec_row = outer + second
    #                     placeholder.extend(small_df.iloc[sec_row, FEATURES_COL:].values.tolist())
    #                     third_row = outer + third
    #                     placeholder.extend(small_df.iloc[third_row, FEATURES_COL:].values.tolist())
    #                     writer.writerow([*placeholder])
    #                     placeholder.clear()

    for outer in range(0, 80, 10):
        for first in range(0, 3):
            for second in range(3, 6):
                for third in range(6, 9):
                    if second == first or third == first or third == second:
                        pass
                    else:    
                        first_row = outer + first
                        placeholder = small_df.iloc[first_row].values.tolist()
                        sec_row = outer + second
                        placeholder.extend(small_df.iloc[sec_row, FEATURES_COL:].values.tolist())
                        third_row = outer + third
                        placeholder.extend(small_df.iloc[third_row, FEATURES_COL:].values.tolist())
                        writer.writerow([*placeholder])
                        placeholder.clear()