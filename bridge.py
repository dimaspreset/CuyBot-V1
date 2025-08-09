from kivy.utils import platform

if platform == "android":
    from jnius import autoclass, PythonJavaClass, java_method
    from android import mActivity

    # class Java
    NotificationService = autoclass('org.kivy.cuybot.NotificationService')

    # Python implementation of Java interface
    class NotificationReceiver(PythonJavaClass):
        __javainterfaces__ = ['org/kivy/cuybot/NotificationCallback']
        __javacontext__ = 'app'

        @java_method('(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V')
        def onNotificationReceived(self, package_name, title, text):
            # di sini kamu bisa kirim event Kivy atau update UI
            print(f"[NOTIF] {package_name} | {title} | {text}")
            # contoh: dispatch ke event atau simpan di list

    def start_notification_listener():
        try:
            receiver = NotificationReceiver()
            # panggil static method setCallback(receiver)
            NotificationService.setCallback(receiver)
            print("[INFO] Notification listener aktif (Android)")
        except Exception as e:
            print("[ERROR] Gagal set callback:", e)

else:
    # desktop fallback: supaya main.py bisa dijalankan di PC tanpa crash
    def start_notification_listener():
        print("[DEBUG] start_notification_listener() dipanggil (PC mode)")
