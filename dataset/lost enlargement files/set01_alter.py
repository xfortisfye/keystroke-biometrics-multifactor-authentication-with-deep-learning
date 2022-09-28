'''
fabricate data
'''
import time
import csv
import pandas as pd
import os
from sys import exit
from statistics import fmean, stdev, variance

namelist  = ["andy", "azfar", "ch", "cy", "gerald", "jc", "jonah", "qikai", "ys", "zen"]

export_dir_path = os.path.join(os.getcwd(), "export")
csv_name = "multigraph" + ".csv"
csv_path = os.path.join(export_dir_path, csv_name)

headerList = ['Subject']
headerList.append(f"T2-D|0")
for _ in range(10-1):
    headerList.append(f"T2-I|{_}+{_+1}")
    headerList.append(f"T2-PF|{_}+{_+1}")
    headerList.append(f"T2-RF|{_}+{_+1}")
    headerList.append(f"T2-NG|{_}+{_+1}")
    headerList.append(f"T2-D|{_+1}")
headerList.append(f"T2-D|S")
headerList.append(f"T2-I|S")
headerList.append(f"T2-PF|S")
headerList.append(f"T2-RF|S")
headerList.append(f"T2-DT-S")

headerList.append(f"T2-D|M")
headerList.append(f"T2-I|M")
headerList.append(f"T2-PF|M")
headerList.append(f"T2-RF|M")
headerList.append(f"T2-DT-M")

headerList.append(f"T2-D|VAR")
headerList.append(f"T2-I|VAR")
headerList.append(f"T2-PF|VAR")
headerList.append(f"T2-RF|VAR")
headerList.append(f"T2-DT-VAR")

headerList.append(f"T2-D|SD")
headerList.append(f"T2-I|SD")
headerList.append(f"T2-PF|SD")
headerList.append(f"T2-RF|SD")
headerList.append(f"T2-DT-SD")

for _ in range(10-2):
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

for _ in range(10-3):
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

for _ in range(10-4):
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

for _ in range(10-5):
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

for _ in range(10-6):
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

for _ in range(10-7):
    headerList.append(f"T8-I|{_}+{_+7}")
    headerList.append(f"T8-PF|{_}+{_+7}")
    headerList.append(f"T8-RF|{_}+{_+7}")
    headerList.append(f"T8-NG|{_}+{_+7}")

headerList.append(f"T8-I|S")
headerList.append(f"T8-PF|S")
headerList.append(f"T8-RF|S")
headerList.append(f"T8-NG|S")

headerList.append(f"T8-I|M")
headerList.append(f"T8-PF|M")
headerList.append(f"T8-RF|M")
headerList.append(f"T8-NG|M")

headerList.append(f"T8-I|VAR")
headerList.append(f"T8-PF|VAR")
headerList.append(f"T8-RF|VAR")
headerList.append(f"T8-NG|VAR")

headerList.append(f"T8-I|SD")
headerList.append(f"T8-PF|SD")
headerList.append(f"T8-RF|SD")
headerList.append(f"T8-NG|SD")


for _ in range(10-8):
    headerList.append(f"T9-I|{_}+{_+8}")
    headerList.append(f"T9-PF|{_}+{_+8}")
    headerList.append(f"T9-RF|{_}+{_+8}")
    headerList.append(f"T9-NG|{_}+{_+8}")
    
headerList.append(f"T9-I|S")
headerList.append(f"T9-PF|S")
headerList.append(f"T9-RF|S")
headerList.append(f"T9-NG|S")

headerList.append(f"T9-I|M")
headerList.append(f"T9-PF|M")
headerList.append(f"T9-RF|M")
headerList.append(f"T9-NG|M")

headerList.append(f"T9-I|VAR")
headerList.append(f"T9-PF|VAR")
headerList.append(f"T9-RF|VAR")
headerList.append(f"T9-NG|VAR")

headerList.append(f"T9-I|SD")
headerList.append(f"T9-PF|SD")
headerList.append(f"T9-RF|SD")
headerList.append(f"T9-NG|SD")

for _ in range(10-9):
    headerList.append(f"T10-I|{_}+{_+9}")
    headerList.append(f"T10-PF|{_}+{_+9}")
    headerList.append(f"T10-RF|{_}+{_+9}")
    headerList.append(f"T10-NG|{_}+{_+9}")
# headerList.append(f"T10-I|M")
# headerList.append(f"T10-PF|M")
# headerList.append(f"T10-RF|M")
# headerList.append(f"T10-NG|M")

# headerList.append(f"T10-I|VAR")
# headerList.append(f"T10-PF|VAR")
# headerList.append(f"T10-RF|VAR")
# headerList.append(f"T10-NG|VAR")

# headerList.append(f"T10-I|SD")
# headerList.append(f"T10-PF|SD")
# headerList.append(f"T10-RF|SD")
# headerList.append(f"T10-NG|SD")

two_dwell_list = []
two_int_list = []
two_pf_list = []
two_rf_list = []
two_g_list = []

three_int_list = []
three_pf_list = []
three_rf_list = []
three_g_list = []

four_int_list = []
four_pf_list = []
four_rf_list = []
four_g_list = []

five_int_list = []
five_pf_list = []
five_rf_list = []
five_g_list = []

six_int_list = []
six_pf_list = []
six_rf_list = []
six_g_list = []

seven_int_list = []
seven_pf_list = []
seven_rf_list = []
seven_g_list = []

eight_int_list = []
eight_pf_list = []
eight_rf_list = []
eight_g_list = []

nine_int_list = []
nine_pf_list = []
nine_rf_list = []
nine_g_list = []

# ten_int_list = []
# ten_pf_list = []
# ten_rf_list = []
# ten_g_list = []


# open CSV file and assign header
with open(csv_path, 'a', newline='') as file:
    dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
    dw.writeheader()

print(f"CSV file will be created: {csv_path}")

for name in namelist:
    # export_dir_path = os.path.join(os.getcwd(), "export")
    # csv_name = name + "_digraph" + ".csv"
    # csv_name = "multigraph" + ".csv"
    # csv_path = os.path.join(export_dir_path, csv_name)

    # headerList = ['Subject']
    # headerList.append(f"T2-D|0")
    # for _ in range(10-1):
    #     headerList.append(f"T2-I|{_}+{_+1}")
    #     headerList.append(f"T2-PF|{_}+{_+1}")
    #     headerList.append(f"T2-RF|{_}+{_+1}")
    #     headerList.append(f"T2-NG|{_}+{_+1}")
    #     headerList.append(f"T2-D|{_+1}")

    # for _ in range(10-2):
    #     headerList.append(f"T3-I|{_}+{_+2}")
    #     headerList.append(f"T3-PF|{_}+{_+2}")
    #     headerList.append(f"T3-RF|{_}+{_+2}")
    #     headerList.append(f"T3-NG|{_}+{_+2}")

    # for _ in range(10-3):
    #     headerList.append(f"T4-I|{_}+{_+3}")
    #     headerList.append(f"T4-PF|{_}+{_+3}")
    #     headerList.append(f"T4-RF|{_}+{_+3}")
    #     headerList.append(f"T4-NG|{_}+{_+3}")

    # for _ in range(10-4):
    #     headerList.append(f"T5-I|{_}+{_+4}")
    #     headerList.append(f"T5-PF|{_}+{_+4}")
    #     headerList.append(f"T5-RF|{_}+{_+4}")
    #     headerList.append(f"T5-NG|{_}+{_+4}")

    # for _ in range(10-5):
    #     headerList.append(f"T6-I|{_}+{_+5}")
    #     headerList.append(f"T6-PF|{_}+{_+5}")
    #     headerList.append(f"T6-RF|{_}+{_+5}")
    #     headerList.append(f"T6-NG|{_}+{_+5}")

    # for _ in range(10-6):
    #     headerList.append(f"T7-I|{_}+{_+6}")
    #     headerList.append(f"T7-PF|{_}+{_+6}")
    #     headerList.append(f"T7-RF|{_}+{_+6}")
    #     headerList.append(f"T7-NG|{_}+{_+6}")

    # for _ in range(10-7):
    #     headerList.append(f"T8-I|{_}+{_+7}")
    #     headerList.append(f"T8-PF|{_}+{_+7}")
    #     headerList.append(f"T8-RF|{_}+{_+7}")
    #     headerList.append(f"T8-NG|{_}+{_+7}")

    # for _ in range(10-8):
    #     headerList.append(f"T9-I|{_}+{_+8}")
    #     headerList.append(f"T9-PF|{_}+{_+8}")
    #     headerList.append(f"T9-RF|{_}+{_+8}")
    #     headerList.append(f"T9-NG|{_}+{_+8}")
    
    # for _ in range(10-9):
    #     headerList.append(f"T10-I|{_}+{_+9}")
    #     headerList.append(f"T10-PF|{_}+{_+9}")
    #     headerList.append(f"T10-RF|{_}+{_+9}")
    #     headerList.append(f"T10-NG|{_}+{_+9}")

    # # open CSV file and assign header
    # with open(csv_path, 'a', newline='') as file:
    #     dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
    #     dw.writeheader()

    # print(f"CSV file will be created: {csv_path}")

    merge_df = pd.read_csv("dataset/invalid_original/" + name + "_merge_df.csv")  
    merge_df.drop(merge_df[merge_df['press_time']=='press_time'].index, inplace=True)
    merge_df.drop(merge_df[merge_df['release_time']=='release_time'].index, inplace=True)
    merge_df = merge_df.astype({'press_time':'float', 'release_time': 'float'})
    # print(merge_df)

    with open(csv_path, 'a', newline='') as file:
        
        # sequence = ""
        for outer in range(0, 1000, 10):
            placeholder = [merge_df.iloc[outer+0]["release_time"] - merge_df.iloc[outer+0]["press_time"]]
            two_dwell_list.append(merge_df.iloc[outer+0]["release_time"] - merge_df.iloc[outer+0]["press_time"])
            for row in range(0, 9):
                outerrow = outer + row
                interval_time = merge_df.iloc[outerrow+1]["press_time"] - merge_df.iloc[outerrow]["release_time"]
                press_flight_time = merge_df.iloc[outerrow+1]["press_time"] - merge_df.iloc[outerrow]["press_time"]
                release_flight_time = merge_df.iloc[outerrow+1]["release_time"] - merge_df.iloc[outerrow]["release_time"]
                digraph_time = merge_df.iloc[outerrow+1]["release_time"] - merge_df.iloc[outerrow]["press_time"]
                later_dwell_time = merge_df.iloc[outerrow+1]["release_time"] - merge_df.iloc[outerrow+1]["press_time"]
                two_dwell_list.append(later_dwell_time)
                two_int_list.append(interval_time)
                two_pf_list.append(press_flight_time)
                two_rf_list.append(release_flight_time)
                two_g_list.append(digraph_time)

                placeholder.extend([str(interval_time), str(press_flight_time),str(release_flight_time), str(digraph_time),
                str(later_dwell_time)])

            placeholder.extend([str(sum(two_dwell_list)), str(sum(two_int_list)), str(sum(two_pf_list)), str(sum(two_rf_list)), str(sum(two_g_list)),
                str(fmean(two_dwell_list)), str(fmean(two_int_list)), str(fmean(two_pf_list)), str(fmean(two_rf_list)), str(fmean(two_g_list)),
                str(variance(two_dwell_list)), str(variance(two_int_list)), str(variance(two_pf_list)), str(variance(two_rf_list)), str(variance(two_g_list)),
                str(stdev(two_dwell_list)), str(stdev(two_int_list)), str(stdev(two_pf_list)), str(stdev(two_rf_list)), str(stdev(two_g_list))])

            for row in range(0,8):
                outerrow = outer + row
                three_int_time = merge_df.iloc[outerrow+2]["press_time"] - merge_df.iloc[outerrow]["release_time"]
                three_pf_time = merge_df.iloc[outerrow+2]["press_time"] - merge_df.iloc[outerrow]["press_time"]
                three_rf_time = merge_df.iloc[outerrow+2]["release_time"] - merge_df.iloc[outerrow]["release_time"]
                three_graph_time = merge_df.iloc[outerrow+2]["release_time"] - merge_df.iloc[outerrow]["press_time"]
                placeholder.extend([str(three_int_time), str(three_pf_time), str(three_rf_time), str(three_graph_time)])
                three_int_list.append(three_int_time)
                three_pf_list.append(three_pf_time)
                three_rf_list.append(three_rf_time)
                three_g_list.append(three_graph_time)
            
            placeholder.extend([str(sum(three_int_list)), str(sum(three_pf_list)), str(sum(three_rf_list)), str(sum(three_g_list)),
                str(fmean(three_int_list)), str(fmean(three_pf_list)), str(fmean(three_rf_list)), str(fmean(three_g_list)),
                str(variance(three_int_list)), str(variance(three_pf_list)), str(variance(three_rf_list)), str(variance(three_g_list)),
                str(stdev(three_int_list)), str(stdev(three_pf_list)), str(stdev(three_rf_list)), str(stdev(three_g_list))])


            for row in range(0,7):
                outerrow = outer + row
                four_int_time = merge_df.iloc[outerrow+3]["press_time"] - merge_df.iloc[outerrow]["release_time"]
                four_pf_time = merge_df.iloc[outerrow+3]["press_time"] - merge_df.iloc[outerrow]["press_time"]
                four_rf_time = merge_df.iloc[outerrow+3]["release_time"] - merge_df.iloc[outerrow]["release_time"]
                four_graph_time = merge_df.iloc[outerrow+3]["release_time"] - merge_df.iloc[outerrow]["press_time"]
                placeholder.extend([str(four_int_time), str(four_pf_time), str(four_rf_time), str(four_graph_time)])
                four_int_list.append(four_int_time)
                four_pf_list.append(four_pf_time)
                four_rf_list.append(four_rf_time)
                four_g_list.append(four_graph_time)
            
            placeholder.extend([str(sum(four_int_list)), str(sum(four_pf_list)), str(sum(four_rf_list)), str(sum(four_g_list)),
                str(fmean(four_int_list)), str(fmean(four_pf_list)), str(fmean(four_rf_list)), str(fmean(four_g_list)),
                str(variance(four_int_list)), str(variance(four_pf_list)), str(variance(four_rf_list)), str(variance(four_g_list)),
                str(stdev(four_int_list)), str(stdev(four_pf_list)), str(stdev(four_rf_list)), str(stdev(four_g_list))])

  

            for row in range(0,6):
                outerrow = outer + row
                five_int_time = merge_df.iloc[outerrow+4]["press_time"] - merge_df.iloc[outerrow]["release_time"]
                five_pf_time = merge_df.iloc[outerrow+4]["press_time"] - merge_df.iloc[outerrow]["press_time"]
                five_rf_time = merge_df.iloc[outerrow+4]["release_time"] - merge_df.iloc[outerrow]["release_time"]
                five_graph_time = merge_df.iloc[outerrow+4]["release_time"] - merge_df.iloc[outerrow]["press_time"]
                placeholder.extend([str(five_int_time), str(five_pf_time), str(five_rf_time), str(five_graph_time)])
                five_int_list.append(five_int_time)
                five_pf_list.append(five_pf_time)
                five_rf_list.append(five_rf_time)
                five_g_list.append(five_graph_time)
            
            placeholder.extend([str(sum(five_int_list)), str(sum(five_pf_list)), str(sum(five_rf_list)), str(sum(five_g_list)),
                str(fmean(five_int_list)), str(fmean(five_pf_list)), str(fmean(five_rf_list)), str(fmean(five_g_list)),
                str(variance(five_int_list)), str(variance(five_pf_list)), str(variance(five_rf_list)), str(variance(five_g_list)),
                str(stdev(five_int_list)), str(stdev(five_pf_list)), str(stdev(five_rf_list)), str(stdev(five_g_list))])


            for row in range(0,5):
                outerrow = outer + row
                six_int_time = merge_df.iloc[outerrow+5]["press_time"] - merge_df.iloc[outerrow]["release_time"]
                six_pf_time = merge_df.iloc[outerrow+5]["press_time"] - merge_df.iloc[outerrow]["press_time"]
                six_rf_time = merge_df.iloc[outerrow+5]["release_time"] - merge_df.iloc[outerrow]["release_time"]
                six_graph_time = merge_df.iloc[outerrow+5]["release_time"] - merge_df.iloc[outerrow]["press_time"]
                placeholder.extend([str(six_int_time), str(six_pf_time), str(six_rf_time), str(six_graph_time)])
                six_int_list.append(six_int_time)
                six_pf_list.append(six_pf_time)
                six_rf_list.append(six_rf_time)
                six_g_list.append(six_graph_time)
            
            placeholder.extend([str(sum(six_int_list)), str(sum(six_pf_list)), str(sum(six_rf_list)), str(sum(six_g_list)),
                str(fmean(six_int_list)), str(fmean(six_pf_list)), str(fmean(six_rf_list)), str(fmean(six_g_list)),
                str(variance(six_int_list)), str(variance(six_pf_list)), str(variance(six_rf_list)), str(variance(six_g_list)),
                str(stdev(six_int_list)), str(stdev(six_pf_list)), str(stdev(six_rf_list)), str(stdev(six_g_list))])


            for row in range(0,4):
                outerrow = outer + row
                seven_int_time = merge_df.iloc[outerrow+6]["press_time"] - merge_df.iloc[outerrow]["release_time"]
                seven_pf_time = merge_df.iloc[outerrow+6]["press_time"] - merge_df.iloc[outerrow]["press_time"]
                seven_rf_time = merge_df.iloc[outerrow+6]["release_time"] - merge_df.iloc[outerrow]["release_time"]
                seven_graph_time = merge_df.iloc[outerrow+6]["release_time"] - merge_df.iloc[outerrow]["press_time"]
                placeholder.extend([str(seven_int_time), str(seven_pf_time), str(seven_rf_time), str(seven_graph_time)])
                seven_int_list.append(seven_int_time)
                seven_pf_list.append(seven_pf_time)
                seven_rf_list.append(seven_rf_time)
                seven_g_list.append(seven_graph_time)
            
            placeholder.extend([str(sum(seven_int_list)), str(sum(seven_pf_list)), str(sum(seven_rf_list)), str(sum(seven_g_list)),
                str(fmean(seven_int_list)), str(fmean(seven_pf_list)), str(fmean(seven_rf_list)), str(fmean(seven_g_list)),
                str(variance(seven_int_list)), str(variance(seven_pf_list)), str(variance(seven_rf_list)), str(variance(seven_g_list)),
                str(stdev(seven_int_list)), str(stdev(seven_pf_list)), str(stdev(seven_rf_list)), str(stdev(seven_g_list))])


            for row in range(0,3):
                outerrow = outer + row
                eight_int_time = merge_df.iloc[outerrow+7]["press_time"] - merge_df.iloc[outerrow]["release_time"]
                eight_pf_time = merge_df.iloc[outerrow+7]["press_time"] - merge_df.iloc[outerrow]["press_time"]
                eight_rf_time = merge_df.iloc[outerrow+7]["release_time"] - merge_df.iloc[outerrow]["release_time"]
                eight_graph_time = merge_df.iloc[outerrow+7]["release_time"] - merge_df.iloc[outerrow]["press_time"]
                placeholder.extend([str(eight_int_time), str(eight_pf_time), str(eight_rf_time), str(eight_graph_time)])
                eight_int_list.append(eight_int_time)
                eight_pf_list.append(eight_pf_time)
                eight_rf_list.append(eight_rf_time)
                eight_g_list.append(eight_graph_time)
            
            placeholder.extend([str(sum(eight_int_list)), str(sum(eight_pf_list)), str(sum(eight_rf_list)), str(sum(eight_g_list)),
                str(fmean(eight_int_list)), str(fmean(eight_pf_list)), str(fmean(eight_rf_list)), str(fmean(eight_g_list)),
                str(variance(eight_int_list)), str(variance(eight_pf_list)), str(variance(eight_rf_list)), str(variance(eight_g_list)),
                str(stdev(eight_int_list)), str(stdev(eight_pf_list)), str(stdev(eight_rf_list)), str(stdev(eight_g_list))])



            for row in range(0,2):
                outerrow = outer + row
                nine_int_time = merge_df.iloc[outerrow+8]["press_time"] - merge_df.iloc[outerrow]["release_time"]
                nine_pf_time = merge_df.iloc[outerrow+8]["press_time"] - merge_df.iloc[outerrow]["press_time"]
                nine_rf_time = merge_df.iloc[outerrow+8]["release_time"] - merge_df.iloc[outerrow]["release_time"]
                nine_graph_time = merge_df.iloc[outerrow+8]["release_time"] - merge_df.iloc[outerrow]["press_time"]
                placeholder.extend([str(nine_int_time), str(nine_pf_time), str(nine_rf_time), str(nine_graph_time)])
                nine_int_list.append(nine_int_time)
                nine_pf_list.append(nine_pf_time)
                nine_rf_list.append(nine_rf_time)
                nine_g_list.append(nine_graph_time)
            
            placeholder.extend([str(sum(nine_int_list)), str(sum(nine_pf_list)), str(sum(nine_rf_list)), str(sum(nine_g_list)),
                str(fmean(nine_int_list)), str(fmean(nine_pf_list)), str(fmean(nine_rf_list)), str(fmean(nine_g_list)),
                str(variance(nine_int_list)), str(variance(nine_pf_list)), str(variance(nine_rf_list)), str(variance(nine_g_list)),
                str(stdev(nine_int_list)), str(stdev(nine_pf_list)), str(stdev(nine_rf_list)), str(stdev(nine_g_list))])


            for row in range(0,1):
                outerrow = outer + row
                ten_int_time = merge_df.iloc[outerrow+9]["press_time"] - merge_df.iloc[outerrow]["release_time"]
                ten_pf_time = merge_df.iloc[outerrow+9]["press_time"] - merge_df.iloc[outerrow]["press_time"]
                ten_rf_time = merge_df.iloc[outerrow+9]["release_time"] - merge_df.iloc[outerrow]["release_time"]
                ten_graph_time = merge_df.iloc[outerrow+9]["release_time"] - merge_df.iloc[outerrow]["press_time"]
                placeholder.extend([str(ten_int_time), str(ten_pf_time), str(ten_rf_time), str(ten_graph_time)])
                
            #     ten_int_list.append(ten_int_time)
            #     ten_pf_list.append(ten_pf_time)
            #     ten_rf_list.append(ten_rf_time)
            #     ten_g_list.append(ten_graph_time)
            
            # placeholder.extend([str(fmean(ten_int_list)), str(fmean(ten_pf_list)), str(fmean(ten_rf_list)), str(fmean(ten_g_list)),
            #     str(variance(ten_int_list)), str(variance(ten_pf_list)), str(variance(ten_rf_list)), str(variance(ten_g_list)),
            #     str(stdev(ten_int_list)), str(stdev(ten_pf_list)), str(stdev(ten_rf_list)), str(stdev(ten_g_list))])

            # ten_int_list.clear()
            # ten_pf_list.clear()
            # ten_rf_list.clear()
            # ten_g_list.clear()
            
            writer = csv.writer(file)
            writer.writerow([name, *placeholder])
            placeholder.clear()

            two_dwell_list.clear()
            two_int_list.clear()
            two_pf_list.clear()
            two_rf_list.clear()
            two_g_list.clear()

            three_int_list.clear()
            three_pf_list.clear()
            three_rf_list.clear()
            three_g_list.clear()

            four_int_list.clear()
            four_pf_list.clear()
            four_rf_list.clear()
            four_g_list.clear()

            five_int_list.clear()
            five_pf_list.clear()
            five_rf_list.clear()
            five_g_list.clear()
            
            six_int_list.clear()
            six_pf_list.clear()
            six_rf_list.clear()
            six_g_list.clear()

            seven_int_list.clear()
            seven_pf_list.clear()
            seven_rf_list.clear()
            seven_g_list.clear()

            eight_int_list.clear()
            eight_pf_list.clear()
            eight_rf_list.clear()
            eight_g_list.clear()

            nine_int_list.clear()
            nine_pf_list.clear()
            nine_rf_list.clear()
            nine_g_list.clear()
        