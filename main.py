import os
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
    
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clearConsole()

print(bcolors.WARNING + "【﻿ＨＵＭＡＮ　ＢＥＮＣＨＭＡＲＫ】" + bcolors.ENDC)
print(" ")
choice = input(bcolors.OKCYAN +  "【﻿CHOOSE   THE   GAME : 】" + "\n"  + "【﻿1 - Reaction Time】" + "\n" + "【﻿2 - Verbal memory】" + "\n" +"【﻿3 - Number Memory】" + "\n" + " YOUR  CHOICE: " +  bcolors.ENDC)
if choice == "1":
    import ReactionTime
elif choice == "2":
    import VerbalMemory
elif choice == "3":
    import NumberMemory
else:
    print(bcolors.FAIL + "【﻿ENTER  THE  CORRECT  OPTION!】" + bcolors.ENDC)
    quit()
