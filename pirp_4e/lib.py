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
  SIZE = 100

  if not isImg:
    H /= 50
    W /= 50
    SIZE /= 50

  img = np.zeros((H,W))
  img[:,:W/2] = 64
  img[:, W/2:] = 192
  img[H/2-SIZE/2:H/2+SIZE/2, H/2-SIZE/2:H/2+SIZE/2] = 128
  img[H/2-SIZE/2:H/2+SIZE/2, W/2+H/2-SIZE/2:W/2+H/2+SIZE/2] = 128

  return img


def main():
  # img = ndimage.imread('../assets/lena.png', flatten=True)
  # new_img = add_grid(img, 20)

  new_img = four_squares()
  print new_img

  plt.imshow(new_img, cmap=plt.get_cmap('gray'))
  plt.axis('off')
  plt.show()


if __name__ == '__main__':
  main()
