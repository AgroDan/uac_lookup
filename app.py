#!/usr/bin/env python3
from flask import Flask, request, render_template, url_for
import uacrights

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def presentForm():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        uacnum = request.form.get('uacnum')
        try:
            uacnum = int(uacnum)
        except:
            uacnum = 0

        uac_vals = uacrights.getRights(uacnum)
        return render_template("index.html", init_val=uacnum, return_val=uac_vals)