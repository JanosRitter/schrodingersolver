#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 15:05:15 2022

@author: janos
"""

from matplotlib import pyplot as plt
import numpy as np
import os








def plotting(dirname, potential_data, energie_data, wavefunc_data, expvalues_data, x_bound=None):


    plt.figure(figsize=(10, 8), dpi=80)
    plt.subplot(1,2,1)

    #plotting Potential:
    plt.plot(potential_data[:,0], potential_data[:,1])
    for ii in range(len(energie_data)):
        plt.axhline(y = energie_data[ii], xmin=potential_data[0][0], xmax=potential_data[-1][0], color = 'silver')
    #plotting Wfuncs:
    skaling = 0.5
    for num in range(wavefunc_data.shape[1]-1):
       color = "blue" if num % 2 else "red" 
       plt.plot(wavefunc_data[:,0], wavefunc_data[:,num+1] * skaling + energie_data[num], color = color)
       
    plt.scatter(expvalues_data, energie_data, marker = 'x')
    plt.xlabel("x [Bohr]", size=16)
    plt.ylabel("Energie [Hartree]", size=16)
    
    
    #x_range:
    if x_bound is None:
        plt.xlim(potential_data[:,0].min()*1.1, potential_data[:,0].max()*1.1)
    else:
        plt.xlim(-x_bound,x_bound)
    

    plt.subplot(1,2,2)

    #plotting Potential:
    plt.plot(potential_data[:,0], potential_data[:,1])
    #plotting Wfuncs:
    plt.plot(wavefunc_data[:,0], wavefunc_data[:,1])
    #x_range:
    if x_bound is None:
        plt.xlim(potential_data[:,0].min()*1.1, potential_data[:,0].max()*1.1)
    else:
        plt.xlim(-x_bound,x_bound)
        
    filename = os.path.join(dirname, "plots")
    
    plt.savefig(filename)
