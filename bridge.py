from kivy.utils import platform

if platform == "android":
    from jnius import autoclass, PythonJavaClass, java_method
    Log = autoclass('android.util.Log')
    from android import mActivity

    # class Java
    NotificationService = autoclass('org.kivy.cuybot.NotificationService')

    # Python implementation of Java interface
    class NotificationReceiver(PythonJavaClass):
        __javainterfaces__ = ['org/kivy/cuybot/NotificationCallback']
        __javacontext__ = 'app'

        @java_method('(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V')
        def onNotificationReceived(self, package_name, title, text):
            # Log to Android logcat so it appears in adb logcat output
            Log.d("cuybot", f"{package_name} | {title} | {text}")
            # You can also dispatch Kivy events or update UI here

    def start_notification_listener():
        try:
            receiver = NotificationReceiver()
            # Call static method setCallback(receiver)
            NotificationService.setCallback(receiver)
            Log.i("cuybot", "Notification listener aktif (Android)")
        except Exception as e:
            Log.e("cuybot", f"Gagal set callback: {e}")

else:
    # desktop fallback: supaya main.py bisa dijalankan di PC tanpa crash
    def start_notification_listener():
        print("[DEBUG] start_notification_listener() dipanggil (PC mode)")