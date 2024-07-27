# This is better than your absolute shit microsoft suck on it
from tkinter import *
from datetime import datetime
from PIL import ImageGrab as ig, Image
import time, os, getpass


slep = time.sleep
dtn = datetime.now()
user = getpass.getuser()  
p = f"C:\\Users\\{user}\\Desktop\\Computer Snap Screenshots"

#functions
def initialize():


    if os.path.exists(p):
        print("dir exists")
    else:
        print("no dir, creating dir")
        os.makedirs(p)
        print(f"Path made at {p}")

def main():
   

    selfPath = os.getcwd()
    os.startfile(f"{selfPath}\\other\\StartUp.vbs")
    initialize()
    
    slep(5)
    while (True):
        ltime = time.localtime()
        current_time = time.strftime("%Y-%m-%d %H-%M-%S", ltime)

        # Make Screenshot
        sc = ig.grab()
        save = sc.save(f"Computer-Snap-{current_time}.png")
        sc.close()

        screenshotPath = f"{selfPath}\\Computer-Snap-{current_time}.png"
        if not os.path.exists(screenshotPath):
            os.startfile(f"{selfPath}\\other\\error.vbs")
            exit()

        print("Screenshot was found, re-directing to desktop folder...")

        if not os.path.exists(p):
            initialize()

        new_sc_path = f"{p}\\Computer-Snap-{current_time}.png"
        os.replace(screenshotPath, new_sc_path)
        if os.path.exists(screenshotPath):
            os.remove(screenshotPath)


        slep(600)
    

main()
