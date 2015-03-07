"""
Remember:

- unidimensional:
  - array[initial:final:step]
  - default:
    - initial: 0
    - final: len(array)
    - step: 1
    - [:]: all the elements in the given dimension

- multidimensional:
  - array[1,:] - line 1
  - array[:, 1] - column 1


"""

import numpy as np

def invert(a):
  return a[::-1]

def get_odd(a):
  return a[1::2]

def main():
  a = np.arange(20)
  print 'invert(a): \n', invert(a)
  print 'get_odd(a): \n', get_odd(a)

  b = a.reshape(4,5)
  print 'b: \n', b
  print 'primeira linha\n', b[0,:]
  print 'linhas duas a duas \n',b[::2,:]
  print 'colunas, duas a duas \n', b[:, ::2]
  print 'duas ultimas linhas, reversas:\n' , b[-3:-1:, ::-1]

if __name__ == '__main__':
  main()
