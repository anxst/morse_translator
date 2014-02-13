from Tkinter import Tk
from tkFileDialog import askopenfilename
from time import sleep
try:
    import winsound
except ImportError:
    import os
    def playsound(frequency,duration):
        #apt-get install beep if not installed
        os.system('beep -f %s -l %s' % (frequency,duration))
else:
    def playsound(frequency,duration):
        winsound.Beep(frequency,duration)


morseDict = {
' ': 'x',
'a': '.-',
'b': '-...',
'c': '-.-.',
'd': '-..',
'e': '.',
'f': '..-.',
'g': '--.',
'h': '....',
'i': '..',
'j': '.---',
'k': '-.-',
'l': '.-..',
'm': '--',
'n': '-.',
'o': '---',
'p': '.--.',
'q': '--.-',
'r': '.-.',
's': '...',
't': '-',
'u': '..-',
'v': '...-',
'w': '.--',
'x': '-..-',
'y': '-.--',
'z': '--..',
'1': '.----',
'2': '..---',
'3': '...--',
'4': '....-',
'5': '.....',
'6': '-....',
'7': '--...',
'8': '---..',
'9': '----.',
'0': '-----',
'.': '.-.-.-',
',': '--..--',
'?': '..--..',
'\'': '.----.',
'!': '-.-.--',
'/': '-..-.',
'(': '-.--.',
')': '-.--.-',
'&': '.-...',
':': '---...',
';': '-.-.-.',
'=': '-...-',
'+': '.-.-.',
'-': '-....-',
'_': '..--.-',
'"': '.-..-.',
'$': '...-..-',
'@': '.--.-.'
}

print ("Please provide the text file you wish to translate!")
Tk().withdraw() 
filename = askopenfilename()
with open(filename, "r") as f:
    read_data = f.read()
    for line in read_data:
        message = line.lower()
        translated = ' '.join([morseDict[eachletter] for eachletter in message])
        morseStr = translated
        for eachletter in morseStr:
            if eachletter == "x":
                print "\n"
            else:
                print eachletter,
            if eachletter == '-':
                playsound(800, 600)
            elif eachletter == '.':
                playsound(800, 200)
            elif eachletter == 'x':
                sleep(1.4)
            else:
                sleep(0.2)  


