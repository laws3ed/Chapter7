from chapter7.pycode import convertToList
import numpy as np


def test_convertToList():
    arr = np.array([1, 2, 4, 5])
    arr_list = convertToList(arr)
    assert 4 in arr_list
