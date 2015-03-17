"""
Methods that are constrained to the generation of
images.
"""

import numpy as np


def gen_saddle():
  r, c = np.meshgrid(np.arange(-75, 75), np.arange(-100, 100), indexing='ij')
  f = r * c
  return normalize(f)


def gen_ramp(h, w, orientation='h'):
  # v, h = np.indices((h,w))
  v, h = np.meshgrid(np.arange(h), np.arange(w), indexing='ij')

  return normalize((v, h)[orientation == 'h'])


def gen_X(size=200):
  r, c = np.indices((size, size))
  f = (r == ((size - 1) - c))
  g = (c == r)

  return f + g


def gen_X2(size=200):
  return np.identity(size)[:, ::-1] + np.identity(size)
