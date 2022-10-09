import random
import numpy as np
from pyglet.gl import *
from pyglet.window import Window
from pyglet import app

w=600

n=100000 #кол-во точек
CIF1=[-0.5, -0.43, 0.43, -0.5, 0.0, 0.00, 0.55]
CIF2=[-0.5, 0.43, -0.43, -0.5, 1.5, 0.43, 0.45]

#нахождение начала
xstart=1000
ystart=1000

for i in range(1000):
    x1 = xstart
    y1 = ystart
    xstart = CIF2[0] * x1 + CIF2[1] * y1 + CIF2[4]
    ystart = CIF2[2] * x1 + CIF2[3] * y1 + CIF2[5]

xstart=round(xstart,2)
ystart=round(ystart,2)

print("СТАРТОВАЯ ТОЧКА: ",xstart,ystart)

#нахождения минимума и максимума x и y
x0 = xstart
y0 = ystart

xmax=x0
xmin=x0

ymax=y0
ymin=y0
for i in range(n):
    chance = random.randint(1, 100)
    x1 = x0
    y1 = y0
    if chance <= CIF1[6]*100:
        x0 = CIF1[0] * x1 + CIF1[1] * y1 + CIF1[4]
        y0 = CIF1[2] * x1 + CIF1[3] * y1 + CIF1[5]
    else:
        x0 = CIF2[0] * x1 + CIF2[1] * y1 + CIF2[4]
        y0 = CIF2[2] * x1 + CIF2[3] * y1 + CIF2[5]

    if x0 < xmin:
        xmin = x0
    if x0 > xmax:
        xmax = x0

    if y0 < ymin:
        ymin = y0
    if y0 > ymax:
        ymax = y0

xmax=round(xmax,2)
ymax=round(ymax,2)

xmin=round(xmin,2)
ymin=round(ymin,2)

if ymin>0:
    ymin=0
if xmin>0:
    xmin=0

#создание массива размерности (xmax-xmin)+1 на (ymax-ymin)+1
wx = int((xmax-xmin)*100)
wy = int((ymax-ymin)*100)

print("X: ",wx)
print("Y: ",wy)

vp = np.full((w, w, 3), 255, dtype = 'uint64')

print(wx+1,wy+1)

for i in range(n):
    chance = random.randint(1, 100)
    x1 = xstart
    y1 = ystart
    if chance <= CIF1[6]*100:
        xstart = CIF1[0] * x1 + CIF1[1] * y1 + CIF1[4]
        ystart = CIF1[2] * x1 + CIF1[3] * y1 + CIF1[5]
    else:
        xstart = CIF2[0] * x1 + CIF2[1] * y1 + CIF2[4]
        ystart = CIF2[2] * x1 + CIF2[3] * y1 + CIF2[5]

    vp[int((round(xstart,2)-xmin)*100),int((round(ystart,2)-ymin)*100)] = [0, 0, 0]

vp = vp.flatten()
vp = (GLubyte * ((w) * (w) * 3))(*vp)

window = Window(visible = True, width = w, height = w, caption = 'WOOD')

@window.event
def on_draw():
    window.clear()
    glDrawPixels(w, w, GL_RGB, GL_UNSIGNED_BYTE, vp)
app.run()
