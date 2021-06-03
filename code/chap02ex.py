"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys
from operator import itemgetter

import first
import thinkstats2


def Mode(hist):
    """Returns the value with the highest frequency.

    hist: Hist object

    returns: value from Hist
    """
    mval = None
    mfreq = None
    for val, freq in hist.Items():
        if mfreq == None:
            mfreq = freq
            mval = val
        else:
            if freq > mfreq:
                mfreq = freq
                mval = val
    return mval


def AllModes(hist):
    """Returns value-freq pairs in decreasing order of frequency.

    hist: Hist object

    returns: iterator of value-freq pairs
    """
    sorted_values = sorted(hist.values(), reverse=True)
    sorted_dict = {}
    lst = []

    for v in sorted_values:
        for k in hist.keys():
            if hist[k] == v:
                sorted_dict[k] = hist[k]
    
    for k, v in sorted_dict.items():
        lst.append((k,v))
            
    return lst


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    live, firsts, others = first.MakeFrames()
    hist = thinkstats2.Hist(live.prglngth)

    # test Mode    
    mode = Mode(hist)
    print('Mode of preg length', mode)
    assert mode == 39, mode

    # test AllModes
    modes = AllModes(hist)
    assert modes[0][1] == 4693, modes[0][1]

    for value, freq in modes[:5]:
        print(value, freq)

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
