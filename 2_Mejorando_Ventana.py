from ursina import *

app = Ursina()
window.show_ursina_splash=True
window.exit_button.visible=True
window.exit_button.texture='sword'
window.exit_button.text=''
window.exit_button.color=color.white
window.fps_counter.visible=False


app.run()