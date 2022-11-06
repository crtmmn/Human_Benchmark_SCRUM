import random
import Game
import os
import time
from colours import bcolors

class NumberMemory(Game.Game):
    def __init__(self):
        super().__init__()
        self._random_number = 0
        self._round = 0
    def Play(self):
        self._score = 0
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

            input(bcolors.OKCYAN + "【﻿PRESS   ENTER   TO   START: 】" + bcolors.ENDC)

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
                print(bcolors.FAIL + "【﻿Restart the program and enter a integer number】" + bcolors.ENDC)
                quit()
            if str(user_input1) == str(self._random_number):
                print("")
                print(bcolors.OKGREEN + "【﻿CORRECT】" + bcolors.ENDC)

                self._score += 1
                print("")
                print(bcolors.OKGREEN + "【﻿NUMBER   OF   POINTS: "  + "|" + str(self._score) + "|" + "】" + bcolors.ENDC)

                print("")
            else:
                print("")
                print(bcolors.FAIL + "【﻿INCORRECT】" + bcolors.ENDC)

                print(bcolors.WARNING + "【﻿THE   NUMBER   WAS: " + "|" + str(self._random_number) + "|"  + "】" + bcolors.ENDC)
                print(bcolors.WARNING + "【﻿YOU HAVE: " + "|" + str(self._score) + "|" + " POINTS " + "】" +  bcolors.ENDC)

                
                print("")
                break
        