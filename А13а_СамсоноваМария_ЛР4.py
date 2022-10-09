from pyglet.gl import *
import pyglet
from pyglet import app, graphics
from pyglet.window import Window, key
import numpy as np

n_rot = 0
rot = 1

w = 1.5 * 20
width, height = int(30 * w), int(30 * w)
window = Window(visible = True, width = width, height = height, resizable = True)
glClearColor(0.4, 0.4, 0.4, 1.0)
glClear(GL_COLOR_BUFFER_BIT)
def texInit():
    fn = 'Cat1.jpg'
    img = pyglet.image.load(fn)
    iWidth = img.width
    iHeight = img.height
    img = img.get_data('RGBA', iWidth * 4)

    p, r = GL_TEXTURE_2D, GL_RGBA
    glTexParameterf(p, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(p, GL_TEXTURE_WRAP_T, GL_REPEAT)

    glTexParameterf(p, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(p, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    glTexImage2D(p, 0, r, iWidth, iHeight, 0, r, GL_UNSIGNED_BYTE, img)
    glEnable(p)

gl.glEnable(gl.GL_DEPTH_TEST)
gl.glDepthFunc(gl.GL_LESS)
texInit()

def c_float_Array(data): # Преобразование в си-массив
    return (gl.GLfloat * len(data))(*data)

a=10
b=20
v0, v1, v2, v3 = (0,0,0), (0,b,0), (a,b,0), (a,0,0)

v0_, v1_, v2_, v3_ = (0,0,0.01), (0,b,0.01), (a,b,0.01), (a,0,0.01)
v0__, v1__, v2__, v3__ = (0,0,-0.01), (0,b,-0.01), (a,b,-0.01), (a,0,-0.01)

c=(1,0,0)
tc=0.5

mtClr = c_float_Array([1, 0, 0, 0])

def draw1(dt1):
    global tc
    t1,t2,t3,t4=(0, 0), (0, tc), (tc, tc), (tc, 0)

    graphics.draw(4, GL_QUADS, ('v3f', (v0 + v1 + v2 + v3)), ('t2f', t1+t2+t3+t4))

def draw2(dt2):
    global tc
    t1, t2, t3, t4 = (0, 0), (0, tc), (tc, tc), (tc, 0)

    gl.glPushMatrix()
    gl.glRotatef(95.0, 0.0, 1.0, 0.0)
    graphics.draw(4, GL_QUADS, ('v3f', (v0 + v1 + v2 + v3)),  ('t2f', t1+t2+t3+t4))
    gl.glPopMatrix()

def draw3(dt3):
    global tc
    t1,t2,t3,t4=(0, 0), (0, tc), (tc, tc), (tc, 0)

    graphics.draw(4, GL_QUADS, ('v3f', (v0__ + v1__ + v2__ + v3__)), ('c3f', (c + c + c + c)) )

def draw4(dt4):
    global tc
    t1, t2, t3, t4 = (0, 0), (0, tc), (tc, tc), (tc, 0)

    gl.glPushMatrix()
    gl.glRotatef(95.0, 0.0, 1.0, 0.0)
    graphics.draw(4, GL_QUADS, ('v3f', (v0_ + v1_ + v2_ + v3_)), ('c3f', (c + c + c + c)))
    gl.glPopMatrix()

@window.event
def on_draw():
    global n_rot,rot,tc
    window.clear()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gl.glRotatef(60.0, 1.0, 0.0, 0.0)
    gl.glRotatef(-45.0, 0.0, 1.0, 0.0)
    glOrtho(-w, w, -w, w, -w, w)

    gl.glMatrixMode(gl.GL_MODELVIEW)



    if n_rot > 360:
        n_rot = 0
        rot = 1

    if n_rot > 180:
        tc -= 0.01
    else:
        tc += 0.01

    n_rot += 1

    gl.glRotatef(rot, 0, 1, 0)
    pyglet.clock.tick()

pyglet.clock.schedule(draw1)
pyglet.clock.schedule(draw2)
pyglet.clock.schedule(draw3)
pyglet.clock.schedule(draw4)
app.run()