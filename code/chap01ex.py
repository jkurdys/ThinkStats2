from __future__ import print_function, division

import sys
import numpy as np
import thinkstats2
import nsfg

from collections import defaultdict

def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz',
                nrows=None):
    """Reads the NSFG respondent data.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip', nrows=nrows)
    CleanFemResp(df)
    return df


def CleanFemResp(df):
    """Recodes variables from the respondent frame.

    df: DataFrame
    """
    pass

def validate():
    resp = ReadFemResp()
    pregs = sum(resp.pregnum.value_counts())

    preg = nsfg.ReadFemPreg()


if __name__=='__main__':
    resp = ReadFemResp()
    preg = nsfg.ReadFemPreg()
    preg_map = nsfg.MakePregMap(preg)
    print(preg_map)