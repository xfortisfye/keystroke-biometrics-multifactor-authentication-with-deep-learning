"""
combi
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
    try:
        print(f"Display found as {os.environ['DISPLAY']}")
    except:
        os.environ['DISPLAY'] = ':0'
        print("Display NOT FOUND and has been set to zero")
    finally:
        print("...Program started.")

    # start from here
    startFlag = True

    while startFlag is True:
        print("What kind of dataset will you like to generate? \n"
        + "1) Random 10-Letters Dataset for CAPTCHA\n"
        + "2) Identical 10-Letters Dataset for CAPTCHA\n"
        + "3) Controlled dataset for Password\n"
        + "4) Controlled dataset for Password")
        case = input()
        
        if case is 1:
            completed = False
            name = input("What is your name? ")
            round = 1
            count = 1
            captcha = []    

            csv_path, export_dir_path, three, four, five, six = prelude(name)
            
            for _ in range(round):
                captcha.append(random.choice(three) + " " + random.choice(six))
                captcha.append(random.choice(four) + " " + random.choice(five))
                captcha.append(random.choice(five) + " " + random.choice(four))
                captcha.append(random.choice(six) + " " + random.choice(three))
            
            random.shuffle(captcha)
            maxCount = len(captcha)

            keyboard = Keyboard()
            keyboard.set_name(name)
            keyboard.set_csv(csv_path)
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
            print("hello1")
            
        elif case is 2:
            print("hello2")
            completed = False
            name = input("What is your name? ")
            round = 2
            count = 1
            captcha = []    

            csv_path_322, csv_path_5, export_dir_path, three_f, four_f, five_f, six_f, three_r, four_r, five_r, six_r = prelude(name)
            
            for _ in range(0, len(three_f), 2):
                captcha.append(three_f[_] + " " + three_f[_+1])
                captcha.append(four_f[_] + " " + four_f[_+1])
                captcha.append(five_f[_] + " " + five_f[_+1])
                captcha.append(six_f[_] + " " + six_f[_+1])

            for _ in range(round):
                captcha.append(random.choice(three_r) + " " + random.choice(six_r))
                captcha.append(random.choice(four_r) + " " + random.choice(five_r))
                captcha.append(random.choice(five_r) + " " + random.choice(four_r))
                captcha.append(random.choice(six_r) + " " + random.choice(three_r))
            
            # random.shuffle(captcha)
            maxCount = len(captcha)

            keyboard = Keyboard()
            keyboard.set_name(name)
            keyboard.set_csv(csv_path_322)
            keyboard.set_csv_5(csv_path_5)
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
            
            # csv_name = name + ".csv"
            # csv_path = os.path.join(export_dir_path, csv_name)

            csv_name_322 = name + "_322.csv"
            csv_path_322 = os.path.join(export_dir_path, csv_name_322)

            csv_name_5 = name + "_5.csv"
            csv_path_5 = os.path.join(export_dir_path, csv_name_5)

            if os.path.isfile(csv_path_322) is True:
                print(f"CSV file exist at {csv_path_322}")
            else:
                # assign header columns
                headerList = ['Subject', 'Seq_No', 'Sequence']
                headerList.append(f"D|0")
                for _ in range(10-1):
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
                
                # open CSV file and assign header
                with open(csv_path_322, 'w', newline='') as file:
                    dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
                    dw.writeheader()

                print(f"CSV file will be created: {csv_path_322}")

                if os.path.isfile(csv_path_5) is True:
                    print(f"CSV file exist at {csv_path_5}")
                else:
                    # assign header columns
                    headerList = ['Subject', 'Char_Total_Str', 'Char_Total_Int', 'Char_Init', 'Char_End', 'Seq_No', 'Current_Dwell', 'Interval', 'Press_Flight', 'Release_Flight', 'Digraph', 'Later_Dwell']
                    
                    # open CSV file and assign header
                    with open(csv_path_5, 'w', newline='') as file:
                        dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
                        dw.writeheader()

                    print(f"CSV file will be created: {csv_path_5}")



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

            with open("captcha/three_fixed.txt", "r") as file:
                three_f = list(map(str, file.read().split()))

            with open("captcha/four_fixed.txt", "r") as file:
                four_f = list(map(str, file.read().split()))

            with open("captcha/five_fixed.txt", "r") as file:
                five_f = list(map(str, file.read().split()))

            with open("captcha/six_fixed.txt", "r") as file:
                six_f = list(map(str, file.read().split()))

            with open("captcha/three_rand.txt", "r") as file:
                three_r = list(map(str, file.read().split()))

            with open("captcha/four_rand.txt", "r") as file:
                four_r = list(map(str, file.read().split()))

            with open("captcha/five_rand.txt", "r") as file:
                five_r = list(map(str, file.read().split()))

            with open("captcha/six_rand.txt", "r") as file:
                six_r = list(map(str, file.read().split()))

            time.sleep(0.1)
            return csv_path_322, csv_path_5, export_dir_path, three_f, four_f, five_f, six_f, three_r, four_r, five_r, six_r

        elif case is 3:
            # do stuf
            print("hello3")
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

        elif case is 4:
            # do stuf
            print("hello4")
            completed = False
            name = input("What is your name? ")
            # passwordFlag = False
            # while passwordFlag is False:
            #     password = input("What is your desired password? 8 alphanumeric numbers only and avoid common password: ")
            #     if len(password) == 8:
            #         passwordFlag = True

            # # password = "dEcisi0n"

            # maxCount = 105
            maxCount = 60
            count = 1

            merge_csv_path, csv_path_full, csv_path_semi, csv_path_bare, csv_path_single, export_dir_path = prelude(name, 8)

            keyboard = Keyboard()
            keyboard.set_name(name)
            keyboard.set_merge_csv(merge_csv_path)
            keyboard.set_csv(csv_path_full)
            keyboard.set_csv_semi(csv_path_semi)
            keyboard.set_csv_bare(csv_path_bare)
            keyboard.set_csv_single(csv_path_single)
            keyboard.set_export(export_dir_path)
            listener = Listener(on_press=keyboard.key_press, on_release=keyboard.key_release)
            listener.start()

            invalidCount = 0
            incorrectCount = 0

            # andy, azfar, bryce, chris, cy, gerald, ken, qk, sz, vale, ye, ys
            password_list = ["C05mical", "play4pay", "4cHkh1dL", "a1rcr2ft", "wang1234", "Andy1234", "Kennth12", "Andyb1tc", "andy1234", "memories", "HiAndy12", "tw1nkle6"]

            for password in password_list:
                for x in range(0, 1):
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
            
            error_name = "combi_" + name + "_error.txt"
            # error_name = "same_" + name + "_error.txt"
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

                
            
        def prelude(name, maxPwdLen):
            # maxPwdLen = len(password)
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
            # merge_csv_name = "own_" + name + "_merge_df.csv"
            # merge_csv_path = os.path.join(export_dir_path, merge_csv_name)

            # csv_name_full = "own_" + name + "_full.csv"
            # csv_path_full = os.path.join(export_dir_path, csv_name_full)

            # csv_name_semi = "own_" + name + "_semi.csv"
            # csv_path_semi = os.path.join(export_dir_path, csv_name_semi)

            # csv_name_bare = "own_" + name + "_bare.csv"
            # csv_path_bare = os.path.join(export_dir_path, csv_name_bare)

            # csv_name_5 = "own_" + name + "_5.csv"
            # csv_path_single = os.path.join(export_dir_path, csv_name_5)

            # merge_csv_name = "same_" + name + "_merge_df.csv"
            # merge_csv_path = os.path.join(export_dir_path, merge_csv_name)

            # csv_name_full = "same_" + name + "_full.csv"
            # csv_path_full = os.path.join(export_dir_path, csv_name_full)

            # csv_name_semi = "same_" + name + "_semi.csv"
            # csv_path_semi = os.path.join(export_dir_path, csv_name_semi)

            # csv_name_bare = "same_" + name + "_bare.csv"
            # csv_path_bare = os.path.join(export_dir_path, csv_name_bare)

            # csv_name_5 = "same_" + name + "_5.csv"
            # csv_path_single = os.path.join(export_dir_path, csv_name_5)

            merge_csv_name = "combi_" + name + "_merge_df.csv"
            merge_csv_path = os.path.join(export_dir_path, merge_csv_name)

            csv_name_full = "combi_" + name + "_full.csv"
            csv_path_full = os.path.join(export_dir_path, csv_name_full)

            csv_name_semi = "combi_" + name + "_semi.csv"
            csv_path_semi = os.path.join(export_dir_path, csv_name_semi)

            csv_name_bare = "combi_" + name + "_bare.csv"
            csv_path_bare = os.path.join(export_dir_path, csv_name_bare)

            csv_name_5 = "combi_" + name + "_5.csv"
            csv_path_single = os.path.join(export_dir_path, csv_name_5)

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

            if os.path.isfile(csv_path_semi) is True:
                print(f"CSV file exist at {csv_path_semi}")
            else:
                # assign header columns
                headerList = ['Subject', 'Password']
                headerList.append(f"D|0")
                for _ in range(maxPwdLen-1):
                    headerList.append(f"I|{_}+{_+1}")
                    headerList.append(f"PF|{_}+{_+1}")
                    headerList.append(f"RF|{_}+{_+1}")
                    headerList.append(f"DT|{_}+{_+1}")
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
                with open(csv_path_semi, 'w', newline='') as file:
                    dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
                    dw.writeheader()

                print(f"CSV file will be created: {csv_path_semi}")

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
                    headerList.append(f"DT|{_}+{_+1}")
                    headerList.append(f"D|{_+1}")
                
                # open CSV file and assign header
                with open(csv_path_bare, 'w', newline='') as file:
                    dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
                    dw.writeheader()

                print(f"Bare CSV file will be created: {csv_path_bare}")

                ###########################################

                if os.path.isfile(csv_path_single) is True:
                    print(f"CSV file exist at {csv_path_single}")
                else:
                    # assign header columns
                    headerList = ['Subject', 'Char_Total_Str', 'Char_Total_Int', 'Char_Init', 'Char_End', 'Current_Dwell', 'Interval', 'Press_Flight', 'Release_Flight', 'Digraph', 'Later_Dwell']
                    
                    # open CSV file and assign header
                    with open(csv_path_single, 'w', newline='') as file:
                        dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
                        dw.writeheader()

                    print(f"CSV file will be created: {csv_path_single}")


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

            time.sleep(0.1)
            return merge_csv_path, csv_path_full, csv_path_semi, csv_path_bare, csv_path_single, export_dir_path

        else:
            print("Please select an appropriate case number.")     


def prelude(name):
    ## missing info
    ## 2
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
    merge_csv_name = name + "_merge_df.csv"
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

## 3erd

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

### 4th
def prelude(name, maxPwdLen):
            # maxPwdLen = len(password)
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
            # merge_csv_name = "own_" + name + "_merge_df.csv"
            # merge_csv_path = os.path.join(export_dir_path, merge_csv_name)

            # csv_name_full = "own_" + name + "_full.csv"
            # csv_path_full = os.path.join(export_dir_path, csv_name_full)

            # csv_name_semi = "own_" + name + "_semi.csv"
            # csv_path_semi = os.path.join(export_dir_path, csv_name_semi)

            # csv_name_bare = "own_" + name + "_bare.csv"
            # csv_path_bare = os.path.join(export_dir_path, csv_name_bare)

            # csv_name_5 = "own_" + name + "_5.csv"
            # csv_path_single = os.path.join(export_dir_path, csv_name_5)

            # merge_csv_name = "same_" + name + "_merge_df.csv"
            # merge_csv_path = os.path.join(export_dir_path, merge_csv_name)

            # csv_name_full = "same_" + name + "_full.csv"
            # csv_path_full = os.path.join(export_dir_path, csv_name_full)

            # csv_name_semi = "same_" + name + "_semi.csv"
            # csv_path_semi = os.path.join(export_dir_path, csv_name_semi)

            # csv_name_bare = "same_" + name + "_bare.csv"
            # csv_path_bare = os.path.join(export_dir_path, csv_name_bare)

            # csv_name_5 = "same_" + name + "_5.csv"
            # csv_path_single = os.path.join(export_dir_path, csv_name_5)

            merge_csv_name = "combi_" + name + "_merge_df.csv"
            merge_csv_path = os.path.join(export_dir_path, merge_csv_name)

            csv_name_full = "combi_" + name + "_full.csv"
            csv_path_full = os.path.join(export_dir_path, csv_name_full)

            csv_name_semi = "combi_" + name + "_semi.csv"
            csv_path_semi = os.path.join(export_dir_path, csv_name_semi)

            csv_name_bare = "combi_" + name + "_bare.csv"
            csv_path_bare = os.path.join(export_dir_path, csv_name_bare)

            csv_name_5 = "combi_" + name + "_5.csv"
            csv_path_single = os.path.join(export_dir_path, csv_name_5)

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


if __name__ == "__main__":
    main()

    # generate ui file
    # pyuic5 mainwindow.ui -o mainwindowui.py
    # generate resource file
    # pyrcc5 resources.qrc -o resources.py
    # create app
    # pyinstaller -F -w main.py
    # pyinstaller --onefile main.py
    # pyinstaller main.py --onefile --hidden-import=pynput.keyboard._xorg -n combi
