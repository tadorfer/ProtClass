import pytest
import numpy as np
from .. import length
import pkg_resources

PATH = pkg_resources.resource_filename(__name__, 'test_data/')

def test_lengths():
    "Test sequence lengths"
    
    # load data
    X_str = 'AYTLG'
    X_list = open(PATH+'multiple.txt').read().splitlines()
    X_err = 'AGT2HT9'
    
    # test integer lengths
    len_single = length(X_str, 'int')
    len_int = length(X_list, 'int')
    assert np.array_equal(len_int, np.array([7,9,8]))
    
    # test one-hot-encoded lengths
    len_ohe = length(X_list, 'ohe')
    # columns: [6, 7, 9]
    assert np.array_equal(len_ohe, np.array([[1., 0., 0.],
                                             [0., 0., 1.],
                                             [0., 1., 0.]]))
    
    # test ValueError
    with pytest.raises(ValueError):
        len_err = length(X_err)