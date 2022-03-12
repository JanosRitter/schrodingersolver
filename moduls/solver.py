import numpy as np
from scipy.linalg import eigh_tridiagonal
"""
Created on Sun Jan  9 14:22:31 2022

@author: janos
"""
def solver(mass, potential_data, first_ev = 1, last_ev = 10, select_range=None):
    """Soll die vorhin ausgegebenen Daten in die benötigten Werte umrechnen

    """
    delta = np.abs(potential_data[0][0]-potential_data[-1][0])/len(potential_data[:,0])
    a = 1 / (mass * delta ** 2)
# rechner der energien und wellenfunktionen
    diagonale = np.array([a + ii for ii in potential_data[:,1]])
    off_diagonale = np.array([-a / 2] * (len(potential_data[:,1])-1))
    energie_data, wavefct = eigh_tridiagonal(diagonale, off_diagonale)
    
    energie_data_slice = energie_data[(first_ev - 1):last_ev]
    
# normierung der Wellenfunktionen
    wavefunc_data = wavefct.copy().T
    for index, wfunc in enumerate(wavefunc_data):
        norm = 1 / (np.sqrt(delta * np.sum(wfunc ** 2)))
        wavefunc_data[index, :] = wfunc * norm
    
    wavefunc_data_slice = wavefunc_data.T[:,first_ev - 1:last_ev]
        
    pot_wavefunc_data = np.concatenate((np.expand_dims(potential_data[:,0], axis=1), wavefunc_data_slice), axis=1)
    
# Berechnung von Erwartungswerten
    expvalues = np.array([])
    for wfunc in wavefunc_data_slice.T:
        expvalues = np.append(expvalues,
                              [delta * np.sum(wfunc ** 2 * potential_data[:,0])],
                              axis=0)
    
    """
    Calculates the uncertainity :math:`\\Delta x` defined as

    .. math::

       \\Delta x = \\sqrt{<x^2> - <x>^2}

    for each wavefunction.

    Args:
        xcoords (1darray): Array containing the x-coordinates
        wfuncs (ndarray): Array containing the wave functions that
            correspond to the x-coordinates
        xmin: Minimum Value for x
        xmax: Maximum Value for x
        npoints: Number of x values in range (xmin, xmax)
    Returns:
        uncertainty (1darray): The uncertainity of the x-coordinate.

    """
#calculating uncertainty
    uncertainty = np.array([])

    for wfunc, expv in zip(wavefunc_data_slice.T, expvalues):
        expvalsq = np.sum((wfunc ** 2) * (potential_data[:,0] ** 2)) * delta
        uncertainty = np.append(uncertainty, [np.sqrt(expvalsq - expv ** 2)],
                                axis=0)
    
    expvalues_array = np.array([expvalues])
    uncertainty_array = np.array([uncertainty])
    
    
    expvalues_data = np.concatenate((expvalues_array.T, uncertainty_array.T), axis = 1)
   
    return energie_data_slice, pot_wavefunc_data, wavefunc_data_slice


    
def calculate_expvalues(potential_data, wavefunc_data_slice):
    
    delta = np.abs(potential_data[0][0]-potential_data[-1][0])/len(potential_data[:,0])
    
    expvalues = np.array([])
    for wfunc in wavefunc_data_slice.T:
        expvalues = np.append(expvalues,
                              [delta * np.sum(wfunc ** 2 * potential_data[:,0])],
                              axis=0)
    
    uncertainty = np.array([])

    for wfunc, expv in zip(wavefunc_data_slice.T, expvalues):
        expvalsq = np.sum((wfunc ** 2) * (potential_data[:,0] ** 2)) * delta
        uncertainty = np.append(uncertainty, [np.sqrt(expvalsq - expv ** 2)],
                                axis=0)
    
    expvalues_array = np.array([expvalues])
    uncertainty_array = np.array([uncertainty])
    
    
    expvalues_data = np.concatenate((expvalues_array.T, uncertainty_array.T), axis = 1)
    
    return expvalues_data




