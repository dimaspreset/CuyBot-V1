from kivymd.app import MDApp
from screens.home import HomeScreen
from kivy.core.text import LabelBase

class CuyBotApp(MDApp):
    def build(self):
        LabelBase.register(name="Titillium Web", fn_regular="assets/fonts/TitilliumWeb-Regular.ttf")
        LabelBase.register(name="Titillium Web Bold", fn_regular="assets/fonts/TitilliumWeb-Bold.ttf")

        return HomeScreen()

CuyBotApp().run()
