import numpy as np
import scipy
from scipy.linalg import eigh_tridiagonal
"""
Created on Sun Jan  9 14:22:31 2022

@author: janos
"""
def solver(mass, potential_data, select_range=None):
    """Soll die vorhin ausgegebenen Daten in die benötigten Werte umrechnen

    """
    delta = np.abs(potential_data[0][0]-potential_data[-1][0])/len(potential_data[:,0])
    a = 1 / (mass * delta ** 2)
# rechner der energien und wellenfunktionen
    diagonale = np.array([a + ii for ii in potential_data[:,1]])
    off_diagonale = np.array([-a / 2] * (len(potential_data[:,1])-1))
    energie_data, wavefct = scipy.linalg.eigh_tridiagonal(diagonale, off_diagonale)
# normierung der Wellenfunktionen
    wavefunc_data = wavefct.T
    for index, wfunc in enumerate(wavefunc_data):
        wavefunc_data[index, :] = wfunc / (np.sqrt(delta * np.sum(wfunc ** 2)))
# Berechnung von Erwartungswerten
    expvalues_data = np.array([])
    for wfunc in wavefunc_data:
        expvalues_data = np.append(expvalues_data,
                              [delta * np.sum(wfunc ** 2 * potential_data[:,0] ** 2)],
                              axis=0)

    return energie_data, wavefunc_data, expvalues_data

print(solver(4, np.array([[-20.,  35.],[-10.,   0.],[  0.,   2.],[ 10.,   0.],[ 20.,  35.]])))
