package org.kivy.custom;

import android.service.notification.NotificationListenerService;
import android.service.notification.StatusBarNotification;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;

public class NotificationService extends NotificationListenerService {

    private static final String TAG = "CuyNotifService";

    @Override
    public void onNotificationPosted(StatusBarNotification sbn) {
        String packageName = sbn.getPackageName();
        Bundle extras = sbn.getNotification().extras;

        String title = extras.getString("android.title", "");
        String text = extras.getCharSequence("android.text", "").toString();

        Log.d(TAG, "Notif dari: " + packageName + " | Judul: " + title + " | Teks: " + text);

        Intent intent = new Intent("org.kivy.NOTIFICATION_LISTENER");
        intent.putExtra("package", packageName);
        intent.putExtra("title", title);
        intent.putExtra("text", text);
        sendBroadcast(intent);
    }

    @Override
    public void onNotificationRemoved(StatusBarNotification sbn) {
        // Tidak wajib, hanya log kalau perlu
        Log.d(TAG, "Notifikasi dihapus dari: " + sbn.getPackageName());
    }
}
