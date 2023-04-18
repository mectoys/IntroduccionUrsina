from ursina import *

def Mensaje():
    print_on_screen("Soy un texto",duration=3,position=(.6,0))

app = Ursina()

b = Button(text='Exit', color=color.cyan, icon="sword", scale=.25)
b.on_click = application.quit
b.tooltip = Tooltip('Salir')

b1 = Button(text='Boton Click', color=color.blue, icon="file_icon", scale=.25,position=(.5,0))
b1.on_click = Mensaje
b1.tooltip = Tooltip('Boton Click')
app.run()
