package org.kivy.cuybot;

import android.service.notification.NotificationListenerService;
import android.service.notification.StatusBarNotification;
import android.util.Log;

public class NotificationService extends NotificationListenerService {
    private static NotificationCallback callback;

    // dipanggil dari Python (pyjnius) untuk set listener
    public static void setCallback(NotificationCallback cb) {
        callback = cb;
    }

    @Override
    public void onNotificationPosted(StatusBarNotification sbn) {
        try {
            String pkg = sbn.getPackageName();
            String title = "";
            String text = "";

            if (sbn.getNotification() != null && sbn.getNotification().extras != null) {
                CharSequence t = sbn.getNotification().extras.getCharSequence("android.title");
                CharSequence m = sbn.getNotification().extras.getCharSequence("android.text");
                title = t != null ? t.toString() : "";
                text = m != null ? m.toString() : "";
            }

            Log.d("CUYBOT", "onNotificationPosted: " + pkg + " | " + title + " | " + text);

            if (callback != null) {
                callback.onNotificationReceived(pkg, title, text);
            }
        } catch (Exception e) {
            Log.e("CUYBOT", "Error in onNotificationPosted", e);
        }
    }

    @Override
    public void onNotificationRemoved(StatusBarNotification sbn) {
        Log.d("CUYBOT", "onNotificationRemoved: " + sbn.getPackageName());
    }
}
