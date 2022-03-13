"""Internal test for the filemanager.py modul"""
import os.path
import numpy as np
from moduls.filemanager import _read_schrodinger

testdirectory = "tests/test_data"

def test_inf_potwell():
    """Tests the _read_schrodinger function for the infinite potential well"""
    datapath = os.path.join(testdirectory, "inf_potwell.inp")
    mass, x_data, first_ev, last_ev, interpoltype, ipolxydec = _read_schrodinger(datapath)
    expected_interpolxydecs = np.array([[-2.0, 0.0], [2.0, 0.0]])
    assert mass == 2.0
    assert x_data == (-2.0, 2.0, 1999)
    assert first_ev == 1
    assert last_ev == 5
    assert interpoltype == "linear"
    assert np.all(ipolxydec == expected_interpolxydecs)


def test_asym_potwell():
    """Tests the _read_schrodinger function for the asymetric potential well"""
    datapath = os.path.join(testdirectory, "asym_potwell.inp")
    mass, x_axis_data, first_ev, last_ev, interpoltype, interpolxydeclarations = _read_schrodinger(datapath)
    expected_interpolxydecs = np.array([[0.0, 30.0], [1.0, 11.8], [2.0, 1.7],
                                        [3.0, 0.0], [5.0, 0.6], [7.0, 1.6],
                                        [9.0, 2.4], [11.0, 3.0], [13.0, 3.4],
                                        [15.0, 3.6], [19.0, 3.79],
                                        [20.0, 3.8]], dtype=float)
    assert mass == 1.0
    assert x_axis_data == (0.0, 20.0, 1999)
    assert first_ev == 1
    assert last_ev == 7
    assert interpoltype == "cspline"
    assert np.all(interpolxydeclarations == expected_interpolxydecs)


def test_harm_osci():
    """Tests the _read_schrodinger function for the harmonic oscillator's
    potential"""
    datapath = os.path.join(testdirectory, "harm_osci.inp")
    mass, x_axis_data, first_ev, last_ev, interpoltype, interpolxydeclarations = _read_schrodinger(datapath)
    expected_interpolxydecs = np.array([[-1.0, 0.5], [0.0, 0.0], [1.0, 0.5]],
                                       dtype=float)
    assert mass == 4
    assert x_axis_data == (-5.0, 5.0, 1999)
    assert first_ev == 1
    assert last_ev == 5
    assert interpoltype == "polynomial"
    assert np.all(interpolxydeclarations == expected_interpolxydecs)
