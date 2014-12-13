#!/usr/bin/env python
# -*- coding: utf-8 -*-
from application import route
from flask import render_template

@route('/')
def home():
    return render_template("index.html")
        

