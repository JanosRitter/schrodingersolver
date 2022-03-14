"""Contains tests for the private _solvers module"""
from numpy import insert, loadtxt, allclose
import pytest
from moduls.filemanager import _read_schrodinger
from moduls.interpolation import interpolation
from moduls.solver import solver, calculate_expvalues


problems = ['inf_potwell', 'fin_potwell', 'double_well', 'asym_potwell',
            'harm_osci']


@pytest.mark.parametrize('sampleinput', problems)
def test_energies(sampleinput):
    """
    Tests whether the computed wavefunctions and energies match the
    reference data.

    """
    input_path = 'tests/test_data/{}.inp'.format(sampleinput)
    mass, xdata, first_ev, last_ev, ipoltype, ipoldeclarations = _read_schrodinger(input_path)

    potential_data = interpolation(ipoldeclarations, xdata, interpoltype = ipoltype)

    
    cal_energies, cal_wavefuncs, ignore = solver(mass, potential_data, first_ev, last_ev)

    
    ref_energies = loadtxt('tests/test_data/energies_{}.ref'.format(sampleinput))
    

    assert allclose(ref_energies, cal_energies, atol = 0.0001)
    
    
    
@pytest.mark.parametrize('sampleinput', problems)
def test_wavefunc(sampleinput):
    """
    Tests whether the computed wavefunctions and energies match the
    reference data.

    """
    input_path = 'tests/test_data/{}.inp'.format(sampleinput)
    mass, xdata, first_ev, last_ev, ipoltype, ipoldeclarations = _read_schrodinger(input_path)

    potential_data = interpolation(ipoldeclarations, xdata, interpoltype = ipoltype)

    
    cal_energies, cal_wavefuncs, cal_wf_slice = solver(mass, potential_data, first_ev, last_ev)
    
    cal_expvalues = calculate_expvalues(potential_data, cal_wf_slice)


    
    #ref_energies = loadtxt('tests/test_data/energies_{}.ref'.format(sampleinput))
    ref_wavefuncs = loadtxt('tests/test_data/wfuncs_{}.ref'.format(sampleinput))
    ref_wf_slice = ref_wavefuncs[:,1:]
    
    ref_expvalues = calculate_expvalues(potential_data, ref_wf_slice)

    #assert allclose(ref_energies, cal_energies, atol = 0.01)
    assert allclose(ref_expvalues[:,0], cal_expvalues[:,0], atol = 0.001)

