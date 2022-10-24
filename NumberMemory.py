import random
import Game
import os
import time
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
class NumberMemory(Game.Game):
    def __init__(self):
        super().__init__()
        self._random_number = 0
        self._round = 0
    def Play(self):
        clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        clearConsole()

        print(bcolors.WARNING + "【﻿ＮＵＭＢＥＲ　ＭＥＭＯＲＹ　ＧＡＭＥ】" + bcolors.ENDC)
#biore sterydy
        if self._round <= 1:
            a = 1
            b = 9
        else:
            a = 1
            b = 10
        while True:
            self._round += 1
            self._random_number = random.randint(a, b)
            print("")

            input(bcolors.OKCYAN + " PRESS   ENTER   TO   START: " + bcolors.ENDC)

            print("")
            print(bcolors.OKCYAN + "【﻿REMEMBER   THAT   NUMBER : " + "|" + str(self._random_number) + "| " + "】" + bcolors.ENDC)
            print("")
            a = a * 10
            b = b * 10
            print(bcolors.WARNING + "|5|" + bcolors.ENDC)
            time.sleep(1)
            print(bcolors.WARNING + "|4|" + bcolors.ENDC)
            time.sleep(1)
            print(bcolors.WARNING + "|3|" + bcolors.ENDC)
            time.sleep(1)
            print(bcolors.WARNING + "|2|" + bcolors.ENDC)
            time.sleep(1)
            print(bcolors.WARNING + "|1|" + bcolors.ENDC)
            clearConsole()
            print("")
            user_input1 = input(bcolors.BOLD + "INPUT   NUMBER: " + bcolors.ENDC)
            try:
                int(user_input1)
                it_is = True
            except ValueError:
                it_is = False
            if it_is == False:
                print(bcolors.FAIL + "Restart the program and enter a integer number" + bcolors.ENDC)
                quit()
            if str(user_input1) == str(self._random_number):
                print("")
                print(bcolors.OKGREEN + "【﻿CORRECT】" + bcolors.ENDC)

                self._score += 1
                print("")
                print(bcolors.OKGREEN + "【﻿NUMBER   O F   POINTS: "  + "|" + str(self._score) + "|" + "】" + bcolors.ENDC)

                print("")
            else:
                print("")
                print(bcolors.FAIL + "【﻿INCORRECT】" + bcolors.ENDC)

                print(bcolors.WARNING + "【﻿THE   NUMBR   WAS: " + "|" + str(self._random_number) + "|"  + "】" + bcolors.ENDC)
                print(bcolors.WARNING + "【﻿YOU HAVE: " + "|" + str(self._score) + "|" + " POINTS " + "】" +  bcolors.ENDC)

                
                print("")
                break
        