'''
alter dataset to have statistical features. class and seq not automatically added.
'''
import csv
import pandas as pd
import os
from statistics import fmean, stdev, variance

FULL_FEATURES = ["D", "I", "PF", "RF", "NG"]
SUB_FEATURES = ["I", "PF", "RF", "NG"]
STAT_FEATURES = ["S", "M", "VAR", "SD"]

CHAR_COUNT = 10 # minimum value of 5
CYCLE = 0
NGRAPH_COUNT = 0
MIDDLE_NGRAPH = 3 # do not change value.

namelist  = ["andy", "azfar", "ch", "cy", "gerald", "jc", "jonah", "qikai", "ys", "zen"]
export_csv_name = "base1" + ".csv"
export_csv_path = os.path.join(os.getcwd(), "03_pair", export_csv_name)

headerList = ['Subject']
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

two_dwell_list = []
two_int_list = []
two_pf_list = []
two_rf_list = []
two_ng_list = []

three_int_list = []
three_pf_list = []
three_rf_list = []
three_ng_list = []

four_int_list = []
four_pf_list = []
four_rf_list = []
four_ng_list = []

five_int_list = []
five_pf_list = []
five_rf_list = []
five_ng_list = []

six_int_list = []
six_pf_list = []
six_rf_list = []
six_ng_list = []

seven_int_list = []
seven_pf_list = []
seven_rf_list = []
seven_ng_list = []

eight_int_list = []
eight_pf_list = []
eight_rf_list = []
eight_ng_list = []

nine_int_list = []
nine_pf_list = []
nine_rf_list = []
nine_ng_list = []

# open CSV file and assign header
with open(export_csv_path, 'a', newline='') as file:
    dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
    dw.writeheader()

print(f"\nCSV file will be created: {export_csv_path}")

for name in namelist:
    merge_df = pd.read_csv("00_backup/" +  "df_" + name + ".csv")  
    merge_df.drop(merge_df[merge_df['press_time']=='press_time'].index, inplace=True)
    merge_df.drop(merge_df[merge_df['release_time']=='release_time'].index, inplace=True)
    merge_df = merge_df.astype({'press_time':'float', 'release_time': 'float'})

    with open(export_csv_path, 'a', newline='') as file:
        for body in range(0, 1000, 10):
            placeholder = [merge_df.iloc[body+0]["release_time"] - merge_df.iloc[body+0]["press_time"]]
            two_dwell_list.append(merge_df.iloc[body+0]["release_time"] - merge_df.iloc[body+0]["press_time"])
            for row in range(0, 9):
                body_row = body + row
                interval_time = merge_df.iloc[body_row+1]["press_time"] - merge_df.iloc[body_row]["release_time"]
                press_flight_time = merge_df.iloc[body_row+1]["press_time"] - merge_df.iloc[body_row]["press_time"]
                release_flight_time = merge_df.iloc[body_row+1]["release_time"] - merge_df.iloc[body_row]["release_time"]
                digraph_time = merge_df.iloc[body_row+1]["release_time"] - merge_df.iloc[body_row]["press_time"]
                later_dwell_time = merge_df.iloc[body_row+1]["release_time"] - merge_df.iloc[body_row+1]["press_time"]
                two_dwell_list.append(later_dwell_time)
                two_int_list.append(interval_time)
                two_pf_list.append(press_flight_time)
                two_rf_list.append(release_flight_time)
                two_ng_list.append(digraph_time)

                placeholder.extend([str(interval_time), str(press_flight_time),str(release_flight_time), str(digraph_time),
                str(later_dwell_time)])

            placeholder.extend([str(sum(two_dwell_list)), str(sum(two_int_list)), str(sum(two_pf_list)), str(sum(two_rf_list)), str(sum(two_ng_list)),
                str(fmean(two_dwell_list)), str(fmean(two_int_list)), str(fmean(two_pf_list)), str(fmean(two_rf_list)), str(fmean(two_ng_list)),
                str(variance(two_dwell_list)), str(variance(two_int_list)), str(variance(two_pf_list)), str(variance(two_rf_list)), str(variance(two_ng_list)),
                str(stdev(two_dwell_list)), str(stdev(two_int_list)), str(stdev(two_pf_list)), str(stdev(two_rf_list)), str(stdev(two_ng_list))])

            for row in range(0,8):
                body_row = body + row
                three_int_time = merge_df.iloc[body_row+2]["press_time"] - merge_df.iloc[body_row]["release_time"]
                three_pf_time = merge_df.iloc[body_row+2]["press_time"] - merge_df.iloc[body_row]["press_time"]
                three_rf_time = merge_df.iloc[body_row+2]["release_time"] - merge_df.iloc[body_row]["release_time"]
                three_graph_time = merge_df.iloc[body_row+2]["release_time"] - merge_df.iloc[body_row]["press_time"]
                placeholder.extend([str(three_int_time), str(three_pf_time), str(three_rf_time), str(three_graph_time)])
                three_int_list.append(three_int_time)
                three_pf_list.append(three_pf_time)
                three_rf_list.append(three_rf_time)
                three_ng_list.append(three_graph_time)
            
            placeholder.extend([str(sum(three_int_list)), str(sum(three_pf_list)), str(sum(three_rf_list)), str(sum(three_ng_list)),
                str(fmean(three_int_list)), str(fmean(three_pf_list)), str(fmean(three_rf_list)), str(fmean(three_ng_list)),
                str(variance(three_int_list)), str(variance(three_pf_list)), str(variance(three_rf_list)), str(variance(three_ng_list)),
                str(stdev(three_int_list)), str(stdev(three_pf_list)), str(stdev(three_rf_list)), str(stdev(three_ng_list))])

            for row in range(0,7):
                body_row = body + row
                four_int_time = merge_df.iloc[body_row+3]["press_time"] - merge_df.iloc[body_row]["release_time"]
                four_pf_time = merge_df.iloc[body_row+3]["press_time"] - merge_df.iloc[body_row]["press_time"]
                four_rf_time = merge_df.iloc[body_row+3]["release_time"] - merge_df.iloc[body_row]["release_time"]
                four_graph_time = merge_df.iloc[body_row+3]["release_time"] - merge_df.iloc[body_row]["press_time"]
                placeholder.extend([str(four_int_time), str(four_pf_time), str(four_rf_time), str(four_graph_time)])
                four_int_list.append(four_int_time)
                four_pf_list.append(four_pf_time)
                four_rf_list.append(four_rf_time)
                four_ng_list.append(four_graph_time)
            
            placeholder.extend([str(sum(four_int_list)), str(sum(four_pf_list)), str(sum(four_rf_list)), str(sum(four_ng_list)),
                str(fmean(four_int_list)), str(fmean(four_pf_list)), str(fmean(four_rf_list)), str(fmean(four_ng_list)),
                str(variance(four_int_list)), str(variance(four_pf_list)), str(variance(four_rf_list)), str(variance(four_ng_list)),
                str(stdev(four_int_list)), str(stdev(four_pf_list)), str(stdev(four_rf_list)), str(stdev(four_ng_list))])

            for row in range(0,6):
                body_row = body + row
                five_int_time = merge_df.iloc[body_row+4]["press_time"] - merge_df.iloc[body_row]["release_time"]
                five_pf_time = merge_df.iloc[body_row+4]["press_time"] - merge_df.iloc[body_row]["press_time"]
                five_rf_time = merge_df.iloc[body_row+4]["release_time"] - merge_df.iloc[body_row]["release_time"]
                five_graph_time = merge_df.iloc[body_row+4]["release_time"] - merge_df.iloc[body_row]["press_time"]
                placeholder.extend([str(five_int_time), str(five_pf_time), str(five_rf_time), str(five_graph_time)])
                five_int_list.append(five_int_time)
                five_pf_list.append(five_pf_time)
                five_rf_list.append(five_rf_time)
                five_ng_list.append(five_graph_time)
            
            placeholder.extend([str(sum(five_int_list)), str(sum(five_pf_list)), str(sum(five_rf_list)), str(sum(five_ng_list)),
                str(fmean(five_int_list)), str(fmean(five_pf_list)), str(fmean(five_rf_list)), str(fmean(five_ng_list)),
                str(variance(five_int_list)), str(variance(five_pf_list)), str(variance(five_rf_list)), str(variance(five_ng_list)),
                str(stdev(five_int_list)), str(stdev(five_pf_list)), str(stdev(five_rf_list)), str(stdev(five_ng_list))])

            for row in range(0,5):
                body_row = body + row
                six_int_time = merge_df.iloc[body_row+5]["press_time"] - merge_df.iloc[body_row]["release_time"]
                six_pf_time = merge_df.iloc[body_row+5]["press_time"] - merge_df.iloc[body_row]["press_time"]
                six_rf_time = merge_df.iloc[body_row+5]["release_time"] - merge_df.iloc[body_row]["release_time"]
                six_graph_time = merge_df.iloc[body_row+5]["release_time"] - merge_df.iloc[body_row]["press_time"]
                placeholder.extend([str(six_int_time), str(six_pf_time), str(six_rf_time), str(six_graph_time)])
                six_int_list.append(six_int_time)
                six_pf_list.append(six_pf_time)
                six_rf_list.append(six_rf_time)
                six_ng_list.append(six_graph_time)
            
            placeholder.extend([str(sum(six_int_list)), str(sum(six_pf_list)), str(sum(six_rf_list)), str(sum(six_ng_list)),
                str(fmean(six_int_list)), str(fmean(six_pf_list)), str(fmean(six_rf_list)), str(fmean(six_ng_list)),
                str(variance(six_int_list)), str(variance(six_pf_list)), str(variance(six_rf_list)), str(variance(six_ng_list)),
                str(stdev(six_int_list)), str(stdev(six_pf_list)), str(stdev(six_rf_list)), str(stdev(six_ng_list))])

            for row in range(0,4):
                body_row = body + row
                seven_int_time = merge_df.iloc[body_row+6]["press_time"] - merge_df.iloc[body_row]["release_time"]
                seven_pf_time = merge_df.iloc[body_row+6]["press_time"] - merge_df.iloc[body_row]["press_time"]
                seven_rf_time = merge_df.iloc[body_row+6]["release_time"] - merge_df.iloc[body_row]["release_time"]
                seven_graph_time = merge_df.iloc[body_row+6]["release_time"] - merge_df.iloc[body_row]["press_time"]
                placeholder.extend([str(seven_int_time), str(seven_pf_time), str(seven_rf_time), str(seven_graph_time)])
                seven_int_list.append(seven_int_time)
                seven_pf_list.append(seven_pf_time)
                seven_rf_list.append(seven_rf_time)
                seven_ng_list.append(seven_graph_time)
            
            placeholder.extend([str(sum(seven_int_list)), str(sum(seven_pf_list)), str(sum(seven_rf_list)), str(sum(seven_ng_list)),
                str(fmean(seven_int_list)), str(fmean(seven_pf_list)), str(fmean(seven_rf_list)), str(fmean(seven_ng_list)),
                str(variance(seven_int_list)), str(variance(seven_pf_list)), str(variance(seven_rf_list)), str(variance(seven_ng_list)),
                str(stdev(seven_int_list)), str(stdev(seven_pf_list)), str(stdev(seven_rf_list)), str(stdev(seven_ng_list))])

            for row in range(0,3):
                body_row = body + row
                eight_int_time = merge_df.iloc[body_row+7]["press_time"] - merge_df.iloc[body_row]["release_time"]
                eight_pf_time = merge_df.iloc[body_row+7]["press_time"] - merge_df.iloc[body_row]["press_time"]
                eight_rf_time = merge_df.iloc[body_row+7]["release_time"] - merge_df.iloc[body_row]["release_time"]
                eight_graph_time = merge_df.iloc[body_row+7]["release_time"] - merge_df.iloc[body_row]["press_time"]
                placeholder.extend([str(eight_int_time), str(eight_pf_time), str(eight_rf_time), str(eight_graph_time)])
                eight_int_list.append(eight_int_time)
                eight_pf_list.append(eight_pf_time)
                eight_rf_list.append(eight_rf_time)
                eight_ng_list.append(eight_graph_time)
            
            placeholder.extend([str(sum(eight_int_list)), str(sum(eight_pf_list)), str(sum(eight_rf_list)), str(sum(eight_ng_list)),
                str(fmean(eight_int_list)), str(fmean(eight_pf_list)), str(fmean(eight_rf_list)), str(fmean(eight_ng_list)),
                str(variance(eight_int_list)), str(variance(eight_pf_list)), str(variance(eight_rf_list)), str(variance(eight_ng_list)),
                str(stdev(eight_int_list)), str(stdev(eight_pf_list)), str(stdev(eight_rf_list)), str(stdev(eight_ng_list))])

            for row in range(0,2):
                body_row = body + row
                nine_int_time = merge_df.iloc[body_row+8]["press_time"] - merge_df.iloc[body_row]["release_time"]
                nine_pf_time = merge_df.iloc[body_row+8]["press_time"] - merge_df.iloc[body_row]["press_time"]
                nine_rf_time = merge_df.iloc[body_row+8]["release_time"] - merge_df.iloc[body_row]["release_time"]
                nine_graph_time = merge_df.iloc[body_row+8]["release_time"] - merge_df.iloc[body_row]["press_time"]
                placeholder.extend([str(nine_int_time), str(nine_pf_time), str(nine_rf_time), str(nine_graph_time)])
                nine_int_list.append(nine_int_time)
                nine_pf_list.append(nine_pf_time)
                nine_rf_list.append(nine_rf_time)
                nine_ng_list.append(nine_graph_time)
            
            placeholder.extend([str(sum(nine_int_list)), str(sum(nine_pf_list)), str(sum(nine_rf_list)), str(sum(nine_ng_list)),
                str(fmean(nine_int_list)), str(fmean(nine_pf_list)), str(fmean(nine_rf_list)), str(fmean(nine_ng_list)),
                str(variance(nine_int_list)), str(variance(nine_pf_list)), str(variance(nine_rf_list)), str(variance(nine_ng_list)),
                str(stdev(nine_int_list)), str(stdev(nine_pf_list)), str(stdev(nine_rf_list)), str(stdev(nine_ng_list))])

            for row in range(0,1):
                body_row = body + row
                ten_int_time = merge_df.iloc[body_row+9]["press_time"] - merge_df.iloc[body_row]["release_time"]
                ten_pf_time = merge_df.iloc[body_row+9]["press_time"] - merge_df.iloc[body_row]["press_time"]
                ten_rf_time = merge_df.iloc[body_row+9]["release_time"] - merge_df.iloc[body_row]["release_time"]
                ten_graph_time = merge_df.iloc[body_row+9]["release_time"] - merge_df.iloc[body_row]["press_time"]
                placeholder.extend([str(ten_int_time), str(ten_pf_time), str(ten_rf_time), str(ten_graph_time)])

            writer = csv.writer(file)
            writer.writerow([name, *placeholder])
            placeholder.clear()

            two_dwell_list.clear()
            two_int_list.clear()
            two_pf_list.clear()
            two_rf_list.clear()
            two_ng_list.clear()

            three_int_list.clear()
            three_pf_list.clear()
            three_rf_list.clear()
            three_ng_list.clear()

            four_int_list.clear()
            four_pf_list.clear()
            four_rf_list.clear()
            four_ng_list.clear()

            five_int_list.clear()
            five_pf_list.clear()
            five_rf_list.clear()
            five_ng_list.clear()
            
            six_int_list.clear()
            six_pf_list.clear()
            six_rf_list.clear()
            six_ng_list.clear()

            seven_int_list.clear()
            seven_pf_list.clear()
            seven_rf_list.clear()
            seven_ng_list.clear()

            eight_int_list.clear()
            eight_pf_list.clear()
            eight_rf_list.clear()
            eight_ng_list.clear()

            nine_int_list.clear()
            nine_pf_list.clear()
            nine_rf_list.clear()
            nine_ng_list.clear()

print(f"\nCSV file has been altered and saved at: {export_csv_path}")