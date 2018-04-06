import time
import os
x=os.path.getsize('text_english.txt')
print (x)
while x<2:
    print ('l')
    time.sleep(0.1)
    x=os.path.getsize('text_english.txt')
f=open("text_english.txt", "r")
if f.mode == 'r':
    contents=f.read()
    print(contents)
    f.close()
