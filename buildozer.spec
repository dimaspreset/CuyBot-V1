[app]
title = CuyBot
package.name = cuybot
package.domain = org.kivy

requirements = 
    python==3.8.5,
    kivy==2.2.1,
    kivymd==1.1.1,
    pyjnius==1.4.2,
    android==0.9,
    pillow==10.0.0

android.permissions = 
    BIND_NOTIFICATION_LISTENER_SERVICE,
    RECEIVE_BOOT_COMPLETED,
    FOREGROUND_SERVICE,
    POST_NOTIFICATIONS

android.api = 33
android.minapi = 21
android.ndk = 23b
android.sdk = 33

# Add services and manifest
android.add_src = src
services = NotificationService:org.kivy.cuybot.NotificationService
android.extra_manifest_xml = src/main/AndroidManifest.xml