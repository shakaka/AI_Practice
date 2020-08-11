#! python2
# mcb.py - saves and loads pieces of text to the clipboard
# usage: py.exe mcb.py save <keyboard> - saves clipboard to keyboard
#        py.exe mcb.py <keyboard> - loads keyboaSrd to clipboard
#        py.exe mcb.py list - loads all keyboard to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

#save clipboard to content
if len(sys.argv)==3:
    if sys.argv[1].lower()=='save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
#delete
    elif sys.argv[1].lower()='delete':
        del mcbShelf[sys.argv[2]]
    else:
        pass

elif len(sys.argv) == 2:
    # list keyboard and load content
    if sys.argv[1].lower()=='list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
