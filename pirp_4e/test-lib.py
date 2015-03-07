import numpy as np
import unittest
import lib as lib


class LibTest(unittest.TestCase):

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_add_grid(self):
    img = np.zeros(25).reshape(5, 5)
    actual = lib.add_grid(img, 4)
    expected = np.array([
        [255, 255, 255, 255, 255],
        [255, 0, 0, 0, 255],
        [255, 0, 0, 0, 255],
        [255, 0, 0, 0, 255],
        [255, 255, 255, 255, 255],
    ])

    np.testing.assert_array_equal(actual, expected)

  def test_add_grid_2(self):
    img = np.zeros(25).reshape(5, 5)
    actual = lib.add_grid(img, 2)
    expected = np.array([
        [255, 255, 255, 255, 255],
        [255, 0, 255, 0, 255],
        [255, 255, 255, 255, 255],
        [255, 0, 255, 0, 255],
        [255, 255, 255, 255, 255],
    ])

    np.testing.assert_array_equal(actual, expected)

  def test_add_inner_border(self):
    img = np.zeros(25).reshape(5, 5)
    actual = lib.add_inner_border(img, 1)
    expected = np.array([
        [255, 255, 255, 255, 255],
        [255, 0, 0, 0, 255],
        [255, 0, 0, 0, 255],
        [255, 0, 0, 0, 255],
        [255, 255, 255, 255, 255],
    ])

    np.testing.assert_array_equal(actual, expected)

  def test_add_inner_border_2(self):
    img = np.zeros(25).reshape(5, 5)
    actual = lib.add_inner_border(img, 2)
    expected = np.array([
        [255, 255, 255, 255, 255],
        [255, 255, 255, 255, 255],
        [255, 255, 0, 255, 255],
        [255, 255, 255, 255, 255],
        [255, 255, 255, 255, 255],
    ])

    np.testing.assert_array_equal(actual, expected)


if __name__ == '__main__':
  unittest.main()
