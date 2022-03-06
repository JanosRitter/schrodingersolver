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


    plt.figure(figsize=(15, 7.5), dpi=80)
    plt.subplot(1,2,1)

    #plotting Potential:
    plt.plot(potential_data[:,0], potential_data[:,1])
    #plotting Wfuncs:
    plt.plot(wavefunc_data[:,0], wavefunc_data[:,1] + energie_data[0])
    plt.plot(wavefunc_data[:,0], wavefunc_data[:,2] + energie_data[1])
    plt.plot(wavefunc_data[:,0], wavefunc_data[:,3] + energie_data[2])
    plt.plot(wavefunc_data[:,0], wavefunc_data[:,4] + energie_data[3])
    plt.plot(wavefunc_data[:,0], wavefunc_data[:,5] + energie_data[4])
    plt.plot(wavefunc_data[:,0], wavefunc_data[:,6] + energie_data[5])
    plt.plot(wavefunc_data[:,0], wavefunc_data[:,7] + energie_data[6])
    plt.plot(wavefunc_data[:,0], wavefunc_data[:,8] + energie_data[7])
    plt.plot(wavefunc_data[:,0], wavefunc_data[:,9] + energie_data[8])
    
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
