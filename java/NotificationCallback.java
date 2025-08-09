package org.kivy.cuybot; // GANTI sesuai package di buildozer.spec

public interface NotificationCallback {
    void onNotificationReceived(String packageName, String title, String text);
}
