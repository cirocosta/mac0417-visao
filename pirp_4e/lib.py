import numpy as np
import matplotlib.pyplot as plt

from scipy import ndimage


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
  g = f.transpose()
  return g


def four_squares(isImg=False):
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


def normalize(arr, range=(0, 255)):
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


def equalize_histogram(img):
  hist, bins = np.histogram(img.flatten(), 256, normed=True)
  cdf = hist.cumsum()
  cdf = 255 * cdf / cfg[-1]
  new_img = np.interp(img.flatten(), bins[:-1], cdf)

  return new_img.reshape(img.shape), cdf


def main():
  print gen_X2()
  plt.imshow(gen_X2(), cmap="gray")
  plt.show()


if __name__ == '__main__':
  main()
