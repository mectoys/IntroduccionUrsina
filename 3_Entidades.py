#ENTIDADES
from ursina import *

app=Ursina()
#quad, cubo, circulo, esfera
Entity(model="cube",color=color.azure, position=(0,0,0),rotation=(45,80,45),scala=1.5,texture="white_cube")
Entity(model="quad",color=color.blue, position=(-3,0,0),rotation=(45,0,0),scala=2,texture="brick")
Entity(model="circle",color=color.yellow, position=(3,0,0),rotation=(0,0,45),scala=3,texture="brick")
Entity(model="sphere",color=rgb(255,0,0), position=(0,2,0),rotation=(45,0,45),scala=1,texture="brick")

app.run()