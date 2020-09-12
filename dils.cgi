#!/usr/bin/python3
#dilution of high volume oncoscan (>180 ng/uL) and cytoscan (>560 ng/uL) DNA isolates
#x must be in nanograms/uL

import cgi
import os


print("Content-Type: text/html")
print()
form = cgi.FieldStorage()

form_startdil = form.getvalue("startdil")

if form.getvalue("array") == "Oncoscan":
    x = int(form_startdil)
    if x >= 180 and x < 400:
        dil = (x * 3)/50
        buffer = round(dil - 3)
        #result = f"use {buffer} uL of buffer and 3 uL of sample"
        result = "use {0} uL of buffer and 3 uL of sample".format(buffer)
        #return result
        print(result)
    elif x >= 400:
        dil = (x * 2)/50
        buffer = round(dil - 2)
        #result = f"use {buffer} uL of buffer and 2 uL of sample"
        result = "use {0} uL of buffer and 2 uL of sample".format(buffer)
        #return result
        print(result)
    else:
        #result = f"This does not need to be diluted!"
        result = "This does not need to be diluted!"
        #return result
        print(result)

else:
    x = int(form_startdil)
    if x >= 560:
        csdil = (x * 2)/80
        buffer = round(csdil - 2)
        #result = f"use {buffer} uL of buffer and 2 uL of sample"
        result = "use {0} uL of buffer and 2 uL of sample".format(buffer)
        #return result
        print(result)
    else:
        #result = f"This does not need to be diluted!"
        result = "This does not need to be diluted"
        #return result
        print(result)

