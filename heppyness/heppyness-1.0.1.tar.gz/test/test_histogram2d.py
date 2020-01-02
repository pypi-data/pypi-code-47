# Auxiliary modules
from os.path import join, dirname
import numpy as np
from copy import deepcopy
import sys

# Module to be tested
sys.path.append(join(dirname(__file__), '..'))
import heppy



#
# Set up
#
_areas = np.array([
	[1., 5.],
	[2., 6.],
	[3., 7.],
	])
_binedges_x = np.array([-7., 0., 5., 50.])
_binedges_y = np.array([-1., 0., 1.])
_binedges = (_binedges_x, _binedges_y)
_binsizes = np.array([
	[7.,  7. ],
	[5.,  5. ],
	[45., 45.],
	])
_corr_variations = {
	'corr__1up' : _areas * 1.2,
	'corr__1down' : _areas * 0.8,
}
_uncorr_variations = {
	'uncorr__1up' : _areas * 1.3,
	'uncorr__1down' : _areas * 0.7,
}
_h = heppy.histogram2d(_binedges, _areas, areas=True, corr_variations=_corr_variations, uncorr_variations=_uncorr_variations)





def test_calculate_bin_sizes():
	'''
	Test free function used for calculating bin sizes, in the case of a 2D histogram
	'''
	from heppy.histogram import _calculate_bin_sizes
	binsizes = _calculate_bin_sizes(_binedges)
	assert binsizes.shape == (3, 2)
	np.testing.assert_array_almost_equal( binsizes, _binsizes )



def test_binareas():
	'''
	Test computing bin areas of a 2D histogram
	'''
	binsizes = _h.binsizes
	assert binsizes.shape == (3, 2)
	np.testing.assert_array_almost_equal( binsizes, _binsizes )



def test_areas():
	'''
	Test retrieving areas of a 2D histogram
	'''
	areas = _h.areas
	assert areas.shape == (3, 2)
	np.testing.assert_array_almost_equal( areas, _areas )



def test_corr_variations():
	'''
	Test retrieving correlated variations (areas)
	'''
	np.testing.assert_array_almost_equal( _h.corr_variations['corr__1up'], _areas * 1.2 )
	np.testing.assert_array_almost_equal( _h.corr_variations['corr__1down'], _areas * 0.8 )



def test_uncorr_variations():
	'''
	Test retrieving uncorrelated variations (areas)
	'''
	np.testing.assert_array_almost_equal( _h.uncorr_variations['uncorr__1up'], _areas * 1.3 )
	np.testing.assert_array_almost_equal( _h.uncorr_variations['uncorr__1down'], _areas * 0.7 )



def test_heights():
	'''
	Test retrieving heights of a 2D histogram
	'''
	heights = _h.heights
	assert heights.shape == (3, 2)
	np.testing.assert_array_almost_equal( heights, _areas/_binsizes )



def test_nbins():
	'''
	Test retrieving the numbers of bins of a 2D histogram
	'''
	nbins = _h.nbins
	assert nbins == (3, 2)



def test_points():
	'''
	Test making the point representation of a 2D histogram
	'''
	midx, midy, heights = _h.points()
	assert midx.shape == midy.shape
	assert midx.shape == heights.shape
	np.testing.assert_array_almost_equal( midx, np.array([-3.5, -3.5, 2.5, 2.5, 27.5, 27.5]) )
	np.testing.assert_array_almost_equal( midy, np.array([-0.5, 0.5, -0.5, 0.5, -0.5, 0.5]) )
	np.testing.assert_array_almost_equal( heights, np.ravel(_areas/_binsizes) )



def test_rebin():
	'''
	Test rebinning of 2D histogram (including corr. and uncorr. variations)
	'''
	newedges_x = np.array([-7., 5., 50.])
	newedges_y = np.array([-1., 1.])
	newedges = (newedges_x, newedges_y)
	h = deepcopy(_h)
	h.rebin(newedges)
	assert isinstance(h.binedges, tuple)
	assert h.binsizes.shape == (2, 1)
	np.testing.assert_array_almost_equal(h.binedges[0], newedges_x)
	np.testing.assert_array_almost_equal(h.binedges[1], newedges_y)
	np.testing.assert_array_almost_equal(h.areas, np.array([[14.], [10.]]))
	np.testing.assert_array_almost_equal(h.corr_variations['corr__1up'], np.array([[14.], [10.]]) * 1.2 )
	np.testing.assert_array_almost_equal(h.corr_variations['corr__1down'], np.array([[14.], [10.]]) * 0.8 )
	np.testing.assert_array_almost_equal(h.uncorr_variations['uncorr__1up'], np.array([[14. + np.sqrt(0.09 + 2.25 + 0.36 + 3.24)], [10. + np.sqrt(0.81 + 4.41)]]) )
	np.testing.assert_array_almost_equal(h.uncorr_variations['uncorr__1down'], np.array([[14. - np.sqrt(0.09 + 2.25 + 0.36 + 3.24)], [10. - np.sqrt(0.81 + 4.41)]]) )



def test_project_x():
	'''
	Test projecting a 2D histogram (including corr. and uncorr. variations) onto the x-axis
	'''
	h = _h.project('x', name='x projection')
	assert isinstance(h, heppy.histogram1d)
	assert h.name == 'x projection'
	np.testing.assert_array_almost_equal(h.binedges, _binedges_x)
	np.testing.assert_array_almost_equal(h.areas, [6., 8., 10.])
	np.testing.assert_array_almost_equal(h.corr_variations['corr__1up'], np.array([6., 8., 10.]) * 1.2 )
	np.testing.assert_array_almost_equal(h.corr_variations['corr__1down'], np.array([6., 8., 10.]) * 0.8 )
	np.testing.assert_array_almost_equal(h.uncorr_variations['uncorr__1up'], np.array([6. + np.sqrt(0.09 + 2.25), 8. + np.sqrt(0.36 + 3.24), 10. + np.sqrt(0.81 + 4.41)]) )
	np.testing.assert_array_almost_equal(h.uncorr_variations['uncorr__1down'], np.array([6. - np.sqrt(0.09 + 2.25), 8. - np.sqrt(0.36 + 3.24), 10. - np.sqrt(0.81 + 4.41)]) )




def test_project_y():
	'''
	Test projecting a 2D histogram (including corr. and uncorr. variations) onto the y-axis
	'''
	h = _h.project('y', name='y projection')
	assert isinstance(h, heppy.histogram1d)
	assert h.name == 'y projection'
	np.testing.assert_array_almost_equal(h.binedges, _binedges_y)
	np.testing.assert_array_almost_equal(h.areas, [6., 18.])
	np.testing.assert_array_almost_equal(h.corr_variations['corr__1up'], np.array([6., 18.]) * 1.2 )
	np.testing.assert_array_almost_equal(h.corr_variations['corr__1down'], np.array([6., 18.]) * 0.8 )
	np.testing.assert_array_almost_equal(h.uncorr_variations['uncorr__1up'], np.array([6. + np.sqrt(0.09 + 0.36 + 0.81), 18. + np.sqrt(2.25 + 3.24 + 4.41)]) )
	np.testing.assert_array_almost_equal(h.uncorr_variations['uncorr__1down'], np.array([6. - np.sqrt(0.09 + 0.36 + 0.81), 18. - np.sqrt(2.25 + 3.24 + 4.41)]) )
