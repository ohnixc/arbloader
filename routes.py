import os

from flask import render_template, request, send_from_directory
from app import app
from form import LoginForm


@app.route('/')
@app.route('/index')
def hello_world():
    user = {'name': "Hank"}
    files = list_download('./')
    return render_template('arbdl.html', title="Home Page", user=user, files=files)


@app.route("/arbdl/d")
def login():
    form = LoginForm()
    return render_template('arbdl-download-result.html', form=form)


@app.route("/arbdl/list")
def login():
    form = LoginForm()
    return render_template('arbdl-list.html', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


def list_download(path):
    files = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)) is True:
            files.append(file)
    return files


