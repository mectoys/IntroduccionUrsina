'''Mini reproductor
Boton play/pause, stop, control de volumen(+,-)'''
from ursina import *

app = Ursina()
audio = None
window.fps_counter.visible = False
audio_paused = False

def PlayButton():
    global audio, audio_paused
    if audio is not None and audio.playing:
        audio.pause()
        audio_paused = True
    elif audio is not None and audio_paused:
        audio.resume()
        audio_paused = False
    else:
        audio = Audio()
        audio.clip = 'audio//TMNT1.mp3'
        audio.play()
        print_on_screen(round(audio.volume, 2), position=(0, 0.2))


def StopButton():
    global audio, audio_paused
    if audio is not None:
        audio.stop()
        audio = None
        audio_paused = False


def Increase_volumen():
    global audio, audio_paused
    if audio is not None:
        audio.volume += 0.1
        print_on_screen(round(audio.volume, 2), position=(0, 0.2))


def Decrease_volumen():
    global audio, audio_paused
    if audio is not None:
        audio.volume -= 0.1
        print_on_screen(round(audio.volume, 2), position=(0, 0.2))


# Botones
# boton play
b_play = Button(text='Play/Pause', color=rgb(166, 166, 166, ), position=(-.6, 0), scale=.25)
b_play.tooltip = Tooltip('Play/Pause Music')
b_play.on_click = PlayButton
# boton stop
b_stop = Button(text='Stop', color=color.blue, position=(-.2, 0), scale=.25)
b_stop.tooltip = Tooltip('Stop Music')
b_stop.on_click = StopButton

# boton +volume
b_increase = Button(text='Subir Volumen', color=color.cyan, position=(.2, 0), scale=.25)
b_increase.tooltip = Tooltip('Subir Volumen')
b_increase.on_click = Increase_volumen

# boton - volumen
b_decrease = Button(text='Bajar Volumen', color=color.azure, position=(.6, 0), scale=.25)
b_decrease.tooltip = Tooltip('Bajar Volumen')
b_decrease.on_click = Decrease_volumen

app.run()
