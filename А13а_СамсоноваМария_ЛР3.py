import numpy as np
import pyglet
from pyglet import app, gl, graphics
from pyglet.window import Window, key

sf,cf=(1/3)**0.5,(1/3)**0.5
sp,cp=(1/2)**0.5, (1/2)**0.5
iso=np.array([cp, sf * sp, 0.0, 0.0, 0.0, cp, 0.0, 0.0, sp, -sf * cp, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0])
iso=np.reshape(iso,(4,4))
print(iso)

width = height = 300 # Размер окна вывода

a = 20 # Длина половины стороны треугольника
h = 10 # Половины длины ребра куба
w = 40 # Для задания области вывода

n_rot = 0
rot_z = 1
rot = 0

textureIDs = (gl.GLuint * 6)() # Массив идентификаторов (номеров) текстур
p = gl.GL_TEXTURE_2D
tc = 1 # Число повторов текстуры

verts1 = ((a+h/2, h/2, h/2),
         (a+h/2, -h/2, h/2),
         (a-h/2, -h/2, h/2),
         (a-h/2, h/2, h/2),
         (a+h/2, h/2, -h/2),
         (a+h/2, -h/2, -h/2),
         (a-h/2, h/2, -h/2),
         (a-h/2, -h/2, -h/2))

verts2=  ((-a+h/2, h/2, h/2),
         (-a+h/2, -h/2, h/2),
         (-a-h/2, -h/2, h/2),
         (-a-h/2, h/2, h/2),
         (-a+h/2, h/2, -h/2),
         (-a+h/2, -h/2, -h/2),
         (-a-h/2, h/2, -h/2),
         (-a-h/2, -h/2, -h/2))

verts3= ((h/2, (3**0.5)*a+h/2, h / 2),
        (h/2, (3**0.5)*a-h/2, h / 2),
        (-h/2, (3**0.5)*a-h/2, h / 2),
        (-h/2, (3**0.5)*a+h/2, h / 2),
        (h/2, (3**0.5)*a+h/2, -h / 2),
        (h/2, (3**0.5)*a-h/2, -h / 2),
        (-h/2, (3**0.5)*a+h/2, -h / 2),
        (-h/2, (3**0.5)*a-h/2, -h / 2))

faces = ((0, 1, 2, 3), # Индексы вершин граней куба 1
         (3, 2, 7, 6),
         (6, 7, 5, 4),
         (4, 5, 1, 0),
         (1, 5, 7, 2),
         (4, 0, 3, 6))

clrs = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0),
        (0, 1, 1), (1, 1, 1), (1, 0, 0), (0, 1, 0),
        (0, 0, 1), (1, 1, 0), (0, 1, 1), (1, 1, 1))

# Индексы ребер куба (используется при выводе линий вдоль ребер куба)
edges = ((0, 1), (0, 3), (0, 4), (2, 1), (2, 3), (2, 7),
         (6, 3), (6, 4), (6, 7), (5, 1), (5, 4), (5, 7))

window = Window(visible = True, width = width, height = height,
                resizable = True, caption = 'Кубики')

t_coords = ((0, 0), (0, tc), (tc, tc), (tc, 0)) # Координаты текстуры

def texInit(): # Формирование текстур

    gl.glGenTextures(6, textureIDs)
    r = gl.GL_RGBA
    p3 = gl.GL_REPEAT
    p4 = gl.GL_LINEAR
    for k in range(6):
        fn = 'Cat' + str(k + 1) + '.jpg'
        img = pyglet.image.load(fn)  # загрузка изображения
        iWidth = img.width  # длина изображение
        iHeight = img.height  # ширина изображения

        img = img.get_data('RGBA', iWidth * 4)

        gl.glBindTexture(p, textureIDs[k])

        # Размещение по осям x и y
        gl.glTexParameterf(p, gl.GL_TEXTURE_WRAP_S, p3)
        gl.glTexParameterf(p, gl.GL_TEXTURE_WRAP_T, p3)

        gl.glTexParameterf(p, gl.GL_TEXTURE_MAG_FILTER, p4)
        gl.glTexParameterf(p, gl.GL_TEXTURE_MIN_FILTER, p4)

        gl.glTexImage2D(p, 0, r, iWidth, iHeight, 0, r, gl.GL_UNSIGNED_BYTE, img)

    gl.glEnable(p)

def cube_draw1(dt1):
    global rot
    k = -1
    gl.glPushMatrix()
    gl.glRotatef(rot, a, 0, 0)
    rot=rot+0.1

    for face in faces:
        k += 1
        m = -1
        v1= ()
        c1= ()
        t1= ()
        gl.glBindTexture(p, textureIDs[k])
        for v in face:
            m += 1
            c1 += clrs[k + m]
            v1 += verts1[v]
            t1 += t_coords[m]
        graphics.draw(4, gl.GL_QUADS, ('v3f', v1), ('c3f', c1),('t2f', t1) )
    gl.glPopMatrix()

def cube_draw2(dt2):
    global rot
    k = -1
    gl.glPushMatrix()
    gl.glRotatef(rot, -a, 0, 0)
    rot = rot + 0.1

    for face in faces:
        k += 1
        m = -1
        v2= ()
        c2= ()
        t2= ()
        gl.glBindTexture(p, textureIDs[k])
        for v in face:
            m += 1
            c2 += clrs[k + m]
            v2 += verts2[v]
            t2 += t_coords[m]
        graphics.draw(4, gl.GL_QUADS, ('v3f', v2), ('c3f', c2), ('t2f', t2) )
    gl.glPopMatrix()

def cube_draw3(dt3):
    global rot
    k = -1
    gl.glPushMatrix()
    gl.glRotatef(rot, 0, (3**0.5)*a, 0)
    rot = rot + 0.1
    for face in faces:
        k += 1
        m = -1
        v3= ()
        c3= ()
        t3 = ()
        gl.glBindTexture(p, textureIDs[k])
        for v in face:
            m += 1
            c3 += clrs[k + m]
            v3 += verts3[v]
            t3 += t_coords[m]
        graphics.draw(4, gl.GL_QUADS, ('v3f', v3), ('c3f', c3), ('t2f', t3) )
    gl.glPopMatrix()

gl.glClearColor(0, 0, 0, 1) # Черный цвет фона
gl.glClear(gl.GL_COLOR_BUFFER_BIT|gl.GL_DEPTH_BUFFER_BIT)
gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)
gl.glShadeModel(gl.GL_SMOOTH) # GL_SMOOTH, GL_FLAT
gl.glEnable(gl.GL_DEPTH_TEST)
gl.glDepthFunc(gl.GL_LESS) # GL_LESS GL_GREATER
#
texInit()

@window.event
def on_draw():
    window.clear()
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()

    gl.glRotatef(60.0, 1.0, 0.0, 0.0)
    gl.glRotatef(45.0, 0.0, 0.0, 1.0)

    #gl.glPushMatrix()
    #gl.glLoadMatrixf(iso.ctypes.data_as(ctypes.POINTER(ctypes.c_float))) #Матрица перевода (Не рабоатет)
    #gl.glPopMatrix()

    gl.glOrtho(-w, w, -w, w, -w, w)


    global n_rot, rot_z
    gl.glMatrixMode(gl.GL_MODELVIEW)

    gl.glPushMatrix()
    gl.glLoadIdentity()

    gl.glBegin(gl.GL_LINES)
    gl.glColor3f(0, 0, 1)
    gl.glVertex3f(0, 0, 100)
    gl.glVertex3f(0, 0, -100)

    gl.glColor3f(0, 1, 0)
    gl.glVertex3f(0, 100, 0)
    gl.glVertex3f(0, -100, 0)

    gl.glColor3f(1, 0, 0)
    gl.glVertex3f(100, 0, 0)
    gl.glVertex3f(-100, 0, 0)
    gl.glEnd()

    gl.glPopMatrix()

    gl.glBegin(gl.GL_TRIANGLES)
    gl.glColor3f(1, 0, 0)
    gl.glVertex3f(-a, 0, 0)
    gl.glColor3f(0, 1, 0)
    gl.glVertex3f(a, 0, 0)
    gl.glColor3f(0, 0, 1)
    gl.glVertex3f(0, (3 ** 0.5) * a, 0)
    gl.glEnd()

    if n_rot > 360:
        n_rot = 0
        rot_z = 1
    n_rot += 1
    gl.glRotatef(rot_z, 0, 0, 1) # Поворот относительно оси Z



    pyglet.clock.tick()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key._1:
        gl.glCullFace(gl.GL_BACK)
        gl.glEnable(gl.GL_CULL_FACE)
    elif symbol == key._2:
        gl.glDisable(gl.GL_CULL_FACE)
    elif symbol == key._3:
        gl.glTexEnvf(gl.GL_TEXTURE_ENV, gl.GL_TEXTURE_ENV_MODE,gl.GL_DECAL)  # игнорирование основного источника цвета


pyglet.clock.schedule(cube_draw1)
pyglet.clock.schedule(cube_draw2)
pyglet.clock.schedule(cube_draw3)

app.run()