"""
Basic funcionalitty shared all over the code
"""

import math
import numpy as np


def add_grid(f, delta, color=255):
  g = np.copy(f)
  g[::delta, :] = color
  g[:, ::delta] = color

  return g


def add_inner_border(f, size, color=255):
  if not size:
    return g

  g = np.copy(f)
  g[:size, :] = color
  g[-size:, :] = color
  g[:, :size] = color
  g[:, -size:] = color

  return g


def rotate_90(f):
  return f.transpose()


def crop_binary(f):
  r, c = f.nonzero()
  return f[r[0]:r[-1] + 1, c.min():c.max() + 1]


def gamma_correction(f, gamma):
  g = np.copy(f)
  t_gamma = normalize(np.arange(256) ** gamma)

  return t_gamma[g]


def naive_percentile(arr, p):
  """
  Gives the value below which a given percentage
  of sorted observations fall.
  """
  return np.ceil(len(arr) * p / 100.0)


def normalize(arr, range=(0, 255), percentile=1):
  """
  Based on minimum and maximimum values, performs
  a linear interpolation of the values.
  """
  arr = np.asarray(arr)
  faux = np.ravel(arr).astype(float)
  min_val = faux.min()
  max_val = faux.max()
  lower, upper = range

  if upper == lower:
    g = np.ones(faux.shape) * max_val
  if max_val == min_val:
    g = np.ones(faux.shape) * (upper + lower) / 2.0
  else:
    g = (faux - min_val) * (upper - lower) / (max_val - min_val) + lower

  g = g.reshape(arr.shape).astype(arr.dtype)

  return g


def normalize_with_clip(f, p):
  p1, p2 = np.percentile(f, [p, 100 - p])
  f = np.clip(f, p1, p2)

  return normalize(f)

def scale(val):
  return np.array([
    [val,0,0],
    [0,val,0],
    [0,0,1]]
  )

def rotate(theta):
  return np.array([
    [math.cos(theta),-math.sin(theta),0],
    [math.sin(theta),math.cos(theta),0],
    [0,0,1]
  ])

def translate(x,y):
  return np.array([
    [1,0,x],
    [0,1,y],
    [0,0,1]
  ])

def affine(f, T):
  """Applies the affine transformation on a given
  image.

  ' g(r, c) = f(T^{-1}(r,c)) '

  Direct mapping:
    From image (f) map the values to image (g)
    - g(T(r,c)) = f((r,c)) ,
                  (r,c) in [0,H-1]x[0, W-1]
    - con: T(r,c) might not fill every pixel of G

  Indirect Mapping
    From image (g) search the values in image (f)
    - g(r', c') = f(T^{-1}(r', c')) ,
                  (r', c') in [0, H'-1]x[0, W'-1]
    - pro: every pixel of (g) receives a value
  """
  h, w = f.shape
  y1, x1 = np.indices(f.shape)
  g = np.lib.pad(f, 1, 'constant', constant_values=0)

  yx1 = np.array([
    y1.ravel(), x1.ravel(), np.ones(np.product(f.shape))
  ])

  yx_float = np.dot(np.linalg.inv(T), yx1)
  yy = np.rint(yx_float[0]).astype(int)+1
  xx = np.rint(yx_float[1]).astype(int)+1

  y = np.clip(yy, 0, h+1)
  x = np.clip(xx, 0, w+1)

  return g[y, x].reshape(h, w)


def equalize_histogram(img):
  """
  T(r) = (L-1)/n * (\sum\limits_{i=0}^{r},h(i)),
  where h(i) = hist(i).
  """
  # np.bincount() returns an array that, contains
  # the number of occurences of each integer I,
  # indexed by the array returned, i.e, out
  # 'absolute' histogram (divide it by N and then
  # we have a relative)
  bins = np.bincount(img.ravel())
  n = img.size
  T = 255 / n * np.cumsum(bins)
  T = T.astype(uint8)

  return T[img]


def f(t):
  return np.exp(-t) * np.cos(2 * np.pi * t)


def main():
  import matplotlib.pyplot as plt
  from scipy import ndimage

  # img = ndimage.imread('../assets/cameraman.tif', flatten=True)
  # img = img.astype(np.uint8)

  # new_img = affine(img, translate(2,0))

  # plt.imshow(new_img, cmap="gray")
  # plt.show()

  img = np.arange(12).reshape((3,4))
  print img
  print affine(img, translate(1,0))

if __name__ == '__main__':
  main()
