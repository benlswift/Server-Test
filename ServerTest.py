import os
import tkinter as tk


fh = os.popen("ServerTest.bat")
output = fh.read()
print ("This is the output of ServerTest.bat:", output)
if "Request timed out" in output: 
    print ("STATION OFF AIR - ALERT HEAD OF SYSTEMS")
    master = tk.Tk()
    whatever_you_do = "STATION OFF AIR - ALERT HEAD OF SYSTEMS"
    msg = tk.Message(master, text = whatever_you_do)
    msg.config(bg='red', font=('times', 50, 'bold'))
    msg.pack()
fh.close()
