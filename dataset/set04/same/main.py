"""
same
"""
import os
import platform
import time
from sys import exit

# keyboard
from pynput.keyboard import Key, Listener
from keyboard import Keyboard
import csv
from time import sleep
import random

def main():
    completed = False
    name = input("What is your name? ")
    # passwordFlag = False
    # while passwordFlag is False:
    #     password = input("What is your desired password? 8 alphanumeric numbers only and avoid common password: ")
    #     if len(password) == 8:
    #         passwordFlag = True

    password = "dEcisi0n"

    maxCount = 105
    count = 1

    csv_path_df, csv_path_full, csv_path_nonstat, csv_path_bare, csv_path_onekey, export_dir_path = prelude(name, password)

    keyboard = Keyboard()
    keyboard.set_name(name)
    keyboard.set_csv_df(csv_path_df)
    keyboard.set_csv(csv_path_full)
    keyboard.set_csv_nonstat(csv_path_nonstat)
    keyboard.set_csv_bare(csv_path_bare)
    keyboard.set_csv_onekey(csv_path_onekey)
    keyboard.set_export(export_dir_path)
    listener = Listener(on_press=keyboard.key_press, on_release=keyboard.key_release)
    listener.start()

    invalidCount = 0
    incorrectCount = 0

    for _ in range(0, maxCount):
        completed = False
        while completed is False:
            basePwdInput = input(f"Please type \"{password}\": ")
            sleep(1)
            if basePwdInput == password:
                press_df = keyboard.get_press_df()
                release_df = keyboard.get_release_df()
                
                press_df.reset_index(inplace=True, drop=True)
                release_df.reset_index(inplace=True, drop=True)
                press_df.drop(press_df[press_df['key']=='key.enter'].index, inplace=True)
                press_df.drop(press_df[press_df['key']=='key.caps_lock'].index, inplace=True)
                press_df.drop(press_df[press_df['key']=='key.shift'].index, inplace=True)
                press_df.drop(press_df[press_df['key']=='key.shift_r'].index, inplace=True)
                release_df.drop(release_df[release_df['key']=='key.enter'].index, inplace=True)
                release_df.drop(release_df[release_df['key']=='key.caps_lock'].index, inplace=True)
                release_df.drop(release_df[release_df['key']=='key.shift'].index, inplace=True)
                release_df.drop(release_df[release_df['key']=='key.shift_r'].index, inplace=True)
                
                if len(press_df.index.values) == len(password) and len(release_df.index.values) == len(password):
                    print(f"Thank you. {maxCount - count} times left. ")
                    keyboard.export_to_csv(password)
                    count = count + 1
                    keyboard.reset()
                    completed = True
                else:
                    keyboard.reset()
                    print(f"Invalid. Please key in {password} without any backspace or errors. ")
                    invalidCount = invalidCount + 1
            else:
                keyboard.reset()
                print("Password is incorrect. Please retry. ")
                incorrectCount = incorrectCount + 1

    export_dir_name = "export"
    current_path = os.getcwd()
    export_dir_path = os.path.join(current_path, export_dir_name)
    
    # error_name = "own_same_" + name + ".txt"
    error_name = "error_same_" + name + ".txt"
    error_path = os.path.join(export_dir_path, error_name) 

    if os.path.isfile(error_path) is True:
        print(f"Error file exist at {error_path}")
    else:
        # open CSV file and assign header
        with open(error_path, 'w', newline='') as file:
            file.write(f"Incorrect Count: {invalidCount}\n")
            file.write(f"Invalid Count: {incorrectCount}\n")
            totalCount = invalidCount + incorrectCount
            file.write(f"Total Wrong Count: {totalCount}\n")
            accuracy = (105 / (totalCount + 105)) * 100
            file.write(f"Accuracy: {accuracy}\n")

        print(f"Error file will be created: {error_path}")

        
    
def prelude(name, password):
    maxPwdLen = len(password)
    export_dir_name = "export"
    '''
    obtain information about system
    '''
    current_path = os.getcwd()
    print(f"OS Name: {os.name}")
    print(f"Operating System: {platform.system()}")
    print(f"Release Version: {platform.release()}")
    print(f"Current Path: {os.getcwd()}")

    try:
        print(f"Display found as {os.environ['DISPLAY']}")
    except:
        os.environ['DISPLAY'] = ':0'
        print("Display NOT FOUND and has been set to zero")
    finally:
        print("...Program started.")

    '''
    export directory
    '''
    export_dir_path = os.path.join(current_path, export_dir_name)

    if os.path.isdir(export_dir_path) is True:
        print(f"Export directory exists at: {export_dir_path}")
        pass
    else:
        try:
            os.mkdir(export_dir_path, 666)
            print(f"Export directory have been created at: {export_dir_path}")
        except:
            print("Error: Export Directory not created")

    '''
    create merge_df csv file
    '''
    csv_df_name = "df_same_" + name + ".csv"
    csv_path_df = os.path.join(export_dir_path, csv_df_name)

    csv_name_full = "same_" + name + ".csv"
    csv_path_full = os.path.join(export_dir_path, csv_name_full)

    csv_name_semi = "nonstat_same_" + name + ".csv"
    csv_path_nonstat = os.path.join(export_dir_path, csv_name_semi)

    csv_name_bare = "bare_same_" + name + ".csv"
    csv_path_bare = os.path.join(export_dir_path, csv_name_bare)

    csv_name_5 = "onekey_same_" + name + ".csv"
    csv_path_onekey = os.path.join(export_dir_path, csv_name_5)

    if os.path.isfile(csv_path_df) is True:
        print(f"CSV file exist at {csv_path_df}")
    else:
        # assign header columns
        headerList = ['', 'key', 'press_time', 'release_time']
        
        # open CSV file and assign header
        with open(csv_path_df, 'w', newline='') as file:
            dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
            dw.writeheader()

        print(f"Merge_DF CSV file will be created: {csv_path_df}")

    if os.path.isfile(csv_path_full) is True:
        print(f"CSV file exist at {csv_path_full}")
    else:
        # assign header columns
        headerList = ['Subject', 'Password']
        headerList.append(f"D|0")
        for _ in range(maxPwdLen-1):
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

        for _ in range(maxPwdLen-2):
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

        for _ in range(maxPwdLen-3):
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

        for _ in range(maxPwdLen-4):
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

        for _ in range(maxPwdLen-5):
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

        for _ in range(maxPwdLen-6):
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

        for _ in range(maxPwdLen-7):
            headerList.append(f"T8_I|{_}+{_+7}")
            headerList.append(f"T8_PF|{_}+{_+7}")
            headerList.append(f"T8_RF|{_}+{_+7}")
            headerList.append(f"T8_G|{_}+{_+7}")
        
        # open CSV file and assign header
        with open(csv_path_full, 'w', newline='') as file:
            dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
            dw.writeheader()

        print(f"CSV file will be created: {csv_path_full}")

        ###########################################

    if os.path.isfile(csv_path_nonstat) is True:
        print(f"CSV file exist at {csv_path_nonstat}")
    else:
        # assign header columns
        headerList = ['Subject', 'Password']
        headerList.append(f"D|0")
        for _ in range(maxPwdLen-1):
            headerList.append(f"I|{_}+{_+1}")
            headerList.append(f"PF|{_}+{_+1}")
            headerList.append(f"RF|{_}+{_+1}")
            headerList.append(f"G|{_}+{_+1}")
            headerList.append(f"D|{_+1}")

        for _ in range(maxPwdLen-2):
            headerList.append(f"T3_I|{_}+{_+2}")
            headerList.append(f"T3_PF|{_}+{_+2}")
            headerList.append(f"T3_RF|{_}+{_+2}")
            headerList.append(f"T3_G|{_}+{_+2}")

        for _ in range(maxPwdLen-3):
            headerList.append(f"T4_I|{_}+{_+3}")
            headerList.append(f"T4_PF|{_}+{_+3}")
            headerList.append(f"T4_RF|{_}+{_+3}")
            headerList.append(f"T4_G|{_}+{_+3}")

        for _ in range(maxPwdLen-4):
            headerList.append(f"T5_I|{_}+{_+4}")
            headerList.append(f"T5_PF|{_}+{_+4}")
            headerList.append(f"T5_RF|{_}+{_+4}")
            headerList.append(f"T5_G|{_}+{_+4}")

        for _ in range(maxPwdLen-5):
            headerList.append(f"T6_I|{_}+{_+5}")
            headerList.append(f"T6_PF|{_}+{_+5}")
            headerList.append(f"T6_RF|{_}+{_+5}")
            headerList.append(f"T6_G|{_}+{_+5}")

        for _ in range(maxPwdLen-6):
            headerList.append(f"T7_I|{_}+{_+6}")
            headerList.append(f"T7_PF|{_}+{_+6}")
            headerList.append(f"T7_RF|{_}+{_+6}")
            headerList.append(f"T7_G|{_}+{_+6}")

        for _ in range(maxPwdLen-7):
            headerList.append(f"T8_I|{_}+{_+7}")
            headerList.append(f"T8_PF|{_}+{_+7}")
            headerList.append(f"T8_RF|{_}+{_+7}")
            headerList.append(f"T8_G|{_}+{_+7}")
        
        # open CSV file and assign header
        with open(csv_path_nonstat, 'w', newline='') as file:
            dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
            dw.writeheader()

        print(f"CSV file will be created: {csv_path_nonstat}")

        ###########################################

    if os.path.isfile(csv_path_bare) is True:
        print(f"CSV file exist at {csv_path_bare}")
    else:
        # assign header columns
        headerList = ['Subject', 'Password']
        headerList.append(f"D|0")
        for _ in range(maxPwdLen-1):
            headerList.append(f"I|{_}+{_+1}")
            headerList.append(f"PF|{_}+{_+1}")
            headerList.append(f"RF|{_}+{_+1}")
            headerList.append(f"G|{_}+{_+1}")
            headerList.append(f"D|{_+1}")
        
        # open CSV file and assign header
        with open(csv_path_bare, 'w', newline='') as file:
            dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
            dw.writeheader()

        print(f"Bare CSV file will be created: {csv_path_bare}")

        ###########################################

        if os.path.isfile(csv_path_onekey) is True:
            print(f"CSV file exist at {csv_path_onekey}")
        else:
            # assign header columns
            headerList = ['Subject', 'Char_Total_Str', 'Char_Total_Int', 'Char_Init', 'Char_End', 'Current_Dwell', 'Interval', 'Press_Flight', 'Release_Flight', 'Digraph', 'Later_Dwell']
            
            # open CSV file and assign header
            with open(csv_path_onekey, 'w', newline='') as file:
                dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
                dw.writeheader()

            print(f"CSV file will be created: {csv_path_onekey}")


    '''
    generate info file
    '''
    info_name = "info_" + name + ".txt"
    info_path = os.path.join(export_dir_path, info_name) 

    if os.path.isfile(info_path) is True:
        print(f"Info file exist at {info_path}")
    else:
        # open CSV file and assign header
        with open(info_path, 'w', newline='') as file:
            file.write(f"Name: {name}\n")
            file.write(f"OS: {os.name}\n")
            file.write(f"Platform system: {platform.system()}\n")
            file.write(f"Platform release: {platform.release()}\n")

        print(f"Info file will be created: {info_path}")

    time.sleep(0.1)
    return csv_path_df, csv_path_full, csv_path_nonstat, csv_path_bare, csv_path_onekey, export_dir_path

if __name__ == "__main__":
    main()

    # generate ui file
    # pyuic5 mainwindow.ui -o mainwindowui.py
    # generate resource file
    # pyrcc5 resources.qrc -o resources.py
    # create app
    # pyinstaller -F -w main.py
    # pyinstaller --onefile main.py
    # pyinstaller main.py --onefile --hidden-import=pynput.keyboard._xorg