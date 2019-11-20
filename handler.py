import os
import sys

# Author: Caleb Sykes / Date: 20/11/2019

lis = []
dict = {}
count = 0
count2 = 0
count3 = -1
count4 = -1

if len(sys.argv) > 2:
    print("Error: 1 argument needed, got "+str((len(sys.argv))-1))
    exit()
elif sys.argv[1] == "-h":
    print("Usage: python3 handler.py [EXPLOIT]\nIf shows weird output or not working keep retrying")
os.system("touch list.txt")
query = os.system("msfconsole -x \'search "+str(sys.argv[1])+";exit;\' > list.txt")
with open("list.txt","r+") as f:
    lines = f.readlines()
    for l in lines:
        count += 1
        if len(l) >= 100:
            count2 += 1
            if count2 > 2:
                count3 += 1
                re = l.split(" ",7)
                lis.append(re[5])
                while("" in lis):
                    lis.remove("")
                print(str(count3)+") "+l[6:-1])
    f.close()

for i in lis:
    count4 += 1
    dict[count4] = i
choice = input("\nWhat module would you like to use (Pick a number):")
query2 = os.system("msfconsole -x \'use "+dict[int(choice)]+"\'")
os.remove("list.txt")
