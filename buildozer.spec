[app]

title = SmartBatteryAI
package.name = smartbatteryai
package.domain = org.smartbatteryai

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 0

# Android
android.api = 34
android.minapi = 23
android.ndk = 25b

# IMPORTANT
android.archs = arm64-v8a

android.permissions = INTERNET

# Fichiers
presplash.filename =
icon.filename =

log_level = 2

[buildozer]

warn_on_root = 1
