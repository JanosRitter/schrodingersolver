"""
Created on Wed Jan  5 18:55:28 2022

@author: janos
"""
import numpy as np
from scipy.interpolate import interp1d, KroghInterpolator, CubicSpline

def interpolation(interpolxydeclarations, x_axis_data, interpoltype = 'cspline'):
    """Checks the interpolatioin type and interpolates the potential.
    creates the potential.dat for plotting

    Args:
        interpolxydeclarations (array): Contains data points of the potential
        x_axis_data (list): Contains the start and the end of the x-axis
        and the number of points
        interpoltype (str): type of interpolation to be used

    Returns:
        potential_data (array): containing the x coordinates and the corressponding
        potential
        or Error Msg if Typ is not linear, cspline or polynomial
    """


    if interpoltype == "linear":
        interpolfunc = interp1d(interpolxydeclarations[:,0], interpolxydeclarations[:,1])

    elif interpoltype == "polynomial":
        interpolfunc = CubicSpline(interpolxydeclarations[:,0], interpolxydeclarations[:,1])

    elif interpoltype == "cspline":
        interpolfunc = KroghInterpolator(interpolxydeclarations[:,0], interpolxydeclarations[:,1])
    else:
        print("unvalid type, please enter either linear,"
              "polynomial or cspline the default cspline will be used")
        interpolfunc = KroghInterpolator(interpolxydeclarations[:,0], interpolxydeclarations[:,1])

    x_potential = np.linspace(x_axis_data[0],x_axis_data[1],x_axis_data[2])
    y_potential = interpolfunc(x_potential)
    potential_data = np.transpose(np.vstack((x_potential, y_potential)))


    return potential_data
