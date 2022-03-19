Schrodingersolver is python package used to numericaly solve the 1D schrodinger 
equation for a given potential.

Developers:
Janos Ritter: https://github.com/JanosRitter
Merlin Böschen

Disclaimer:
This is a student project using very basic numerical algorithms. It might not
be 100% reliable


Description:
The packade reads in an input file and uses his modules and the main executable
skript executesolver.py to solve the 1D time independent schrodinger equation 
for a potential defined in the input file. The results are returned in .dat 
files and are visualized in a file plot.png.


Installation:
The package can be installed by installing a tar archiv of the package or it
can be downloaded under 

https://github.com/JanosRitter/schrodingersolver


Requirements:
This package was developt in spyder version 4.2.1 and written in Python version 3.8.
The used distribution was ubuntu 20.04. The package is using the python 
packages numpy version 1.22.0 and scipy version 1.7.3.

A version of python 3 should be sufficient to run the solver. But no tests in 
other version had been done. Different versions of numpy and scipy might lead to 
slightly different results following different approaches for a numerical solution,
but the results should still be correct.


Usage:
    Input: The input file has to be provided by the user. It is recommended to
    create a new directory with in the "InputOutput/" directory, named after the
    problem (Example: Test1 or HarmOszillator...). The input file is placed 
    inside the directory and HAS TO BE NAMED "schrodinger.inp". The input file 
    should contain a potential somewhat close that is some what close to zero.
    Most input samples cover an x Range of around 10 bohr radians and the 
    depth of the potential should not be greater than a few hartree. Really low
    or high values could screw up the visualization of the data.
        
        The input file has to cantain the following data:
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
            
    Two schrodinger.inp files a included with in the package. The first one
    is in the main directory and an additional input is inside an example
    directory "InputOutput/ExampleIO".
    
    Execution: After the input has been provided. The solver can be executed by 
    typing "python3 executesolver.py" into the console of your system while 
    additionaly providing the input path after using -i for the command line 
    parsing
    
        Example:
            python3 executesolver.py -i InputOutput/Test1
            
    An error message appears if the input path was not found. There is no 
    message for succesful execution.
    
    There is also the possibility to provide a skaling factor for the amplitude
    of the wavefunction within the command line. Typing -f followed by the 
    factor. 
        
        Example:
            python3 executesolver.py -i InputOutput/Test1 -f 0.5
            
    The default value of this factor is set to 0.5 so it is not necessary to 
    provide a skaling factor. The factor can be used for the creation of nicer 
    looking plots. Depending on the potential, the amplitude of a normalized 
    wavefunction
        
    Output: The results are stored in .dat files. 
    The files contain:
        potential.dat: An interpolation of the provided potential. The kind and
        shape is controlled by the data within the input file.
        
        energie.dat: The energie eigenvalues of the solution of the schrodinger
        equation. Limited to the lowest eigenvalues. The number of eigenvalues
        can be controlled in line 3 of the input file.
        
        wavefunc.dat: The first column contains the linear spaced x-axis data
        That can be controlled in line 2 of the input file. The other columns 
        each contain a normalized wavefunction solving the schrodinger equation. 
        The wavefunctions and the number of wavefunctions correspond to the 
        eigenvalues in energie.dat. 
        
        expvalues.dat: The first column contains the expvalues of the position
        operator describing a quantum mechanical particel of mass m (line 1) for 
        the different energie eigenvalues. The second column contains the 
        uncertainty of the expvalue.
        
    Plot Output:
        The plot created by the package contains the results of the .dat files
        The plot is divided into two subplots the left one contains the
        energie eigenvalues, the wavefunctions, the interpolated potential and 
        the expvalues of the position operator. The right subplot contains the
        energie eigenvalues and the uncertainty of the expvalues. The limits of
        the plot are meant to scale to the eigenvalues, the x limit of the
        potential and the uncertaintys. 
        
    All outputs are stored in the same directory as the input file.  
    
    
Moduls:
The main skript of this package is executesolver.py it can be found inside the 
main directory "schrodingersolver/" and can be executed as described. It contains
several functions defined inside different moduls which can be found inside the
directory "moduls/".
A more detailed description can be found inside the .py files of the moduls.
Inputs and outputs are simplified
    
    filemanger.py:
        read_schrodinger(inputpath):
            reads in the input file 
            returns: inputvalues
        filesaver(results):
            saves the results as .dat files
    interpolation.py:
        interpolation(inputvalues):
            interpolates the potential using different methods depending on the
            input.
            returns(potential_data)
    solver.py:
        solver(potential_data, inputvalues):
            calculates the energie eigenvalues and the wavefunctions from the
            input
            returns energies wavefunctions
        calculate_expvalues(wavefunctions, potential_data):
            calculates the expvalues ant the uncertainty from the wavefunc and
            the potential_data
            returns: expvalues and uncertainty
    graphicsplotter.py:
        plotting(results):
            creates a plot from the results and saves it as plot.png
    
    
Tests: 
The package contains a number of unit tests to check reliability after the 
installation.

    Test description: The tests can be found in the directory "tests/" inside 
    the "schrodingersolver/" directory. The directory contains 3 test moduls 
    for the testing of the corresponding modul.
    The tests can be run by typing:
    "python3 -m pytest"
    Into the console of the main directory. 
    
    Test_data: For the execution of the tests referenz data was needed for
    comparison. The data was provided by a group who developt a similar project
    in the year 2020. Their project can be found at:
    
    https://github.com/kenokrieger/QmPy
    
    Test moduls: test_filemanager is testing the read_schrodinger function of the
    filemanger. test_interpolation is testing the shape of the interpolation output
    for different npoints and the interpolation for an easy example. test_solver
    is testing the solver function and compares energie eigenvalues, expavalues 
    and uncertaintys to the values of the "test_data/" directory.
    
    
Credits:
Provided test data:
    Keno Krieger: https://github.com/kenokrieger
    Helmut Wecke:
    






