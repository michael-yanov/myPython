#! python3

import pyperclip

#text = 'fgjflkg\n gdfkglkdf\n dgjlkdfj\n dkjglkdfj\n ldkfjglkdfg'

text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i] 

text = '\n'.join(lines)
pyperclip.copy(text)