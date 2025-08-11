from kivymd.app import MDApp
from kivy.core.text import LabelBase
from kivy.utils import platform
from kivy.clock import Clock
from screens.home import HomeScreen
from kivy.logger import Logger
from kivymd.uix.list import OneLineListItem

# Android-specific imports
if platform == 'android':
    from android.permissions import request_permissions, Permission
    from android.storage import app_storage_path


class CuyBotApp(MDApp):
    def build(self):
        # Register custom fonts
        LabelBase.register(
            name="Titillium Web",
            fn_regular="assets/fonts/TitilliumWeb-Regular.ttf"
        )
        LabelBase.register(
            name="Titillium Web Bold", 
            fn_regular="assets/fonts/TitilliumWeb-Bold.ttf"
        )
        
        # Set app theme
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        
        return HomeScreen()

    def on_start(self):
        # Request permissions on Android
        if platform == 'android':
            self.request_android_permissions()
        
        # Start notification listener with delay
        Clock.schedule_once(self.start_services, 5)

    def request_android_permissions(self):
        try:
            from android.permissions import request_permissions, Permission
            permissions = [
                Permission.BIND_NOTIFICATION_LISTENER_SERVICE,
                Permission.RECEIVE_BOOT_COMPLETED,
                Permission.FOREGROUND_SERVICE
            ]
            request_permissions(permissions, self.permission_callback)
        except Exception as e:
            Logger.error(f"Permission error: {str(e)}")

    def permission_callback(self, permissions, grant_results):
        if all(grant_results):
            Logger.info("All permissions granted")
        else:
            Logger.warning("Some permissions were denied")

    def start_services(self, dt):
        try:
            from bridge import start_notification_listener
            start_notification_listener()
            Logger.info("Notification service started")
        except Exception as e:
            Logger.error(f"Service start failed: {str(e)}")

    def on_notification(self, package, title, text):
        """Callback for received notifications"""
        Clock.schedule_once(
            lambda dt: self.root.add_notification(package, title, text)
        )

if __name__ == '__main__':
    CuyBotApp().run()