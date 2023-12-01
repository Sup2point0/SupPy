'''
Walking the Worlds by Distance
'''

import sys
import random as ran
import copy

import pygame as py


class World:
  def __init__(self,
    i: int,
    x: float = None,
    y: float = None,
  ):
    self.i = i
    self.x = x or ran.uniform(-1, 1)
    self.y = y or ran.uniform(-1, 1)


class WorldWalker(py.sprite.Sprite):
  def __init__(self, cx, cy):
    super().__init__()

    self.cx = cx
    self.cy = cy
    self.points = []
    self.trace = []

  def splash(self, points):
    self.points = [World(i) for i in range(points)]

  def trace(self, start = 0):
    self.trace = []
    self.ahead = copy.copy(self.points)
    point = self.ahead[start]
    
    for i in range(1, self.points):
      dist = float("inf")
      dest = None

      for idx, each in enumerate(self.ahead):
        dx = each.x - point.x
        dy = each.y - point.y

        if dx ** 2 + dy ** 2 < dist:
          dest = World(idx, each.x, each.y)

      self.ahead.pop(dest.i)
      self.trace.append((dest.x, dest.y))

  def render(self, surf: py.Surface):
    py.draw.lines(surf,
      col = (255, 255, 255, 128),
      closed = False,
      points = self.trace
    )


if __name__ == "__main__":
  py.init()

  screen = py.display.init()
  world = WorldWalker(200, 200)

  while True:
    for event in py.event.get():
      if event.type == py.QUIT:
        py.quit()

      elif event.type == py.KEYDOWN:
        if event.key == py.K_SPACE:
          world.trace()
        elif event.key == py.K_RETURN:
          world.splash()

    py.display.flip()
    py.display.fill((0, 0, 0))
    world.render(display)

  sys.exit()
