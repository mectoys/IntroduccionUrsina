from ursina import *

a = Audio()


def input(key):
    if key == "space":
        a.clip='audio//TMNT1.mp3'
        a.play()

    elif key == "s":
        a.stop()


app = Ursina()

app.run()
