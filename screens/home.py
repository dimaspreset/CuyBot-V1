from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.properties import StringProperty

Builder.load_file("kv/home.kv")


class HomeScreen(MDScreen):
    notif_title = StringProperty("Belum ada notifikasi")
    notif_text = StringProperty("")

    def update_notification_preview(self, title, text):
        self.notif_title = title
        self.notif_text = text
