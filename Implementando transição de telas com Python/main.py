import kivy
kivy.require('1.9.1') #versão mínima da biblioteca que deve ser utilizada

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class Tela1(BoxLayout):

    def on_press_bt(self):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(Tela2())

    def __init__(self, **kwargs):
        super(Tela1, self).__init__(**kwargs) #Acessa a função __init__ da superclasse BoxLayout da qual Tela1 foi instênciada
        self.orientation = "vertical"
        bt1 = Button(text="Click")
        bt1.on_press = self.on_press_bt
        self.add_widget(bt1)
        self.add_widget(Button(text="bt2"))
        self.add_widget(Button(text="bt3"))

class Tela2(BoxLayout):

    def on_press_bt(self):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(Tela1())

    def __init__(self, **kwargs):
        super(Tela2, self).__init__(**kwargs)
        self.orientation = "vertical"
        bt = Button(text = "Click")
        bt.on_press = self.on_press_bt
        self.add_widget(bt)




class KVvsPY(App):
    def build(self):
        return Tela1()

janela = KVvsPY()
janela.run()
