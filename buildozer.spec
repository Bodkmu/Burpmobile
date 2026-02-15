[app]

# (str) Title of your application
title = BurpMobile

# (str) Package name
package.name = burpmobile

# (str) Package domain (needed for android/ios packaging)
package.domain = org.tech

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# تم إضافة requests و urllib3 لأعمال البروكسي و KivyMD للواجهة
requirements = python3, kivy==2.3.0, kivymd, requests, urllib3, certifi

# (list) Permissions
# تم إضافة صلاحيات الإنترنت والخدمات الخلفية (ضروري جداً للبروكسي)
android.permissions = INTERNET, ACCESS_NETWORK_STATE, FOREGROUND_SERVICE, WAKE_LOCK

# (int) Target Android API (API 33 متوافق مع متطلبات 2026)
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then automatically accept SDK license
# ضروري جداً لنجاح العملية على GitHub Actions بدون تدخل يدوي
android.accept_sdk_license = True

# (bool) Enable AndroidX support (مطلوب لـ KivyMD)
android.enable_androidx = True

# (list) The Android archs to build for
# اخترنا arm64-v8a فقط لتسريع عملية الـ Build في البداية
android.archs = arm64-v8a

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

# (str) The format used to package the app for debug mode (apk or aar).
android.debug_artifact = apk

[buildozer]

# (int) Log level (2 = debug لترى كل التفاصيل في GitHub Actions)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
