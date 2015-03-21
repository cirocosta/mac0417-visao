"""
Methods that are constrained to the generation of
images.
"""

import numpy as np
from lib import normalize


def gen_saddle():
  r, c = np.meshgrid(np.arange(-75, 75), np.arange(-100, 100), indexing='ij')
  f = r * c
  return normalize(f)


def gen_ramp(h, w, orientation='h'):
  v, h = np.meshgrid(np.arange(h), np.arange(w), indexing='ij')
  return normalize((v, h)[orientation == 'h'])


def gen_X(size=200):
  r, c = np.indices((size, size))
  f = (r == ((size - 1) - c))
  g = (c == r)

  return f + g

def gen_X2(size=200):
  return np.identity(size)[:, ::-1] + np.identity(size)

def gen_four_squares(isImg=False):
  H = 300
  W = 600

  if not isImg:
    H /= 50
    W /= 50

  img = np.empty((H, W), "uint8")
  img[:, :W / 2] = 64
  img[:, W / 2:] = 192
  img[H / 3:2 * H / 3, W / 6:2 * W / 6] = 128
  img[H / 3:2 * H / 3, 2 * W / 3:5 * W / 6] = 128

  return img

def gen_color_ramp(f):
  g = np.copy(f)

  r, c = np.meshgrid(np.arange(0, 256, 2), np.arange(20), indexing='ij')
  r[:,0] = r[:,-1] = 255

  h_g, w_g = g.shape
  h_r, w_r = r.shape

  g[20:(h_r + 20), (w_g-40):w_r+(w_g-40)] = r

  return g


def main():
  import matplotlib.pyplot as plt
  from scipy import ndimage

  img = ndimage.imread('../assets/cameraman.tif', flatten=True)

  plt.imshow(gen_color_ramp(img), cmap="gray")
  plt.axis('off')
  plt.show()

if __name__ == '__main__':
  main()
