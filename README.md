# tdeck_repl
LILYGO T-Deck Virtual REPL

Placing code.py and tdeck_repl.py on the LilyGO [T-DECK](https://www.lilygo.cc/products/t-deck) will present a virtual REPL on the device keyboard when it boots. The trackball will function as an up/down/left/right arrow for accessing the command line history and edit functions.  

To generate an equal sign (=) enter an underscore followed by a dash (_-) and to generate square brackets enter a parenthesis followed or proceeded by a plus sign ( [ = (+, ] = +) ).
Pressing the speaker key (just left of the enter key) will generate the dollar sign ($).

Multi-key translation table:  
    _-   ->   =  
    (+   ->   [  
    +)   ->   ]  
    (-   ->   <  
    -)   ->   >  
    _#   ->   ^  
    _/   ->   \  
    -/   ->   %  

In order to enable T-Deck keyboard input in python scripts add the following block of code to the import section of your code:
```py
try:
    from tdeck_repl import input
except:
    pass
```
The Virtual REPL will treat a file named virtcode.py in the root directory ('/') the way the native REPL treats a code.py file, that is it will be executed within the Virtual REPL when the Microcontroller is powered up or reset. When the virtcode.py program exits the Virtual REPL will take over control.
