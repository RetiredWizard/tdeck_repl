# tdeck_repl
LILYGO T-Deck Virtual REPL

Placing code.py and tdeck_repl.py on the LilyGO [T-DECK](https://www.lilygo.cc/products/t-deck) will present a virtual REPL on the device keyboard when it boots. The trackball will function as an up/down/left/right arrow for accessing the command line history and edit functions.  

To generate an equal sign (=) enter an underscore followed by a dash (_-) and to generate square brackets enter a parenthesis followed or proceeded by a plus sign ( [ = (+, ] = +) )

In order to enable T-Deck keyboard input in python scripts add the following block of code to the import section of your code:
```py
try:
    from tdeck_repl import input
except:
    pass
