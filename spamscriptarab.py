import pyautogui
import pyperclip
import keyboard
import random
import colorama

print("""
    _                  _    _         _
    | | ____ _ ______ _| | _| |__  ___| |_ __ _ _ __
    | |/ / _` |_  / _` | |/ / '_ \/ __| __/ _` | '_ \\
    |   < (_| |/ / (_| |   <| | | \__ \ || (_| | | | |
    |_|\_\__,_/___\__,_|_|\_\_| |_|___/\__\__,_|_| |_|
""", colorama.Fore.RED,
"""
    _                     _
    | |__   ___  _ __ ___ | |__
    | '_ \ / _ \| '_ ` _ \| '_ \\
    | |_) | (_) | | | | | | |_) |
    |_.__/ \___/|_| |_| |_|_.__/
""")
stringArab = """
ضصثقفغعهخحجدذشسيبلاتنمكط\ئءؤرىةوزظ
手田口廿卜山戈人心［］'；中大十竹土火木尸日Ｚ、難金女月弓一，。/
АБВГДЕЁЖЗИЙКЛМНОонмлкйизжёедгвбаПРСТУФХЦЧШЩЪЫЬЭЮЯпрстуфхцчшщъыьэюяІѢѴѲіѣѳѵ
कखगघङचछजझञटठडढणतथदधनपफबभमक़ख़ज़ग़ड़ढ़फ़यरलळवहशषसऱऴअआइईउऊऋॠऌॡएऐओऔ।॥ऽ॰॰ॐ०१२३४५६७८९
ABCDEFabcdefæßðđŋħĸøł~@ł€¶ŧ←↓→øþ
ħ→ħ→ħ«|@æłß€ð¶đŧŋ←ħ↓ĸøłþ~«»¢“”nµ·@#¬{[]}\|«»ßðđŋħł{}}[\]
123456
💥💥💥💥💥💥
"""
warn = "Казахстан 🇰🇿 угрожает ⚠️ нам бомбардировкой 💣"
all_str = ''
count = 0
print(colorama.Fore.LIGHTRED_EX,"""
      ~~~~~~~~~~~~~~~~~~~~
      Bomb tool by MrLorem 
      ~~~~~~~~~~~~~~~~~~~~
      
      Cancel anytime by pressing ctrl + C
      Note: If you want to cancel while spamming,
      just press the number 1 and it will stop.
      """, colorama.Style.RESET_ALL)
print(colorama.Fore.LIGHTGREEN_EX,
      "[*]", colorama.Style.RESET_ALL,
      "Input the number of messages you wanna bomb with")
try:
    election = int(input("->    "))
except ValueError:
    state = False
    print("Wroooong, type a number")
    while state == False:
        try:
            election = int(input("->    "))
            state = True
            break
        except ValueError:
            continue
        
        
print(colorama.Fore.LIGHTGREEN_EX,
      "[*]", colorama.Style.RESET_ALL,
      "Input the cooldown you want to have")
try:
    election_cld = float(input("->    "))
except ValueError:
    state = False
    print("Wroooong, type a number")
    while state == False:
        try:
            election_cld = float(input("->    "))
            state = True
            break
        except ValueError:
            continue
        
        

print(colorama.Fore.LIGHTGREEN_EX,
      "[*]", colorama.Style.RESET_ALL,
      "Input how faster you want the spam to be \n",
      "Example: 0, 0.5, 1, 1.5")
try:
    election_cld_msg = float(input("->    "))
except ValueError:
    state = False
    print("Wroooong, type a number")
    while state == False:
        try:
            election_cld_msg = float(input("->    "))
            state = True
            break
        except ValueError:
            continue
        
        
pyautogui.PAUSE = election_cld_msg

print(colorama.Fore.LIGHTRED_EX, "[*] ",
      "You're about to run this program,\n this program will take FULL control of your keyboard, you'll have\n",
      f"{election_cld} seconds to go to the application you want to bomb, are you SURE you want to continue?",
      "\n (N,y)")

submit = input("->    ")
if submit.lower() == "n":
    exit()
elif submit.lower() == "y":
    print("Ok, if you want to cancel the program, you can do it pressing ctrl + c",
          "When it is spamming, you'll have to press the key '1'.")
while submit.lower() != "y" and submit.lower() != "n":
    submit = input("->    ")
    
for i in range(int(election_cld)):
    
    print(colorama.Fore.LIGHTGREEN_EX, "[*]", colorama.Style.RESET_ALL, f"Starting in... {election_cld} seconds..")
    election_cld -= 1
    pyautogui.sleep(1)
print(colorama.Fore.RED, "~~~Starting...~~~", colorama.Style.RESET_ALL)




for i in range(election):
    if keyboard.is_pressed('1'):
        print(colorama.Fore.LIGHTGREEN_EX, "[*]", colorama.Style.RESET_ALL, "Successfully cancelled program [Closing...]")
        exit()
        
    ransel="".join(random.sample(stringArab, len(stringArab)))
    all_str += ransel
    all_str += warn
    pyperclip.copy(all_str)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.sleep(0.014)
    pyautogui.press('enter')
    all_str = ""
    count += 1
    print(colorama.Fore.LIGHTGREEN_EX, "[*]", colorama.Style.RESET_ALL, f"Successfully sended message [{count}]")



print(colorama.Fore.RED, "Closing program...")
