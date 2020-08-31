#dilution of high volume oncoscan (>180 ng/uL) and cytoscan (>560 ng/uL) DNA isolates
#x must be in nanograms/uL

import eel
import os
#change directory to where web folder is
os.chdir('..../Documents/CytogeneticScripts/dilution_app')
eel.init("web")

@eel.expose
def oshigh(startdil):
    x = int(startdil)
    if x >= 180 and x < 400:
        dil = (x * 3)/50
        buffer = round(dil - 3)
        result = f"use {buffer} uL of buffer and 3 uL of sample"
        return result
    elif x >= 400:
        dil = (x * 2)/50
        buffer = round(dil - 2)
        result = f"use {buffer} uL of buffer and 2 uL of sample"
        return result
    else:
        result = f"This does not need to be diluted!"
        return result
@eel.expose
def cshigh(startdil):
    x = int(startdil)
    if x >= 560:
        csdil = (x * 2)/80
        buffer = round(csdil - 2)
        result = f"use {buffer} uL of buffer and 2 uL of sample"
        return result
    else:
        result = f"This does not need to be diluted!"
        return result

#need mode for other browser besides chrome
eel.start("home.html", mode="safari")
