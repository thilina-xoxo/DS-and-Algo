#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    ss = s
    hh = int(ss[:2])
    if ("PM" in ss) and (hh != 12):
        hh += 12
    if ("AM" in ss) and (hh == 12):
        hh = 00

    hour = (str(hh)).zfill(2)  # what the fuck is this

    return f"{hour}{s[2:-2]}"


if __name__ == '__main__':


    s = input()

    result = timeConversion(s)

    print(result)


