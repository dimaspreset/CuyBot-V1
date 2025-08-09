package org.kivy.cuybot; // GANTI sesuai package di buildozer.spec

import android.service.notification.NotificationListenerService;
import android.service.notification.StatusBarNotification;
import android.util.Log;

public class NotificationService extends NotificationListenerService {

    private static NotificationCallback callback;

    // Dipanggil dari Python untuk set listener
    public static void setCallback(NotificationCallback cb) {
        callback = cb;
    }

    @Override
    public void onNotificationPosted(StatusBarNotification sbn) {
        String packageName = sbn.getPackageName();
        String title = "";
        String text = "";

        if (sbn.getNotification().extras != null) {
            title = sbn.getNotification().extras.getString("android.title", "");
            CharSequence cs = sbn.getNotification().extras.getCharSequence("android.text");
            if (cs != null) {
                text = cs.toString();
            }
        }

        Log.d("CUYBOT", "Notifikasi dari: " + packageName + " | " + title + " - " + text);

        // Kirim ke Python jika callback sudah diset
        if (callback != null) {
            callback.onNotificationReceived(packageName, title, text);
        }
    }

    @Override
    public void onNotificationRemoved(StatusBarNotification sbn) {
        Log.d("CUYBOT", "Notifikasi dihapus: " + sbn.getPackageName());
    }
}
