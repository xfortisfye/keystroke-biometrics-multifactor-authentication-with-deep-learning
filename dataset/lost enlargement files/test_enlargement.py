'''
increase dataset
'''
import time
import csv
import pandas as pd
import os
from sys import exit

export_dir_path = os.path.join(os.getcwd(), "export")
csv_name = "m2m_test_flex" + ".csv"
csv_path = os.path.join(export_dir_path, csv_name)

small_df = pd.read_csv("dataset/" + "test_flex.csv")

headerList = ['Subject', 'Seq_No', 'Sequence']
for _ in range(2):
    headerList.append(f"D|0")
    for _ in range(10-1):
        headerList.append(f"I|{_}+{_+1}")
        headerList.append(f"PF|{_}+{_+1}")
        headerList.append(f"RF|{_}+{_+1}")
        headerList.append(f"G|{_}+{_+1}")
        headerList.append(f"D|{_+1}")
    headerList.append(f"T2-D-S")
    headerList.append(f"T2-I-S")
    headerList.append(f"T2-PF-S")
    headerList.append(f"T2-RF-S")
    headerList.append(f"T2-G-S")

    headerList.append(f"T2-D-M")
    headerList.append(f"T2-I-M")
    headerList.append(f"T2-PF-M")
    headerList.append(f"T2-RF-M")
    headerList.append(f"T2-G-M")

    headerList.append(f"T2-D-VAR")
    headerList.append(f"T2-I-VAR")
    headerList.append(f"T2-PF-VAR")
    headerList.append(f"T2-RF-VAR")
    headerList.append(f"T2-G-VAR")

    headerList.append(f"T2-D-SD")
    headerList.append(f"T2-I-SD")
    headerList.append(f"T2-PF-SD")
    headerList.append(f"T2-RF-SD")
    headerList.append(f"T2-G-SD")

    for _ in range(10-2):
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

    for _ in range(10-3):
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

    for _ in range(10-4):
        headerList.append(f"T5_I|{_}+{_+4}")
        headerList.append(f"T5_PF|{_}+{_+4}")
        headerList.append(f"T5_RF|{_}+{_+4}")
        headerList.append(f"T5_G|{_}+{_+4}")
    headerList.append(f"T5-I-S")
    headerList.append(f"T5-PF-S")
    headerList.append(f"T5-RF-S")
    headerList.append(f"T5-G-S")

    headerList.append(f"T5-I-M")
    headerList.append(f"T5-PF-M")
    headerList.append(f"T5-RF-M")
    headerList.append(f"T5-G-M")

    headerList.append(f"T5-I-VAR")
    headerList.append(f"T5-PF-VAR")
    headerList.append(f"T5-RF-VAR")
    headerList.append(f"T5-G-VAR")

    headerList.append(f"T5-I-SD")
    headerList.append(f"T5-PF-SD")
    headerList.append(f"T5-RF-SD")
    headerList.append(f"T5-G-SD")

    for _ in range(10-5):
        headerList.append(f"T6_I|{_}+{_+5}")
        headerList.append(f"T6_PF|{_}+{_+5}")
        headerList.append(f"T6_RF|{_}+{_+5}")
        headerList.append(f"T6_G|{_}+{_+5}")
    headerList.append(f"T6-I-S")
    headerList.append(f"T6-PF-S")
    headerList.append(f"T6-RF-S")
    headerList.append(f"T6-G-S")

    headerList.append(f"T6-I-M")
    headerList.append(f"T6-PF-M")
    headerList.append(f"T6-RF-M")
    headerList.append(f"T6-G-M")

    headerList.append(f"T6-I-VAR")
    headerList.append(f"T6-PF-VAR")
    headerList.append(f"T6-RF-VAR")
    headerList.append(f"T6-G-VAR")

    headerList.append(f"T6-I-SD")
    headerList.append(f"T6-PF-SD")
    headerList.append(f"T6-RF-SD")
    headerList.append(f"T6-G-SD")

    for _ in range(10-6):
        headerList.append(f"T7_I|{_}+{_+6}")
        headerList.append(f"T7_PF|{_}+{_+6}")
        headerList.append(f"T7_RF|{_}+{_+6}")
        headerList.append(f"T7_G|{_}+{_+6}")

    headerList.append(f"T7-I-S")
    headerList.append(f"T7-PF-S")
    headerList.append(f"T7-RF-S")
    headerList.append(f"T7-G-S")

    headerList.append(f"T7-I-M")
    headerList.append(f"T7-PF-M")
    headerList.append(f"T7-RF-M")
    headerList.append(f"T7-G-M")

    headerList.append(f"T7-I-VAR")
    headerList.append(f"T7-PF-VAR")
    headerList.append(f"T7-RF-VAR")
    headerList.append(f"T7-G-VAR")

    headerList.append(f"T7-I-SD")
    headerList.append(f"T7-PF-SD")
    headerList.append(f"T7-RF-SD")
    headerList.append(f"T7-G-SD")

    for _ in range(10-7):
        headerList.append(f"T8_I|{_}+{_+7}")
        headerList.append(f"T8_PF|{_}+{_+7}")
        headerList.append(f"T8_RF|{_}+{_+7}")
        headerList.append(f"T8_G|{_}+{_+7}")

    headerList.append(f"T8-I-S")
    headerList.append(f"T8-PF-S")
    headerList.append(f"T8-RF-S")
    headerList.append(f"T8-G-S")

    headerList.append(f"T8-I-M")
    headerList.append(f"T8-PF-M")
    headerList.append(f"T8-RF-M")
    headerList.append(f"T8-G-M")

    headerList.append(f"T8-I-VAR")
    headerList.append(f"T8-PF-VAR")
    headerList.append(f"T8-RF-VAR")
    headerList.append(f"T8-G-VAR")

    headerList.append(f"T8-I-SD")
    headerList.append(f"T8-PF-SD")
    headerList.append(f"T8-RF-SD")
    headerList.append(f"T8-G-SD")


    for _ in range(10-8):
        headerList.append(f"T9_I|{_}+{_+8}")
        headerList.append(f"T9_PF|{_}+{_+8}")
        headerList.append(f"T9_RF|{_}+{_+8}")
        headerList.append(f"T9_G|{_}+{_+8}")
        
    headerList.append(f"T9-I-S")
    headerList.append(f"T9-PF-S")
    headerList.append(f"T9-RF-S")
    headerList.append(f"T9-G-S")

    headerList.append(f"T9-I-M")
    headerList.append(f"T9-PF-M")
    headerList.append(f"T9-RF-M")
    headerList.append(f"T9-G-M")

    headerList.append(f"T9-I-VAR")
    headerList.append(f"T9-PF-VAR")
    headerList.append(f"T9-RF-VAR")
    headerList.append(f"T9-G-VAR")

    headerList.append(f"T9-I-SD")
    headerList.append(f"T9-PF-SD")
    headerList.append(f"T9-RF-SD")
    headerList.append(f"T9-G-SD")

    for _ in range(10-9):
        headerList.append(f"T10_I|{_}+{_+9}")
        headerList.append(f"T10_PF|{_}+{_+9}")
        headerList.append(f"T10_RF|{_}+{_+9}")
        headerList.append(f"T10_G|{_}+{_+9}")


with open(csv_path, 'w', newline='') as file:
        dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
        dw.writeheader()

print(f"CSV file will be created: {csv_path}")

with open(csv_path, 'a', newline='') as file:
    writer = csv.writer(file)
        
    for outer in range(0, 80, 8):
        for row in range(0, 2):
            for inside in range(2, 8):
                outerrow = outer + row
                placeholder = small_df.iloc[outerrow].values.tolist()
                
                insiderow = outer + inside
                placeholder.extend(small_df.iloc[insiderow, 3:].values.tolist())

                writer.writerow([*placeholder])
                placeholder.clear()

        for row in range(2, 4):
            # four
            for inside in range(0, 2):
                outerrow = outer + row
                placeholder = small_df.iloc[outerrow].values.tolist()
                
                insiderow = outer + inside
                placeholder.extend(small_df.iloc[insiderow, 3:].values.tolist())

                writer.writerow([*placeholder])
                placeholder.clear()

            for inside in range(4, 8):
                outerrow = outer + row
                placeholder = small_df.iloc[outerrow].values.tolist()
                
                insiderow = outer + inside
                placeholder.extend(small_df.iloc[insiderow, 3:].values.tolist())

                writer.writerow([*placeholder])
                placeholder.clear()

        for row in range(4, 6):
            # five
            for inside in range(0, 4):
                outerrow = outer + row
                placeholder = small_df.iloc[outerrow].values.tolist()
                
                insiderow = outer + inside
                placeholder.extend(small_df.iloc[insiderow, 3:].values.tolist())

                writer.writerow([*placeholder])
                placeholder.clear()

            for inside in range(6, 8):
                outerrow = outer + row
                placeholder = small_df.iloc[outerrow].values.tolist()
                
                insiderow = outer + inside
                placeholder.extend(small_df.iloc[insiderow, 3:].values.tolist())

                writer.writerow([*placeholder])
                placeholder.clear()

        for row in range(6, 8):
            # six
            for inside in range(0, 6):
                outerrow = outer + row
                placeholder = small_df.iloc[outerrow].values.tolist()
                
                insiderow = outer + inside
                placeholder.extend(small_df.iloc[insiderow, 3:].values.tolist())

                writer.writerow([*placeholder])
                placeholder.clear()