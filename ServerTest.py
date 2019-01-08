import os
import tkinter as tk
import urllib.request
import threading

def run_check():
    threading.Timer(30.0, run_check).start()
    fh = os.popen("ServerTest.bat")
    output = fh.read()
    print ("This is the output of ServerTest.bat:", output)
    if "Request timed out" in output: 
        print ("STATION OFF AIR - ALERT HEAD OF SYSTEMS")
        master = tk.Tk()
        OffAirMessage = "STATION OFF AIR - ALERT HEAD OF SYSTEMS"
        msg = tk.Message(master, text = OffAirMessage)
        msg.config(bg='red', font=('times', 50, 'bold'))
        msg.pack()
    fh.close()

run_check()
