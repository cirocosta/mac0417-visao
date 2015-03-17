"""
Basic funcionalitty shared all over the code
"""

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

def crop_binary(f):
  r, c = f.nonzero()
  return f[r[0]:r[-1]+1, c.min():c.max()+1]

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
  # retrieve histogram data and also bins
  hist, bins = np.histogram(img.flatten(), 256, normed=True)
  cdf = hist.cumsum()
  cdf = 255 * cdf / cdf[-1]
  new_img = np.interp(img.flatten(), bins[:-1], cdf).reshape(img.shape)

  return new_img.reshape(img.shape)


def f(t):
  return np.exp(-t) * np.cos(2*np.pi*t)

def main():
  t1 = np.arange(0.0, 5.0, 0.1)
  t2 = np.arange(0.0, 5.0, 0.02)

  plt.figure(1)
  plt.subplot(311)
  plt.plot(t1, f(t1), 'bo', t2, f(t2), 'r')

  plt.subplot(312)
  plt.plot(t2, np.cos(2*np.pi*t2), 'r--')

  plt.subplot(313)
  mu, sigma = 100, 15
  x = mu + sigma * np.random.randn(10000)

  hist, bins, patches = plt.hist(x, 100, normed=1, facecolor='g', alpha=0.75)

  plt.plot(x, np.cumsum(hist), 'r')

  plt.xlabel('Smarts')
  plt.ylabel('Probability')
  plt.title('Histogram of IQ')
  plt.text(60, .025, r'$x^2 + y^2 = r^2$')

  plt.show()


if __name__ == '__main__':
  main()
