fullRambam = open("rWithNikud.txt", "w")

import os
for file in os.listdir("allRambam"):
    # open every file 
    f = open("allRambam/" + file).read( encoding = 'iso-8859-8').splitlines()
    for line in f:
        fullRambam.write(line)
    # write that line to fullRambam

