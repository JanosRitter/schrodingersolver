"""Tests for the private _interpolation module"""
import numpy as np
import pytest
from moduls.interpolation import interpolation

points = [5, 10, 100, 1000, 5000, 10000]
ipoldeclarations = np.array([[0,-5], [7,3], [25,25], [100,-5.5], [150,10]])



@pytest.mark.parametrize('npoints', points)
def test_shape_linear(npoints):
    """Tests whether computed arrays have the correct shape (linear)"""
    xdata = (0, 150, npoints)
    potential_data = interpolation(ipoldeclarations, xdata, interpoltype='linear')

    assert potential_data[:,0].shape[0] == npoints and potential_data[:,0].shape[0] == npoints

@pytest.mark.parametrize('npoints', points)
def test_shape_cspline(npoints):
    """Tests whether computed arrays have the correct shape (cspline)"""
    xdata = (0, 150, npoints)
    potential_data = interpolation(ipoldeclarations, xdata, interpoltype='cspline')

    assert potential_data[:,0].shape[0] == npoints and potential_data[:,0].shape[0] == npoints

@pytest.mark.parametrize('npoints', points)
def test_shape_polynomial(npoints):
    """Tests whether computed arrays have the correct shape (polynomial)"""
    xdata = (0, 150, npoints)
    potential_data = interpolation(ipoldeclarations, xdata, interpoltype='polynomial')

    assert potential_data[:,0].shape[0] == npoints and potential_data[:,0].shape[0] == npoints

@pytest.mark.parametrize('npoints', points)
def test_potential(npoints):
    """Tests whether computed arrays have the correct shape (invalid)
    by default cspline will be used"""
    xdata = (0, 150, npoints)
    potential_data = interpolation(ipoldeclarations, xdata, interpoltype='invalid')

    assert potential_data[:,0].shape[0] == npoints and potential_data[:,0].shape[0] == npoints


def test_ifpivots():
    """Tests whether the interpolation goes through all pivots"""
    interpoldeclarations = np.array([[-4,4], [0,0], [4,4]])
    expected_results = np.array([[-4,4], [-3,3], [-2,2], [-1,1], [0,0], [1,1], [2,2], [3,3], [4,4]])


    xdata = (-4, 4, 9)
    potential_data = interpolation(interpoldeclarations, xdata, interpoltype='linear')

    assert np.all(potential_data == expected_results)
