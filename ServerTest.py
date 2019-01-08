import os

fh = os.popen("ServerTest.bat")
output = fh.read()
print ("This is the output of ServerTest.bat:", output)
if "Request timed out" in output: 
    print ("STATION OFF AIR - ALERT HEAD OF SYSTEMS")
fh.close()
