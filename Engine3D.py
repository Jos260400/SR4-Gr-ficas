#Universidad del Valle de Guatemala
#Graficas por Computadoras
#Fernando Jose Garavito Ovando 1807
#SR4 Flat Shading & Textures
# Programa principal
from gl import Renderer, V3, _color

from obj import Texture

import random

width = 1000
height = 600

rend = Renderer(width, height)

modelTexture = Texture("models/model.bmp")


rend.glLoadModel("models/model.obj", modelTexture, V3(width/2, height/2, 0), V3(200,200,200))


rend.glFinish("SR4 Flat Shading & Textures.bmp")


