from jnius import autoclass, PythonJavaClass, java_method

# Ambil class Java
NotificationService = autoclass('org.kivy.cuybot.NotificationService')  
# Ganti 'org.example.cuybot' sesuai package-mu

# Class Python yang implementasi interface Java
class NotificationReceiver(PythonJavaClass):
    __javainterfaces__ = ['org/example/cuybot/NotificationCallback']  # ganti sesuai package
    __javacontext__ = 'app'

    @java_method('(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V')
    def onNotificationReceived(self, package_name, title, text):
        print(f"[NOTIF] {package_name} | {title} | {text}")
        # Di sini nanti bisa kirim event ke UI Kivy

def start_notification_listener():
    receiver = NotificationReceiver()
    NotificationService.setCallback(receiver)
    print("[INFO] Notification listener aktif")
