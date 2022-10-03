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
    round = 10
    count = 1
    captcha = []    

    csv_path_full, csv_path_onekey, export_dir_path, main_rand_five, fixed_five, random_five = prelude(name)
    
    for _ in range(0, 110):
        captcha.append(random.choice(main_rand_five))

    # for _ in range(0, len(fixed_five)):
    #     captcha.append(fixed_five[_])

    # for _ in range(round):
    #     captcha.append(random.choice(random_five))

    # random.shuffle(captcha)
    maxCount = len(captcha)

    keyboard = Keyboard()
    keyboard.set_name(name)
    keyboard.set_csv(csv_path_full)
    keyboard.set_csv_5(csv_path_onekey)
    keyboard.set_export(export_dir_path)
    listener = Listener(on_press=keyboard.key_press, on_release=keyboard.key_release)
    listener.start()

    for _ in captcha:
        completed = False
        while completed is False:
            basePwdInput = input(f"Please type \"{_}\": ")
            sleep(1)
            if basePwdInput == _:
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
                
                if len(press_df.index.values) == len(_) and len(release_df.index.values) == len(_):
                    print(f"Thank you. {maxCount - count} times left. ")
                    keyboard.export_to_csv(_)
                    count = count + 1
                    keyboard.reset()
                    completed = True
                else:
                    keyboard.reset()
                    print(f"Invalid. Please key in {_} without any backspace or errors. ")
            else:
                keyboard.reset()
                print("Password is incorrect. Please retry. ")
    
def prelude(name):
    
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
    merge_csv_name = "rand_" + name + "_merge_df.csv"
    merge_csv_path = os.path.join(export_dir_path, merge_csv_name)

    if os.path.isfile(merge_csv_path) is True:
        print(f"CSV file exist at {merge_csv_path}")
    else:
        # assign header columns
        headerList = ['', 'key', 'press_time', 'release_time']
        
        # open CSV file and assign header
        with open(merge_csv_path, 'w', newline='') as file:
            dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
            dw.writeheader()

        print(f"Merge_DF CSV file will be created: {merge_csv_path}")

    # csv_name = name + ".csv"
    # csv_path = os.path.join(export_dir_path, csv_name)

    csv_name_full = "full_rand_" + name + ".csv"
    csv_path_full = os.path.join(export_dir_path, csv_name_full)

    csv_name_onekey = "onekey_rand_" + name + ".csv"
    csv_path_onekey = os.path.join(export_dir_path, csv_name_onekey)

    if os.path.isfile(csv_path_full) is True:
        print(f"CSV file exist at {csv_path_full}")
    else:
        # assign header columns
        headerList = ['Subject', 'Sequence']
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
        
        # open CSV file and assign header
        with open(csv_path_full, 'w', newline='') as file:
            dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
            dw.writeheader()

        print(f"CSV file will be created: {csv_path_full}")

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
    info_name = name + "_info.txt"
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

    with open("captcha/five.txt", "r") as file:
        main_rand_five = list(map(str, file.read().split()))

    with open("captcha/five_let_fixed.txt", "r") as file:
        fixed_five = list(map(str, file.read().split()))

    with open("captcha/five_let_rand.txt", "r") as file:
        random_five = list(map(str, file.read().split()))


    time.sleep(0.1)
    return csv_path_full, csv_path_onekey, export_dir_path, main_rand_five, fixed_five, random_five

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
