import pyautogui
import pyperclip
import keyboard
import random
import colorama
# from gencode import Gencode

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
election = int(input("->    "))
pyautogui.PAUSE = 0.028
cnt = 5
for i in range(5):
    
    print(colorama.Fore.LIGHTGREEN_EX, "[*]", colorama.Style.RESET_ALL, f"Starting in... {cnt} seconds..")
    cnt -= 1
    pyautogui.sleep(1)
print(colorama.Fore.RED, "~~~Starting...~~~", colorama.Style.RESET_ALL)
try:
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
except ValueError:
    print("Invalid value")
finally:
    print(colorama.Fore.RED, "Closing program...")