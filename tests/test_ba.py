import unittest
import os
import numpy as np
import bz2
import pycalib
import time
from scipy.optimize import least_squares

class TestPyCalibBa(unittest.TestCase):
    BAL_FILENAME = 'problem-49-7776-pre.txt.bz2'
    BAL_URL = 'https://grail.cs.washington.edu/projects/bal/data/ladybug/problem-49-7776-pre.txt.bz2'

    def test_bal(self):
        if not os.path.isfile(self.BAL_FILENAME):
            urllib.request.urlretrieve(self.BAL_URL, self.BAL_FILENAME)

        with bz2.open(self.BAL_FILENAME) as fp:
            camera_params, points_3d, camera_indices, point_indices, points_2d = pycalib.bal.bal_load_numpy(fp)
        camera_params, mask = pycalib.bal.bal_cam9_to_cam14(camera_params)

        # allow p1, p2, k3
        mask[12:] = True

        print(mask)

        ret = pycalib.ba.bundle_adjustment(camera_params, points_3d, camera_indices, point_indices, points_2d, mask=mask)
        print(ret)

if __name__ == '__main__':
    unittest.main()
