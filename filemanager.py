"""
This file contains a function for reading of a "schrodinger.inp" file which 
contains the necessary informations for the schrodinger problem 
"""
import os
import numpy as np
import scipy
from scipy.interpolate import interp1d, KroghInterpolator, CubicSpline


def _read_schrodinger(inputfilepath):
    """Reads the input file "schrodinger.inp" that has the user
    defined data which describes the problem

    Argument:
        inputfilepath (str): Path of the file which is going to be read

    Return:
        input_data (dict): A dictionary that contains the different parameters :
        mass, x_min, x_max, nPoint, x_axis_data, first_EV, last_EV, interpol_type,
        nr_interpol_p, and interpol_xy_declarations (interpol_xy_declarations
        exist as an array and as a list only the array version is returned)
    """
    schrodingerslist = [line.rstrip('\n') for line in open(inputfilepath, 'r')]

    input_data = dict()
    input_data['mass'] = float(list(schrodingerslist[0].split(" "))[0])
    input_data['xmin'] = float(list(schrodingerslist[1].split(" "))[0])
    input_data['xmax'] = float(list(schrodingerslist[1].split(" "))[1])
    input_data['npoint'] = int(list(schrodingerslist[1].split(" "))[2])
    input_data['x_axis_data'] = (input_data['xmin'], input_data['xmax'], input_data['npoint'])
    input_data['first_ev'] = int(list(schrodingerslist[2].split(" "))[0])
    input_data['last_ev'] = int(list(schrodingerslist[2].split(" "))[1])
    input_data['interpoltype'] = list(schrodingerslist[3].split(" "))[0]
    input_data['nr_interpol_p'] = int(list(schrodingerslist[4].split(" "))[0])
    list_xy_dec = list()
    for ii in range(5, len(schrodingerslist)):
        list_xy_dec.append(list(schrodingerslist[ii].split(" ")))
    array_xy_dec = np.array(list_xy_dec)
    input_data['interpolxydeclarations'] = array_xy_dec.astype(np.float)
    
    return input_data


#print(_read_schrodinger("schrodinger.inp"))


def _read_schrodinger2(inputfilepath):
    """Reads the input file "schrodinger.inp" that has the user
    defined data which describes the problem

    Argument:
        inputfilepath (str): Path of the file which is going to be read

    Return:
        The different parameters :
        mass, x_min, x_max, nPoint, x_axis_data, first_EV, last_EV, interpol_type,
        nr_interpol_p, and interpol_xy_declarations (interpol_xy_declarations
        exist as an array and as a list only the array version is returned)
    """
    schrodingerslist = [line.rstrip('\n') for line in open(inputfilepath, 'r')]
    
   
    mass1 = float(schrodingerslist[0].split()[0])
    xmin = float(schrodingerslist[1].split(" ")[0])
    xmax = float(schrodingerslist[1].split(" ")[1])
    npoint = int(schrodingerslist[1].split(" ")[2])
    x_axis_data = (xmin, xmax, npoint)
    first_ev = int(schrodingerslist[2].split(" ")[0])
    last_ev = int(schrodingerslist[2].split(" ")[1])
    interpoltype = schrodingerslist[3].split(" ")[0]
    nr_interpol_p = int(schrodingerslist[4].split(" ")[0])
    list_xy_dec = list()
    for ii in range(5, len(schrodingerslist)):
        list_xy_dec.append(list(schrodingerslist[ii].split(" ")))
    array_xy_dec = np.array(list_xy_dec)
    interpolxydeclarations = array_xy_dec.astype(np.float)
    
    return mass1, xmin, xmax, npoint, x_axis_data, first_ev, last_ev, interpoltype, nr_interpol_p, interpolxydeclarations
    





#print(_read_schrodinger2("schrodinger.inp"))



def filesaver(dirname, potential_data, energie_data, wavefunc_data, expvalues_data):
    potentialpath = os.path.join(dirname, "potential.dat")
    energiepath = os.path.join(dirname, "energie.dat")
    wavefuncpath = os.path.join(dirname, "wavefunc.dat")
    expvaluespath = os.path.join(dirname, "expvalues.dat")
    np.savetxt(potentialpath, potential_data)
    np.savetxt(energiepath, energie_data)
    np.savetxt(wavefuncpath, wavefunc_data)
    np.savetxt(expvaluespath, expvalues_data)
    


def plotfilereader(dirname):
    potentialpath = os.path.join(dirname, "potential.dat")
    energiepath = os.path.join(dirname, "energie.dat")
    wavefuncpath = os.path.join(dirname, "wavefunc.dat")
    expvaluespath = os.path.join(dirname, "expvalues.dat")
    potential_data = np.loadtxt(potentialpath)
    energie_data = np.loadtxt(energiepath)
    wavefunc_data = np.loadtxt(wavefuncpath)
    expvalues_data = np.loadtxt(expvaluespath)
    
    return potential_data, energie_data, wavefunc_data, expvalues_data

