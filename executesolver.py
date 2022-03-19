"""
This is an executable script that uses the modules filemanger,
interpolation, graphicsplotter, and solver to solve the Schrodingers
equation and graphicate the results
"""
import os
import sys, getopt
from moduls.filemanager import _read_schrodinger, filesaver
from moduls.interpolation import interpolation
from moduls.solver import solver, calculate_expvalues
from moduls.graphicsplotter import plotting


def schrodinger_solver(dirname, factor):
    """
    This function solves the 1D Schrodinger equation using the moduls
    filemanger, interpolation, graphicsplotter, and solver. The function reads
    in an input file schrodinger.inp and converts the given data into an
    eigenvalue problem.

    Structur of input file:
        (float) # mass
        (float) (float) (int) # xMin xMax nPoint
        (int) (int) # first and last eigenvalue to print
        (str(can be linear, polynomial, or cspline)) # interpolation type
        (int) # nr. of interpolation points and xy declarations
        (float) (float)
        ...

    Example:
        2.0 # mass
        -20.0 20.0 1999 # xMin xMax nPoint
        1 16 # first and last eigenvalue to include in the output
        linear # interpolation type
        8 # nr. of interpolation points and xy declarations
        -20.0 100.0
        -8.0 -1.5
        -7.0 -1.5
        -0.5 1.8
        0.5 1.8
        7.0 -1.5
        8.0 -1.5
        20.0 100.0

    """

    try:
        input_path = os.path.join(dirname, "schrodinger.inp")
        mass, x_axis_data, first_ev, last_ev, ipoltype, ipoldecla = _read_schrodinger(input_path)

    except FileNotFoundError:
        msg = "Input file or path was not found."
        print(msg)
    else:
        pot_data = interpolation(ipoldecla, x_axis_data, interpoltype = ipoltype)

        energie_data, wavefunc_data, wavefunc_data_slice = solver(mass, pot_data, first_ev, last_ev)

        expvalues_data = calculate_expvalues(pot_data, wavefunc_data_slice)

        filesaver(dirname, pot_data, energie_data, wavefunc_data, expvalues_data)

        plotting(dirname, pot_data, energie_data, wavefunc_data, expvalues_data, factor)





def parsecommand(argv):
    """
    Function used to parse commands from the command line into executesolver.py
    """

    dirname = ""
    factor = 0.5
    try:
        opts, args = getopt.getopt(argv,"hi:o:f:",["help", "ifile=", "ofile=", "factor="])
    except getopt.GetoptError as err:
        print(err)
        print('Help')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('Help')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            dirname = arg
        elif opt in ("-f", "--factor"):
            factor = arg

    return dirname, factor




if __name__ == "__main__":
    directoryname, scal_factor = parsecommand(sys.argv[1:])
    schrodinger_solver(directoryname, scal_factor)
