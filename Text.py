from ursina import *

def input(key):
    if key =='u':
        print_on_screen("ursina engine")
    if key =='h':
        print_on_screen("Hola Mundo")


app =Ursina()

descripcion ='''¿Qué es Lorem Ipsum?
Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. 
Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, 
cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos 
y los mezcló de tal manera que logró hacer un libro de textos especimen.'''

descr=Text(text=descripcion,wordwrap=30,color=color.blue)
app.run()