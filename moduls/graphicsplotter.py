from matplotlib import pyplot as plt
import numpy as np
import os


def plotting(dirname, potential_data, energie_data, wavefunc_data, expvalues_data, x_bound=None):
    """
    This function is used to visualize the calculated data. The data is visualized in two subplots
    the left subplot contains the potential_data, the wavefunction_data, the energie_data and the expevalues_data of the position operatur
    the right subplot contains the uncertainty of the postion operator and the energie_data the y-axis in both subplots are identical 
    for the easy assignment of the given values
    
    Args:
        dirname (str): the given directory for the saving of the plot
        potential_data (2darray): An array containing the linspaced x-coordinates and the given potential
        energie_data (1darray): An array containing the eigenvalues of the given problem 
        wavefunc_data (ndarray): An array where each of the n columns contains the normalized wavefunction of the corresponding
                                eignvalue
        expvalues_data (2darray): An array containing the expected values of the position operator in the first column and the
                                uncertainty of the position operator
    
    Returns:
        .png file containing the data
    """


    plt.figure(figsize=(10, 8), dpi=80)
    plt.subplot(1,2,1)
    
    skaling = 0.5

    plt.plot(potential_data[:,0], potential_data[:,1])
    
    for ii in range(len(energie_data)):
        plt.axhline(y = energie_data[ii], xmin=potential_data[0][0], xmax=potential_data[-1][0], color = 'silver')
        
    for num in range(wavefunc_data.shape[1]-1):
       color = "blue" if num % 2 else "red" 
       plt.plot(wavefunc_data[:,0], wavefunc_data[:,num+1] * skaling + energie_data[num], color = color)
       
    plt.scatter(expvalues_data[:,0], energie_data, marker = 'x')
    
    
    if x_bound is None:
        plt.xlim(potential_data[:,0].min()*1.1, potential_data[:,0].max()*1.1)
    else:
        plt.xlim(-x_bound,x_bound)
        
    if np.amax(energie_data) > 0:
        plt.ylim(np.amin(potential_data[:,1]) * 1.1, np.amax(energie_data) * 1.2)
    else:
        plt.ylim(np.amin(potential_data[:,1]) * 1.1, 0)
    
    #plt.ylim(np.amin(potential_data[:,1]) * 1.1, np.amax(energie_data) * 1.2)
    
    plt.xlabel("x [Bohr]", size=16)
    plt.ylabel("Energie [Hartree]", size=16)
    
    
    

    plt.subplot(1,2,2)

    plt.scatter(expvalues_data[:,1], energie_data, marker = 'x')
    for ii in range(len(energie_data)):
        plt.axhline(y = energie_data[ii], xmin=potential_data[0][0], xmax=potential_data[-1][0], color = 'silver')
    

    if x_bound is None:
        plt.xlim(0, expvalues_data[:,1].max()*1.1)
    else:
        plt.xlim(-x_bound,x_bound)
    
    plt.ylim(np.amin(potential_data[:,1]) * 1.1, np.amax(energie_data) * 1.2)
    
    plt.xlabel("[Bohr]", size=16)
    
    
    
        
    filename = os.path.join(dirname, "plots")
    
    plt.savefig(filename)
