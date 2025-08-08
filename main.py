from kivymd.app import MDApp
from screens.home import HomeScreen
from kivy.core.text import LabelBase
from notification_listener import start_notification_listener, set_notification_callback


class CuyBotApp(MDApp):
    def build(self):
        LabelBase.register(name="Titillium Web", fn_regular="assets/fonts/TitilliumWeb-Regular.ttf")
        LabelBase.register(name="Titillium Web Bold", fn_regular="assets/fonts/TitilliumWeb-Bold.ttf")

        return HomeScreen()

    def on_start(self):
        # Panggil fungsi listener notifikasi saat aplikasi dimulai
        start_notification_listener()

        # Set callback untuk menerima data notifikasi dan update UI
        set_notification_callback(self.on_notification_received)

    def on_notification_received(self, package_name, title, text):
        # Fungsi ini akan dipanggil setiap ada notifikasi masuk
        print(f"[NOTIFICATION] Dari: {package_name}\nJudul: {title}\nIsi: {text}")

        # Jika kamu ingin update UI, kamu bisa panggil metode dari HomeScreen, contoh:
        home_screen = self.root
        if hasattr(home_screen, 'update_notification_preview'):
            home_screen.update_notification_preview(title, text)


CuyBotApp().run()
