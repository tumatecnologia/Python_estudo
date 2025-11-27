echo "[app]
title = WhatsApp Sender
package.name = whatssender
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt

version = 0.1
requirements = python3,kivy,sqlite3

android.permissions = INTERNET
android.api = 21
android.minapi = 21

orientation = portrait

[buildozer]
log_level = 2" > buildozer.spec