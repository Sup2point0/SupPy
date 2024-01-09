'''
Recursively finding the determinant of a square matrix
'''

import random


def rand(n: int) -> list:
  return [random.randint(0, 20) for i in range(n)]

def sign(n: int) -> int:
  return 1 - 2 * (n % 2)


def part(seq, i):
  return seq[:i] + seq[i+1:]

def crop(trix, col, row):
  return [part(each, col) for each in part(trix, row)]

def score(seq) -> int:
  '''
  sc = 0
  for each in seq:
    if each == 0:
      sc += 3
    elif each == 1:
      sc += 1

  return sc


def det(trix) -> int:
  if len(trix) == 1:
    return trix[0][0]

  # find ideal row to choose
  row, apex = 0, 0
  for i, r in enumerate(trix):
    sc = score(r)
    if sc > apex:
      row, apex = i, sc

  return sum((each
    * sign(row)
    * sign(col)
    * det(crop(trix, col, row))
  ) for col, each in enumerate(trix[row]))
    

# generate a random matrix
d = 4
X = [rand(d) for i in range(d)]

print("det[\n", "\n".join(str(row) for row in X), "\n] =", det(X))
