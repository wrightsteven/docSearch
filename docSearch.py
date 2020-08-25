import sys, os

os.chdir("directory")

with open("yourtextfile", "r") as file:
    txt = file.read()
    
def getNthLetters(n, text, target):
    res = ""
    for index, letter in enumerate(text):
        if index % n == 0:
            res = res + letter
    
    if target in res:
        sys.stdout = open(target+str(n)+".txt", "w")
        print(res)
        sys.stdout.close()
    else:
        print("Target not found")

getNthLetters(5, txt, "at")
