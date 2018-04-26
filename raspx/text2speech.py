from num2words import num2words
from subprocess import call

cmd_beg= 'espeak '
cmd_end= '2>/dev/null'
f=open("full.txt", "r")
if f.mode == 'r':
    text =f.read()

text = text.replace(' ', '_')

call([cmd_beg+text+cmd_end], shell=True)
