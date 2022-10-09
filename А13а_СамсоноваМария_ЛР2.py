import math
import pyglet
from pyglet import app, gl, graphics
from pyglet.window import Window, key
d = 20
d2 = 20
w = 1.5 * d # Параметры области визуализации
px = py = 0
width, height = int(20 * w), int(20 * w) # Размеры окна вывода
window = Window(visible = True, width = width, height = height,
                resizable = True, caption = 'Эмблема')

gl.glClearColor(0.1, 0.1, 0.1, 1.0)
gl.glClear(gl.GL_COLOR_BUFFER_BIT)

@window.event
def on_draw():
    window.clear()
    gl.glMatrixMode(gl.GL_MODELVIEW)
    gl.glLoadIdentity()
    gl.glRotatef(180 * px, 1, 0, 0)  # Поворот вокруг оси X
    gl.glRotatef(180 * py, 0, 1, 0)  # Поворот вокруг оси Y

    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    gl.glOrtho(-w, w, -w, w, -1, 1)

    # построение круга с помощью полигона на двух сторонах
    gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)
    n=60
    r=20
    z=0

    gl.glBegin(gl.GL_POLYGON)
    for i in range(n+1):
        x=r*math.cos((2*math.pi*i)/n)
        y=r*math.sin((2*math.pi*i)/n)
        z+=1/n
        gl.glColor3f(x/r, y/r, z)
        gl.glVertex2f(x, y)
    gl.glEnd()

    # построение ребер прямоугольника на лицевой
    # построние вершин прямоугольника на нелицевой
    gl.glPolygonMode(gl.GL_FRONT, gl.GL_LINE)
    gl.glPolygonMode(gl.GL_BACK, gl.GL_POINT)
    gl.glLineWidth(5)
    gl.glPointSize(1)

    pattern = '0b1111111111111111'
    gl.glLineStipple(2, int(pattern, 2))

    gl.glBegin(gl.GL_QUADS)
    gl.glColor3f(1, 1, 1)
    gl.glVertex2f(0, r)
    gl.glVertex2f(-r, 0)
    gl.glVertex2f(0, -r)
    gl.glVertex2f(r, 0)
    gl.glEnd()

    # построение прямоугольника на лицевой
    # построение ребер прямоугольника с помощью линии образца состоящего из нулей на нелицевой (нет отрисовки изображения)
    gl.glPolygonMode(gl.GL_FRONT, gl.GL_FILL)
    gl.glPolygonMode(gl.GL_BACK, gl.GL_LINE)
    gl.glLineWidth(1)

    pattern = '0b0000000000000000'
    gl.glLineStipple(2, int(pattern, 2))

    gl.glBegin(gl.GL_QUADS)
    gl.glColor3f(0, 0, 0)
    gl.glVertex2f(r / 2, r / 2)
    gl.glVertex2f(-r / 2, r / 2)
    gl.glVertex2f(-r / 2, -r / 2)
    gl.glVertex2f(r / 2, -r / 2)
    gl.glEnd()


    # построение вершин круга на лицевой
    # построение ребер полигона с помощью линии образца состоящего из нулей на нелицевой (нет отрисовки изображения)
    gl.glPolygonMode(gl.GL_FRONT, gl.GL_POINT)
    gl.glPolygonMode(gl.GL_BACK, gl.GL_LINE)

    pattern = '0b0000000000000000'
    gl.glLineStipple(2, int(pattern, 2))

    gl.glPointSize(3)
    gl.glEnable(gl.GL_POINT_SMOOTH)

    n = 60
    r1 = r / 2
    gl.glBegin(gl.GL_POLYGON)
    for i in range(n):
        x = r1 * math.cos((2 * math.pi * i) / n)
        y = r1 * math.sin((2 * math.pi * i) / n)
        gl.glColor3f(1, 1, 1)
        gl.glVertex2f(x, y)
    gl.glEnd()

    gl.glDisable(gl.GL_POINT_SMOOTH)

    # построение полигона в виде сердца на лицевой
    # построение вершин полигона на нелицевой
    gl.glPolygonMode(gl.GL_FRONT, gl.GL_FILL)
    gl.glPolygonMode(gl.GL_BACK, gl.GL_POINT)

    t = 2 * math.pi
    i = 0
    n = 30

    gl.glFrontFace(gl.GL_CW)
    gl.glBegin(gl.GL_POLYGON)
    while i < t:
        x = 0.5 * (16 * (math.sin(i) ** 3))
        y = 0.5 * (13 * math.cos(i) - 5 * math.cos(2 * i) - 2 * math.cos(3 * i) - math.cos(4 * i))
        gl.glColor3f(1, 0.50, 0.60)
        gl.glVertex2f(x, y)
        i = i + t / n
    gl.glEnd()
    gl.glFrontFace(gl.GL_CCW)

    # построение ребер полигона с помощью линии образца состоящего из нулей на лицевой (нет отрисовки изображения)
    # построение круга на нелицевой
    gl.glPolygonMode(gl.GL_FRONT, gl.GL_LINE)
    gl.glPolygonMode(gl.GL_BACK, gl.GL_FILL)

    pattern = '0b0000000000000000'
    gl.glLineStipple(2, int(pattern, 2))

    n = 60
    r2 = 0.85*r
    z = 0

    gl.glBegin(gl.GL_POLYGON)
    for i in range(n):
        x = r2 * math.cos((2 * math.pi * i) / n)
        y = r2 * math.sin((2 * math.pi * i) / n)
        z += 1 / n
        gl.glColor3f(0, 0, 0)
        gl.glVertex2f(x, y)
    gl.glEnd()


    # построение вершин четырехугольника
    # построение ребер четырехугольника с помощью линии образца на нелицевой
    gl.glPolygonMode(gl.GL_FRONT, gl.GL_POINT)
    gl.glPolygonMode(gl.GL_BACK, gl.GL_LINE)
    gl.glLineWidth(5)
    gl.glPointSize(1)

    pattern = '0b1101100110011011'
    gl.glLineStipple(2, int(pattern, 2))

    gl.glShadeModel(gl.GL_FLAT)

    gl.glBegin(gl.GL_QUADS)
    gl.glColor3f(0, 0, 0)
    gl.glVertex2f(10, 5)
    gl.glColor3f(0, 0, 1)
    gl.glVertex2f(10, 10)
    gl.glColor3f(1, 0, 0)
    gl.glVertex2f(-10, -10)
    gl.glColor3f(0.5, 0.5, 0.5)
    gl.glVertex2f(-5, -10)
    gl.glEnd()

    gl.glShadeModel(gl.GL_SMOOTH)

@window.event
def on_key_press(symbol, modifiers):
    global px, py
    if symbol == key._1:
        px = 1 - px
        py = 0
    elif symbol == key._2:
        px = 0
        py = 1 - py
    elif symbol == key._3:
        gl.glEnable(gl.GL_LINE_STIPPLE)
    elif symbol == key._4:
        gl.glDisable(gl.GL_LINE_STIPPLE)
app.run()