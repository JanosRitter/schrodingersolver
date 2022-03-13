"""System modules"""
import os
import numpy as np



def _read_schrodinger(inputfilepath):
    """
    Reads the input file "schrodinger.inp" that has the user
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

    mass = float(schrodingerslist[0].split()[0])
    xmin = float(schrodingerslist[1].split()[0])
    xmax = float(schrodingerslist[1].split()[1])
    npoint = int(schrodingerslist[1].split()[2])
    x_axis_data = (xmin, xmax, npoint)
    first_ev = int(schrodingerslist[2].split()[0])
    last_ev = int(schrodingerslist[2].split()[1])
    interpoltype = schrodingerslist[3].split()[0]
    nr_interpol_p = int(schrodingerslist[4].split()[0])
    list_xy_dec = []
    for ii in range(5, len(schrodingerslist)):
        list_xy_dec.append(list(schrodingerslist[ii].split()))
    array_xy_dec = np.array(list_xy_dec)
    interpolxydeclarations = array_xy_dec.astype(np.float)

    return mass, x_axis_data, first_ev, last_ev, interpoltype, interpolxydeclarations








def filesaver(dirname, potential_data, energie_data, wavefunc_data, expvalues_data):
    """
    Saves the calculated data in .dat files
    Args:
        dirname (str): The directory name for the data that is meant to be safed
        potential_data (2darray): An array containing the linspaced x-coordinates
                                and the given potential
        energie_data (1darray): An array containing the eigenvalues of the given problem
        wavefunc_data (ndarray): An array where each of the n columns contains the normalized
                                wavefunction of the corresponding eignvalue
        expvalues_data (2darray): An array containing the expected values of the position
                                operator in the first column and the uncertainty of the
                                position operator
    Returns:
        .dat files in given directory
    """
    potentialpath = os.path.join(dirname, "potential.dat")
    energiepath = os.path.join(dirname, "energie.dat")
    wavefuncpath = os.path.join(dirname, "wavefunc.dat")
    expvaluespath = os.path.join(dirname, "expvalues.dat")
    np.savetxt(potentialpath, potential_data)
    np.savetxt(energiepath, energie_data)
    np.savetxt(wavefuncpath, wavefunc_data)
    np.savetxt(expvaluespath, expvalues_data)



def plotfilereader(dirname):
    """Function for reading the plotfiles"""

    potentialpath = os.path.join(dirname, "potential.dat")
    energiepath = os.path.join(dirname, "energie.dat")
    wavefuncpath = os.path.join(dirname, "wavefunc.dat")
    expvaluespath = os.path.join(dirname, "expvalues.dat")
    potential_data = np.loadtxt(potentialpath)
    energie_data = np.loadtxt(energiepath)
    wavefunc_data = np.loadtxt(wavefuncpath)
    expvalues_data = np.loadtxt(expvaluespath)

    return potential_data, energie_data, wavefunc_data, expvalues_data
