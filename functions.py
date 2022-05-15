import sys
import numpy as np
import matplotlib.pyplot as plt

def diff_2(y, x=1, del_g=False, verbose=False, g_l=False):
    """
    diff_2 computes differentions of given function, tailor made for 
    results given by Ansys (path results)

    Parameters:
    y :             y - values of function
    x :             x - values of function
    del_g :         given vector of differences between x - values
    verbose :       prints computational info if True
    g_l :           get_list - returns lists when True, numpy.array() otherwise

    Returns:
    diffs :         second order differentions of data set
    dels :          vector containing deltas (differences between x - values)
                    (may be usefull for loops of results)

    """

    if type(y) == list:
        y_ = np.array(y)
    elif str(type(y)) == "<class 'numpy.ndarray'>":
        y_ = y
    else:
        sys.exit(
            "Data type of argument \"y\" should be \"list\" or \"numpy.ndarray\", not " + str(type(y)))
    
    y_ = np.append(y_, y_[-2])
    y_ = np.insert(y_, 0, (y_[0]-y_[1]))

    if del_g:
        if verbose:
            print(r"del_x based on given vector")
        pass
    else:
        if verbose:
            print(r"del_x computed based on given x-values")
    
        if type(x) == list:
            x_ = np.array(x)
        elif str(type(x)) == "<class 'numpy.ndarray'>":
            x_ = x
        else:
            sys.exit(
                "Data type of argument \"x\" should be \"list\" or \"numpy.ndarray\", not " + str(type(x)))

        x_ = np.append(x_, x_[-1]+(x_[-1]-x_[-2]))
        x_ = np.insert(x_, 0, x_[0]+(x_[0]-x_[1]))
    
    if del_g:
        del_x = del_g
    else:
        del_x = [x_[i+1]-x_[i] for i in range(len(x_)-1)]

    diffs = []
    for i in range(len(del_x)-1):
        diffs.append((y_[i+2]-y_[i])/(del_x[i]+del_x[i+1]))
    diffs = np.array(diffs)

    if g_l:
        diffs = list(diffs)
        del_x = list(del_x)

    return diffs, del_x

def Force_1(x):
    """
    Computes specific force from time.
    WARNING: Only suitable in one case! Definetly not universal function!

    Parameters:
    x :             time

    Returns:
    F :             applied force
    """
    x1=1.; x2=2.; x3=3.; x4=4.; x5=5.; x6=6.; x7=7.; x8=151.1
    f1=0; f2=570; f3=1073; f4=1577; f5=2565; f6=3352; f7=3967; f8=8430
    if x <= x1:
        F = 0
    elif x > x1 and x <= x2:
        F = f1 + ((f2-f1)/(x2-x1)) * (x-x1)
    elif x > x2 and x <= x3:
        F = f2 + ((f3-f2)/(x3-x2)) * (x-x2)
    elif x > x3 and x <= x4:
        F = f3 + ((f4-f3)/(x4-x3)) * (x-x3)
    elif x > x4 and x <= x5:
        F = f4 + ((f5-f4)/(x5-x4)) * (x-x4)
    elif x > x5 and x <= x6:
        F = f5 + ((f6-f5)/(x6-x5)) * (x-x5)
    elif x > x6 and x <= x7:
        F = f6 + ((f7-f6)/(x7-x6)) * (x-x6)
    elif x > x7 and x <= x8:
        F = f7 + ((f8-f7)/(x8-x7)) * (x-x7)
    else:
        sys.exit("Non-valid input time time")
    return F


def Force_2(x):
    """
    Computes specific force from time.
    WARNING: Only suitable in one case! Definetly not universal function!

    Parameters:
    x :             time

    Returns:
    F :             applied force
    """
    x1 = 1.; x2 = 2.;  x3 = 3.;   x4 = 4.;   x5 = 5.;   x6 = 6.;   x7 = 7.;   x8 = 105
    f1 = 0;  f2 = 570; f3 = 1073; f4 = 1577; f5 = 2565; f6 = 3352; f7 = 3967; f8 = 7000
    if x <= x1:
        F = 0
    elif x > x1 and x <= x2:
        F = f1 + ((f2-f1)/(x2-x1)) * (x-x1)
    elif x > x2 and x <= x3:
        F = f2 + ((f3-f2)/(x3-x2)) * (x-x2)
    elif x > x3 and x <= x4:
        F = f3 + ((f4-f3)/(x4-x3)) * (x-x3)
    elif x > x4 and x <= x5:
        F = f4 + ((f5-f4)/(x5-x4)) * (x-x4)
    elif x > x5 and x <= x6:
        F = f5 + ((f6-f5)/(x6-x5)) * (x-x5)
    elif x > x6 and x <= x7:
        F = f6 + ((f7-f6)/(x7-x6)) * (x-x6)
    elif x > x7 and x <= x8:
        F = f7 + ((f8-f7)/(x8-x7)) * (x-x7)
    else:
        sys.exit("Non-valid input time time")
    return F


def dummy():
    print("420pussysmasher69")
    return True