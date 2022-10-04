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

csv_name = "flm2m_fr291_train" + ".csv"
csv_path = os.path.join(export_dir_path, csv_name)
small_df = pd.read_csv("dataset/" + "fr97_train.csv")

headerList = ['Subject', 'Actual', 'Password']

for _ in range(2):
    headerList.append(f"T2-D|0")
    for _ in range(8-1):
        headerList.append(f"T2-I|{_}+{_+1}")
        headerList.append(f"T2-PF|{_}+{_+1}")
        headerList.append(f"T2-RF|{_}+{_+1}")
        headerList.append(f"T2-NG|{_}+{_+1}")
        headerList.append(f"T2-D|{_+1}")
    headerList.append(f"T2-D|S")
    headerList.append(f"T2-I|S")
    headerList.append(f"T2-PF|S")
    headerList.append(f"T2-RF|S")
    headerList.append(f"T2-NG|S")

    headerList.append(f"T2-D|M")
    headerList.append(f"T2-I|M")
    headerList.append(f"T2-PF|M")
    headerList.append(f"T2-RF|M")
    headerList.append(f"T2-NG|M")

    headerList.append(f"T2-D|VAR")
    headerList.append(f"T2-I|VAR")
    headerList.append(f"T2-PF|VAR")
    headerList.append(f"T2-RF|VAR")
    headerList.append(f"T2-NG|VAR")

    headerList.append(f"T2-D|SD")
    headerList.append(f"T2-I|SD")
    headerList.append(f"T2-PF|SD")
    headerList.append(f"T2-RF|SD")
    headerList.append(f"T2-NG|SD")

    for _ in range(8-2):
        headerList.append(f"T3-I|{_}+{_+2}")
        headerList.append(f"T3-PF|{_}+{_+2}")
        headerList.append(f"T3-RF|{_}+{_+2}")
        headerList.append(f"T3-NG|{_}+{_+2}")

    headerList.append(f"T3-I|S")
    headerList.append(f"T3-PF|S")
    headerList.append(f"T3-RF|S")
    headerList.append(f"T3-NG|S")

    headerList.append(f"T3-I|M")
    headerList.append(f"T3-PF|M")
    headerList.append(f"T3-RF|M")
    headerList.append(f"T3-NG|M")

    headerList.append(f"T3-I|VAR")
    headerList.append(f"T3-PF|VAR")
    headerList.append(f"T3-RF|VAR")
    headerList.append(f"T3-NG|VAR")

    headerList.append(f"T3-I|SD")
    headerList.append(f"T3-PF|SD")
    headerList.append(f"T3-RF|SD")
    headerList.append(f"T3-NG|SD")

    for _ in range(8-3):
        headerList.append(f"T4-I|{_}+{_+3}")
        headerList.append(f"T4-PF|{_}+{_+3}")
        headerList.append(f"T4-RF|{_}+{_+3}")
        headerList.append(f"T4-NG|{_}+{_+3}")

    headerList.append(f"T4-I|S")
    headerList.append(f"T4-PF|S")
    headerList.append(f"T4-RF|S")
    headerList.append(f"T4-NG|S")

    headerList.append(f"T4-I|M")
    headerList.append(f"T4-PF|M")
    headerList.append(f"T4-RF|M")
    headerList.append(f"T4-NG|M")

    headerList.append(f"T4-I|VAR")
    headerList.append(f"T4-PF|VAR")
    headerList.append(f"T4-RF|VAR")
    headerList.append(f"T4-NG|VAR")

    headerList.append(f"T4-I|SD")
    headerList.append(f"T4-PF|SD")
    headerList.append(f"T4-RF|SD")
    headerList.append(f"T4-NG|SD")

    for _ in range(8-4):
        headerList.append(f"T5-I|{_}+{_+4}")
        headerList.append(f"T5-PF|{_}+{_+4}")
        headerList.append(f"T5-RF|{_}+{_+4}")
        headerList.append(f"T5-NG|{_}+{_+4}")
    headerList.append(f"T5-I|S")
    headerList.append(f"T5-PF|S")
    headerList.append(f"T5-RF|S")
    headerList.append(f"T5-NG|S")

    headerList.append(f"T5-I|M")
    headerList.append(f"T5-PF|M")
    headerList.append(f"T5-RF|M")
    headerList.append(f"T5-NG|M")

    headerList.append(f"T5-I|VAR")
    headerList.append(f"T5-PF|VAR")
    headerList.append(f"T5-RF|VAR")
    headerList.append(f"T5-NG|VAR")

    headerList.append(f"T5-I|SD")
    headerList.append(f"T5-PF|SD")
    headerList.append(f"T5-RF|SD")
    headerList.append(f"T5-NG|SD")

    for _ in range(8-5):
        headerList.append(f"T6-I|{_}+{_+5}")
        headerList.append(f"T6-PF|{_}+{_+5}")
        headerList.append(f"T6-RF|{_}+{_+5}")
        headerList.append(f"T6-NG|{_}+{_+5}")
    headerList.append(f"T6-I|S")
    headerList.append(f"T6-PF|S")
    headerList.append(f"T6-RF|S")
    headerList.append(f"T6-NG|S")

    headerList.append(f"T6-I|M")
    headerList.append(f"T6-PF|M")
    headerList.append(f"T6-RF|M")
    headerList.append(f"T6-NG|M")

    headerList.append(f"T6-I|VAR")
    headerList.append(f"T6-PF|VAR")
    headerList.append(f"T6-RF|VAR")
    headerList.append(f"T6-NG|VAR")

    headerList.append(f"T6-I|SD")
    headerList.append(f"T6-PF|SD")
    headerList.append(f"T6-RF|SD")
    headerList.append(f"T6-NG|SD")

    for _ in range(8-6):
        headerList.append(f"T7-I|{_}+{_+6}")
        headerList.append(f"T7-PF|{_}+{_+6}")
        headerList.append(f"T7-RF|{_}+{_+6}")
        headerList.append(f"T7-NG|{_}+{_+6}")

    headerList.append(f"T7-I|S")
    headerList.append(f"T7-PF|S")
    headerList.append(f"T7-RF|S")
    headerList.append(f"T7-NG|S")

    headerList.append(f"T7-I|M")
    headerList.append(f"T7-PF|M")
    headerList.append(f"T7-RF|M")
    headerList.append(f"T7-NG|M")

    headerList.append(f"T7-I|VAR")
    headerList.append(f"T7-PF|VAR")
    headerList.append(f"T7-RF|VAR")
    headerList.append(f"T7-NG|VAR")

    headerList.append(f"T7-I|SD")
    headerList.append(f"T7-PF|SD")
    headerList.append(f"T7-RF|SD")
    headerList.append(f"T7-NG|SD")

    for _ in range(8-7):
        headerList.append(f"T8-I|{_}+{_+7}")
        headerList.append(f"T8-PF|{_}+{_+7}")
        headerList.append(f"T8-RF|{_}+{_+7}")
        headerList.append(f"T8-NG|{_}+{_+7}")

with open(csv_path, 'w', newline='') as file:
        dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
        dw.writeheader()

print(f"CSV file will be created: {csv_path}")

with open(csv_path, 'a', newline='') as file:
    writer = csv.writer(file)
    
    # for outer in range(0, 800, 100):
    #     for first in range(0, 100):
    #         for second in range(0, 100):
    #             if second == first:
    #                 pass
    #             else:    
    #                 first_row = outer + first
    #                 placeholder = small_df.iloc[first_row].values.tolist()
    #                 sec_row = outer + second
    #                 placeholder.extend(small_df.iloc[sec_row, FEATURES_COL:].values.tolist())
    #                 writer.writerow([*placeholder])
    #                 placeholder.clear()

    # for outer in range(0, 800, 100):
    #     for first in range(0, 100):
    #         for second in range(0, 100):
    #             for third in range(0, 100):
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

    for outer in range(0, 800, 100):
        for first in range(0, 33):
            for second in range(33, 66):
                for third in range(66, 99):
                    if second == first or second == third or first == third:
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
