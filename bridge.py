from kivy.utils import platform
from kivy.clock import Clock
from kivy.logger import Logger

if platform == "android":
    from jnius import autoclass, PythonJavaClass, java_method, cast
    from android import mActivity
    from android.permissions import request_permissions, Permission

    # Request permission saat module di-load
    request_permissions([Permission.BIND_NOTIFICATION_LISTENER_SERVICE])

    # Java classes
    PythonService = autoclass('org.kivy.android.PythonService')
    NotificationService = autoclass('org.kivy.cuybot.NotificationService')
    Context = autoclass('android.content.Context')
    Intent = autoclass('android.content.Intent')

    class NotificationReceiver(PythonJavaClass):
        __javainterfaces__ = ['org/kivy/cuybot/NotificationCallback']
        __javacontext__ = 'app'

        @java_method('(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V')
        def onNotificationReceived(self, package_name, title, text):
            Logger.info(f"Notification: {package_name} | {title} | {text}")
            # Dispatch to Kivy event system
            Clock.schedule_once(lambda dt: self._dispatch_event(package_name, title, text))

        def _dispatch_event(self, package, title, text):
            from kivy.app import App
            app = App.get_running_app()
            if hasattr(app, 'on_notification'):
                app.on_notification(package, title, text)

    def start_notification_listener():
        try:
            # Start foreground service
            service = PythonService.mService
            if service:
                context = cast('android.content.Context', service)
                intent = Intent(context, NotificationService)
                context.startForegroundService(intent)
            
            # Set callback
            receiver = NotificationReceiver()
            NotificationService.setCallback(receiver)
            Logger.info("Notification service started")
        except Exception as e:
            Logger.error(f"Notification error: {str(e)}")

else:
    def start_notification_listener():
        Logger.info("Notification service (desktop dummy)")