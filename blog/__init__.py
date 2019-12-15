#!/usr/bin/python3
import os
from flask import Flask
from flask_seasurf import SeaSurf
from flask_misaka import Misaka
import locale

app  = Flask(__name__)
app.config.from_pyfile("../blog.cfg")
app.static_folder = "static/dist"
app.jinja_env.trim_blocks   = True
app.jinja_env.lstrip_blocks = True

csrf = SeaSurf(app)
Misaka(app, strikethrough=True, wrap=True)

#Set timezone and locale
os.environ["TZ"] = "Europe/Amsterdam"
locale.setlocale(locale.LC_ALL, 'nl_NL')

from .views import *
