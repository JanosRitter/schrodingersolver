"""System modules"""
import numpy as np
from scipy.linalg import eigh_tridiagonal

def solver(mass, potential_data, first_ev = 1, last_ev = 10):
    """
    Solver function to calculate energie eigenvalues and the wavefunctions
    for the schrodinger euqation.

    Args:
        mass (int): Mass of the particel within the potential
        potential_data (2darray): An array containing a linspaced x axis in the
        first column and the potential data in the second column.
        first_ev (int): First egenvalue, that has to be calculated
        last_ev (int): Last eigenvalue, that has to be calculated

    Returns:
        energie_data_slice (1darray): An array containing the energie eigenvalues
        in increasing order. The length correponds to the first and last eigenvalue
        pot_wavefunc_data (ndarray): An array containing the x axis data in the
        first column and a normalized wavefunction in the other columns. The number
        of wavefunctions corresponds to the first and last eigenvalue.
        wavefunc_data_slice (ndarray): An array that only contains a normalized
        wavefunction in each column.
    """
    delta = np.abs(potential_data[0][0]-potential_data[-1][0])/len(potential_data[:,0])
    alpha = 1 / (mass * delta ** 2)
# rechner der energien und wellenfunktionen
    diagonale = np.array([alpha + ii for ii in potential_data[:,1]])
    off_diagonale = np.array([-alpha / 2] * (len(potential_data[:,1])-1))
    energie_data, wavefct = eigh_tridiagonal(diagonale, off_diagonale)

    energie_data_slice = energie_data[(first_ev - 1):last_ev]

# normierung der Wellenfunktionen
    wavefunc_data = wavefct.copy().T
    for index, wfunc in enumerate(wavefunc_data):
        norm = 1 / (np.sqrt(delta * np.sum(wfunc ** 2)))
        wavefunc_data[index, :] = wfunc * norm

    wavefunc_data_slice = wavefunc_data.T[:,first_ev - 1:last_ev]
    expand_pot = np.expand_dims(potential_data[:,0], axis=1)
    pot_wavefunc_data = np.concatenate((expand_pot, wavefunc_data_slice), axis=1)


    return energie_data_slice, pot_wavefunc_data, wavefunc_data_slice



def calculate_expvalues(potential_data, wavefunc_data_slice):
    """
    Calculates the expvalues of the position operator
    and the uncertainty of these values

    Args:
        potential_data (2darray): An array containing the x-axis
                                needed for the calculation
        wavefunc_data_slice (ndarray): An array containing the first
                                        wave functions corresponding to given
                                        eigenvalues in each column needed for calculation
    Returns:
        expvalues_data (2darray): An array containing the expvalues in the first
                                    column and the uncertainty in the second column
    """

    delta = np.abs(potential_data[0][0]-potential_data[-1][0])/len(potential_data[:,0])

    expvalues = np.array([])
    for wfunc in wavefunc_data_slice.T:
        expvalues = np.append(expvalues,
                              [delta * np.sum((wfunc ** 2) * potential_data[:,0])],
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
