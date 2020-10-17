# -*- coding: utf-8 -*-

import pyrebase

__author__ = "Tiago Bratz Heck"
__maintainer__ = "Tiago Bratz Heck"
__version__ = "1.0.1"


config = {
    "apiKey": "AIzaSyDOT7iCi-rbh5O7w2_hT5bt10KI4h5dhKY",
    "authDomain": "cloudstorage-3051c.firebaseapp.com",
    "databaseURL": "https://cloudstorage-3051c.firebaseio.com",
    "projectId": "cloudstorage-3051c",
    "storageBucket": "cloudstorage-3051c.appspot.com",
    "messagingSenderId": "441912184158",
    "appId": "1:441912184158:web:2f72cf48fd266b6be553cf",
    "measurementId": "G-90J316SVZP"
}

firebase = pyrebase.initialize_app(config)

