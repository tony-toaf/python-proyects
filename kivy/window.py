from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from random import choice, shuffle
from kivy.core.window import Window
 
Window.clearcolor = (.10, .54, 1, 1)
Window.size = (500,300)
 
list_of_words = ['ELEPHANT', 'LION', 'COCODRILE', 'MONKEY', 'KANGAROO']
 
def create_anagram():
    # Chooses a word from the list and shuffles the letters to create the anagram
 
    choices = choice(list_of_words)
    list_letters = []
    for item in choices:
        list_letters.append(item)
    shuffle(list_letters)
    choices = ''.join(list_letters)
 
    return choices
 
class MainApp(App):
 
    def build(self):
 
        # These are all variables which will be used later on.
 
        self.choices = create_anagram()
        self.window = RelativeLayout()
        self.font_size = 20
        self.letters, self.underscores = [],[]
        self.ind = 0                         # Index used on chose_letter()
        self.size_x, self.size_y = 100, 50
        self.pos_x = 0
        self.word = ''                       # will concatonate the letters choosen.
 
        # Adding the buttons to the respectives lists.
        for letter in self.choices:
            self.window.add_widget(Button(text=letter,
                                        size_hint=(1/len(self.choices), 0.2),
                                        pos_hint = {'x': self.pos_x, 'top': .8},
                                        font_size = self.font_size,
                                        color='#688FF8',
                                        background_color = '#1F48F2',
                                        on_press = self.chose_letter,
                                        disabled = False))
 
            self.underscores.append(Label(text='_',
                                        size_hint=(1/len(self.choices), 0.2),
                                        pos_hint = {'x': self.pos_x, 'top': 0.4},
                                        size=(self.size_x, self.size_y),
                                        font_size = self.font_size,
                                        color = '#FFFFFF'))
 
            self.pos_x += 1/len(self.choices)
 
        # Adding buttons for the letters and the underscores.
        for item in self.letters:
            self.window.add_widget(item)
        for item in self.underscores:
            self.window.add_widget(item)
 
        self.RESTART = Button(text='RESTART',
                                            size_hint=(0.2,0.1),
                                            font_size = 12,
                                            pos_hint = {'center_x': .5,'center_y': 0.1},
                                            on_press = self.on_press_restart)
        self.window.add_widget(self.RESTART)
 
        return self.window
 
 
 
    def chose_letter(self, instance):
        # When the user clicks on a letter, it adds that letter to the first empty label and to self.word
 
        if self.ind == len(self.choices):               # If we click a button when the word is complete (either correct or incorrect)
            return True                                 # This will allow the program not to add 1 to self.ind (and will not cursh)
 
 
        _choice = instance.text                         # Gets the text from the button
        self.underscores[self.ind].text = _choice       # Changes the first underscore for the text in _choice
        self.ind += 1                                   # Adds 1 to the index counter
        self.word += _choice                            # Copies the word created, in order to compare it to the words on the list (in the next line)
 
 
        # It shows a message, either the word is correct or not.
        if len(self.choices) == len(self.word):
            if self.word in list_of_words:
                self.CONGRAT = Label(text='CONGRATULATIONS! THE WORD IS: ',
                                            size_hint=(.8, .4),
                                            pos_hint = {'center_x':0.5, 'center_y': 0.45},
                                            font_size = self.font_size)
                self.window.add_widget(self.CONGRAT)
 
                self.NEW = Button(text='NEW WORD',
                                            size_hint=(0.2,0.1),
                                            font_size = 12,
                                            pos_hint = {'center_x': .5,'center_y': 0.1},
                                            on_press = self.on_press_new)
                self.window.add_widget(self.NEW)
 
            else:
                self.SORRY = Label(text='SORRY, WORNG WORD!',
                                            size_hint=(.8, .4),
                                            pos_hint = {'center_x':0.5, 'center_y': 0.45},
                                            font_size = self.font_size)
                self.window.add_widget(self.SORRY)
 
 
    def on_press_restart(self, instance):
        under_index = 0
        for item in self.underscores:
            self.underscores[under_index].text = '_'
            under_index += 1
        self.ind = 0
        self.word = ''
        # self.window.remove_widget(self.SORRY)
 
    def on_press_new(self, instance):
        # self.choices = create_anagram()
        print(self.choices)
 
        self.window.remove_widget(self.NEW)     # It owrks, but the game doesn't restart.
        self.window.remove_widget(self.CONGRAT)
 
if __name__ == '__main__':
    MainApp().run()