"""
This is the core, and should be called to start PolyBuild.

@Author: Charles Broughton
@Copyright: /LICENSE
@Name: PolyBuild.py
@Path: /src
"""

# Import Packates / Site-Packages
from multiprocessing import Process
from multiprocessing import Queue
from Tkinter import *
import ConfigParser

try:
    import mechanize
except:
    print ("CRITICAL: You appear to be missing one or more of" +
           " PolyBuild's required dependancies.  Please consider" +
           " reading over the README file again to remedy this.")
    quit

# Import Local Process
import logic

if __name__ == '__main__':
    print ("\n\n\n\n-----------------------------------------------------")
    print ("  Welcome to PolyBuild Isometric Client / Build Bot  ")
    print ("       for use with Minecraft (Copyright Mojang AB)  ")
    print ("-----------------------------------------------------")
    
    config = ConfigParser.RawConfigParser()
    config.readfp(open('config.txt', 'r+'))
    
    if config.has_section("Account"):
        username = config.get("Account", "username")
        password = config.get("Account", "password")
    else:
        username = raw_input("Minecraft Account Username: ")
        password = raw_input("Minecraft Account Password: ")

        config.add_section("Account")
        config.set("Account", "username", username)
        config.set("Account", "password", password)
    #End of Account switch

    if config.has_section("Options"):
        automated = config.get("Options", "automated")
        logLevel = config.get("Options", "logLevel")
        silent = config.get("Options", "silent")
    else:
        automated = False
        logLevel = "DEBUG"
        silent = True

        config.add_section("Options")
        config.set("Options", "automated", False)
        config.set("Options", "logLevel", "DEBUG")
        config.set("Options", "silent", True)
    #End of Options switch
    config.write(open('config.txt', 'w+'))
    
    loginurl = "http://www.minecraft.net/game/getversion.jsp?"
    
    print ("\n\nPlease wait while we login to minecraft.net")
    login = mechanize.Browser()
    loginResult = login.open(loginurl + "user=%s&password=%s&version=%s"%(username,password,12)).read()
    
    try:
        if "Bad" in loginResult:
            print ("minecraft.net says your username or password was wrong.")
        elif "Error" in loginResult:
            print ("minecraft.net raised an error.  Something went wrong.")
        elif "Old" in loginResult:
            print ("minecraft.net says we are outdated.  Go get a new PolyBuild version!")
        else:
            print ("minecraft.net says we logged in successfully!")
            loginResult = loginResult.split(":")
            username    = loginResult[2]
            session_id  = loginResult[3]
    except:
        print ("We got an unexpected response from minecraft.net")
    
    argv = {"username": username,
            "session_id": session_id,
            "automated": automated,
            "logLevel": logLevel,
            "silent": silent}
    
  #  ProcessLogic = Process(target=logic.run, args=argv)
  #  ProcessLogic.start()
#End of core insertion point
