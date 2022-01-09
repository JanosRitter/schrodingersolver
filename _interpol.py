#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 18:55:28 2022

@author: janos
"""
import numpy as np
import scipy
from scipy.interpolate import interp1d, KroghInterpolator, CubicSpline

def Interpolation(interpolxydeclarations, x_axis_data, interpoltype = 'cspline'):
    """Checks the interpolatioin type and interpolates the potential.
    creates the potential.dat for plotting

    Args:
        interpolxydeclarations (array): Contains data points of the potential 
        x_axis_data (list?): Contains the start and the end of the x-axis
        and the number of points
        interpoltype (str): type of interpolation to be used

    Returns:
        xkoords: the x koordinates of the potential
        ykoords: the interpolates y koordinates for the potential
        or Error Msg if Typ is not linear, cspline or polynomial
    """
    #if interpoltype not == "linear", "polynomial", "cspline":
        #print("unvalid type, please enter either linear,"
              #"polynomial or cspline the default cspline will be used")

    #Xmin = float("".join(xMin))
    #Xmin = float("".join(xMax))
    #Npoint = float("".join(nPoint))
# converted list into string into float, because linspace wont work otherwise
    #xkoords = np.linspace(Xmin, Xmax, Npoint)

    #Xpot = [float(ii) for ii in xPot]
    #Ypot = [float(ii) for ii in yPot]

    if interpoltype == "linear":
        interpolfunc = scipy.interpolate.interp1d(interpolxydeclarations[:,0], interpolxydeclarations[:,1])

    elif interpoltype == "polynomial":
        interpolfunc = scipy.interpolate.CubicSpline(interpolxydeclarations[:,0], interpolxydeclarations[:,1])

    elif interpoltype == "cspline":
        interpolfunc = scipy.interpolate.KroghInterpolator(interpolxydeclarations[:,0], interpolxydeclarations[:,1])
    else:
        print("unvalid type, please enter either linear,"
              "polynomial or cspline the default cspline will be used")
    x_potential = np.linspace(x_axis_data[0],x_axis_data[1],x_axis_data[2])
    y_potential = interpolfunc(x_potential)
    potential_data = np.transpose(np.vstack((x_potential, y_potential)))

    return potential_data


print(Interpolation(np.array([[-20.,  35.],[-10.,   0.],[  0.,   2.],[ 10.,   0.],[ 20.,  35.]]),
(-20.0, 20.0, 1999),'cspline'))
