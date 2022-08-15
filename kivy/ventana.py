from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label

class TestApp(App):
    def build(self):

        
        
        self.l2= Label(text ="Label is Added on \n screen !!:):), font_size ='20sp',color =[0.41, 0.42, 0.74, 1]
       return self.l2
       


TestApp().run()