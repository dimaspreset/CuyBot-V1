from jnius import autoclass, PythonJavaClass, java_method
from android.runnable import run_on_ui_thread

# Variabel global untuk menyimpan callback
notification_callback = None

# Kelas Python untuk menerima notifikasi dari Java
class NotificationReceiver(PythonJavaClass):
    __javainterfaces__ = ['org/kivy/android/PythonActivity$NotificationCallback']
    __javacontext__ = 'app'

    @java_method('(Ljava/lang/String;Ljava/lang/String;)V')
    def onNotificationReceived(self, title, text):
        global notification_callback
        if notification_callback:
            # Panggil fungsi callback dengan data notifikasi
            notification_callback(title, text)

# Fungsi untuk set callback dari luar (misal dari main.py)
def set_notification_callback(callback):
    global notification_callback
    notification_callback = callback

# Fungsi untuk inisialisasi listener dari sisi Python
@run_on_ui_thread
def start_notification_listener():
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    activity = PythonActivity.mActivity

    # Buat receiver dan simpan sebagai field agar tidak dihapus GC
    receiver = NotificationReceiver()
    activity.setNotificationCallback(receiver)
