'''
Constructing rings of polygons
From UKMT MacLaurin Olympiad 2015 Q6
'''

import math

import pygame as py


py.init()


class Polygon:
  def __init__(self, sides, size):
    self.sides = sides
    self.size = size

  def draw(self, x, y, d, chir = 1):
    '''Constructs a polygon at `pos` facing `dir` with chirality `chir`.

    Depending on chirality, this returns either the 2nd point or penultimate point, alongside direction.
    '''

    points = [(x, y)]
    out = None

    for i in range(1, self.sides):
      x += self.size * math.cos(math.radians(d))
      y += self.size * math.sin(math.radians(d))
      d += chir * 360 / self.sides
      points.append((x, y))

      data = (x, y, d)
      if chir == 1:
        if i == 2:
          out = data
      elif chir == -1:
        if i == self.sides - 1:
          out = data

    py.draw.lines(display, (255, 255, 255, 255), closed = True, points = points)

    return out


class Test:
  def __init__(self, x, y, sides, size):
    self.x = x
    self.y = y
    self.d = 90
    self.sides = sides
    self.size = size

  def start(self):
    print("status: next test started")

    self.sides += 1

    self.shape = Polygon(self.sides, self.size)

    self.cx = self.x
    self.cy = self.y
    self.cd = self.d

    py.display.flip()
    display.fill((0, 23, 42))

  def next(self):
    print("exec: next draw")

    data = self.shape.draw(self.cx, self.cy, self.cd)
    self.cx, self.cy, self.cd = data
    py.display.flip()


display = py.display.set_mode((500, 500))
ex = Test(200, 200, 4, 50)

state = True
while state:
  for event in py.event.get():
    if event.type == py.QUIT:
      state = False
      break

    elif event.type == py.KEYDOWN:
      if event.key == py.K_ESCAPE:
        state = False
        break
      elif event.key == py.K_RETURN:
        ex.start()
      elif event.key == py.K_SPACE:
        ex.next()


py.quit()
