from kivy.app import App

from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.config import Config

Config.set('graphics', 'resizable', False)


import random
from datetime import datetime
#import time
import os



class Wyglad(FloatLayout):
    # setting position of the window to apper on the screen
    Window.top = 55
    Window.left = 550

    # size of the window (resolution)
    Window.size = (360, 680)


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._now = datetime.now()  # current date and time
        self._memory = []
        self._memory.append('Roll History:')  # header of the history file



    def roll(self): #, instance): # nie potrzeba instance gdy sie uzywa kividl
        # s = dice sides
        # a = dice amount

        current_rolls = []

        # variable assignment
        # a = int(self.d_amount.text)
        # s = int(self.d_sides.text)
        a = int(self.ids.d_amount_kv.text)
        s = int(self.ids.d_sides_kv.text)
        mod_to_slice = str(self.ids.d_mod_kv.text)

        # slicing mod_to_slice_string
        sp_ch = ''

        if len(mod_to_slice) > 1:
            if mod_to_slice[0] == '+':
                sp_ch = '+'
            elif mod_to_slice[0] == '-':
                sp_ch = '-'

            mod_sliced = mod_to_slice.split(sp_ch, 1)

        elif len(mod_to_slice) != 0 and type(mod_to_slice[0]) == int:
            mod_sliced = ['+', mod_to_slice[0]]

        else:
            mod_to_slice = ['+', '0']
            mod_sliced = ['+', '0']


        for j in range(a):
            appen = None
            dice = random.randint(1, s)

            if mod_to_slice[0] == '+':
                appen = dice + int(mod_sliced[1])
            elif mod_to_slice[0] == '-':
                appen = dice - int(mod_sliced[1])


            current_rolls.append(appen)



        # printing strings to screen loop
        s_str_d = ""

        i = 0

        while i < len(current_rolls):
            if i == 0:
                s_str_d = str(current_rolls[i])
            else:
                s_str_d = s_str_d + ", " + str(current_rolls[i])

            i += 1

        self.ids.results.text = s_str_d

        self._memory.append(s_str_d)



        # clearing the input boxes after rolling
        # self.ids.d_sides_kv.text = ''
        # self.ids.d_amount_kv.text = ''




    def _history(self): #, instance):
        #self.ids.hist_kv.text = self._memory[1]
        print(self._memory)




    def _save_h(self): #, instance):
        if len(self._memory) > 1:
            # generate new file name each time so history files don't overwrite
            f_name = self._now.strftime("%m-%d-%Y-%H-%M-%S")

            with open(r'roll_history_files/history_file_' + f_name + '.txt',
                      'w') as f_path:
                f_path.write('\n'.join(str(item) for item in self._memory))

            #print('saved to history_file.txt')




    def open_folder(self):
        os.startfile('roll_history_files')  # opening the folder where history files are located
