#! python3
# mcb.pyw - Saves and loads pieces of text to the cliboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3:
        if sys.argv[1].lower() =='save':
                mcbShelf[sys.argv[2]] = pyperclip.paste()
        elif sys.argv[1].lower()=='delete':
                del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
# List kywords and load content.
        if sys.argv[1].lower()=='list':
                pyperclip.copy(str(list(mcbShelf.keys())))
        elif sys.argv[1] in mcbShelf:
                pyperclip.copy(mcbShelf[sys.argv[1]])



mcbShelf.close()
