import kivy
from kivy.app import App # app class for inheritance
from gridlayout import Wyglad # grid layout class
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


#kv = Builder.load_file('dicegui.kv')

#
# class MainScreenApp(Screen):
#
#     def __init__(self, **kwargs):
#         super(MainScreenApp, self).__init__(**kwargs)
#         app_layout = Wyglad()
#         self.add_widget(app_layout)
#
#
# Builder.load_file("dicegui.kv")
# screen_manager = ScreenManager()
# screen_manager.add_widget(MainScreenApp(name='main'))


class DiceguiApp(App):

    def build(self): # constructor

        self.title = 'KOSTUNIE💀'

        #return screen_manager

        return Wyglad()