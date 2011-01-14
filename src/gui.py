"""
This is the GUI, and is called by PolyBuild.

@Author: Charles Broughton
@Copyright: /LICENSE
@Name: gui.py
@Path: /src
"""

# Import Packages / Site-Packages
from Tkinter import *

def GUI_Main():
    def __init__(self):
        print ("- Loading PolyBuild Window...")
        
        top.title("PolyBuild")
        self.LogToggle = Button(top)
        self.LogToggle.configure(text="Hide Log Window",command=self.hideLog)
        self.LogToggle.pack({"side": "left"})
        self.QUITNOW = Button(top)
        self.QUITNOW.configure(text="EXIT NOW",bg="red",command=self.RAGEQUIT)          
        self.QUITNOW.pack({"side": "right"})
        self.pack()

        print ("- Loading Ores Listing Window...")
        GUI_Ores.title("PolyBuild -- Ores Listing")
        GUI_Ores.pack()
    #End of __init__

    def hideLog(self):
        # Hides / Shows the logging window.
        pass # NOT YET IMPLEMENTED
    #End of hideLog

    def RAGEQUIT(self):
        # Quickly exits everything, PANIC
        try:
            # Attempt a clean shutdown...
            ProcessLogic.terminate()
        except NameError:
            pass
        
        print ("\n\n\n\n---------------------------------------------")
        print (" This application was RAGEQUIT by the user ! ")
        print ("---------------------------------------------")

        top.destroy()
    #End of RAGEQUIT
#End of GUI_Main
