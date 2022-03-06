#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 16:02:58 2022

@author: janos
"""
"""
This is an executable script that uses the modules _fileio,
_interpolation, graphics, and solvers to solve the Schrodingers
equation and graphicate the results
"""


import os
import numpy as np
from filemanager import _read_schrodinger2, filesaver, plotfilereader
from _interpol import Interpolation
from solver import solver
from graphicsplotter import plotting


def schrodingers_solver(dirname):
    """
    Solves the 1D Schrodinger's time-independent equation
    for any type of potential and graphicates its solution. The
    output graphs are shown on screen after executing the program and
    the data generated by solving the Schrodinger's equation is written
    in a series of output files (potentials.dat, energies.dat, wavefuncs.dat,
    and expvalues.dat). It needs an input file named schrodinger.inp with
    the data needed to solve the equation. The schrodinger.inp file needs to
    have following format:

        (float) # mass
        (float) (float) (int) # xMin xMax nPoint
        (int) (int) # first and last eigenvalue to print
        (str(can be linear, polynomial, or cspline)) # interpolation type
        (int) # nr. of interpolation points and xy declarations
        (float) (float)
        ...

    Example:
        2.0 # mass
        -2.0 2.0 1999 # xMin xMax nPoint
        1 5 # first and last eigenvalue to print
        linear # interpolation type
        2 # nr. of interpolation points and xy declarations
        -2.0 0.0
        2.0 0.0

    """
    #"~/Pythonzeug/Spyderzeug/schrodingersolver"
    try:
        mass, xmin, xmax, npoint, x_axis_data, first_ev, last_ev, interpoltype, nr_interpol_p, interpolxydeclarations = _read_schrodinger2(os.path.join(dirname, "schrodinger.inp"))
        print(mass, xmin, xmax, npoint, x_axis_data, first_ev, last_ev, interpoltype, nr_interpol_p, interpolxydeclarations)
    except FileNotFoundError:
        msg = "Input file or path was not found."
        print(msg)
    else:
        potential_data = Interpolation(interpolxydeclarations, x_axis_data, interpoltype = 'cspline')
        
        energie_data_slice, wavefunc_data_slice, expvalues_data = solver(mass, potential_data, first_ev, last_ev, select_range=None)
        
        filesaver(dirname, potential_data, energie_data_slice, wavefunc_data_slice, expvalues_data)
        
        plotting(dirname, potential_data, energie_data_slice, wavefunc_data_slice, expvalues_data, x_bound=None)
        print(potential_data)
        print(energie_data_slice, wavefunc_data_slice, expvalues_data)
        
print(schrodingers_solver(""))
        