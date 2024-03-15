'''
Heatrace
Tracing random walks with heatmaps
March 2024
'''

import random as ran

import numpy as np
import matplotlib.pyplot as plt


class Walker:
  def __init__(self, shard):
    self.shard = shard
    self.x = 0
    self.y = 0
    self.trace = {(0, 0): 1}

  def step(self):
    if ran.randint(0, 1):
      self.x += 1 if ran.randint(0, 1) else -1
    else:
      self.y += 1 if ran.randint(0, 1) else -1
    
    self.trace[(self.x, self.y)] = self.trace.get((self.x, self.y), 0) + 1

  def export(self) -> np.ndarray:
    lx = 0
    ly = 0
    tx = 0
    ty = 0

    for each in self.trace.keys():
      if each[0] < lx:
        lx = each[0]
      if each[0] > tx:
        tx = each[0]

      if each[1] < ly:
        ly = each[1]
      if each[1] > ty:
        ty = each[1]

    data = np.zeros(
      shape = (
        tx - lx + 1,
        ty - ly + 1),
      dtype = int,
    )

    for key, val in self.trace.items():
      data[key[0] + abs(lx), key[1] + abs(ly)] = val

    return data

  def walk(self, count) -> np.ndarray:
    for i in range(count):
      self.step()

    return self.export()


if __name__ == "__main__":
  print("STATUS: RUNNING!")

  plt.set_cmap(plt.viridis())

  walker = Walker("sup")
  data = walker.walk(6942069)

  fig, ax = plt.subplots()
  fig.set_size_inches((42, 42))
  im = ax.imshow(data)

  plt.savefig("renders/heatrace.png")
  print("STATUS: DONE!")
