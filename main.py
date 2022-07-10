from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

def click():
    print(ed.text)

def build():
    layout = FloatLayout()

    global ed
    ed = TextInput(text="eXcript")

    ed.size_hint = None, None
    ed.height = 300
    ed.width = 400
    ed.x = 100
    ed.y = 250

    bt = Button(text="Clique aqui")
    bt.size_hint = None, None
    bt.width = 200
    bt.height = 50
    bt.x = 200
    bt.y = 100

    bt.on_press = click

    layout.add_widget(ed)
    layout.add_widget(bt)


    return  layout

janela = App()
from kivy.core.window import Window
Window.size = 600,600
janela.build = build
janela.run()