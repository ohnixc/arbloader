import os
from collections import ChainMap
from threading import Thread
from urllib.parse import quote

from app import app
from flask import render_template, request, jsonify, make_response, send_from_directory, redirect, url_for
from queue import Queue
import youtube_dl

app_defaults = {
    'arbdl_FORMAT': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
    'arbdl_EXTRACT_AUDIO_FORMAT': None,
    'arbdl_EXTRACT_AUDIO_QUALITY': '192',
    'arbdl_RECODE_VIDEO_FORMAT': None,
    'arbdl_OUTPUT_TEMPLATE': './completed/%(title)s [%(id)s].%(ext)s',
    'arbdl_ARCHIVE_FILE': None,
}


def dl_worker():
    while not done:
        url, options = dl_q.get()
        download(url, options)
        dl_q.task_done()


dl_q = Queue()
done = False
dl_thread = Thread(target=dl_worker)
dl_thread.start()


@app.route('/arbdl-list')
def file_list():
    files = list_download('./completed/')
    print(files)
    return render_template("arbdl-list.html", files=files)


@app.route('/download/<path:path>')
def file_download(path):
    response = make_response(send_from_directory('./completed', path))
    response.headers["Content-Disposition"] = "attachment; filename={0}; filename*=utf-8''{0}".format(quote(path))
    return response


@app.route('/')
def arbdl():
    return render_template('index.html')


@app.route('/arbdl/d', methods=["POST"])
def arbdl_download():
    url = request.form["url"]
    options = {
        'format': request.form.get("format")
    }

    if not url:
        result = '''LERN2URL'''
    else:
        result = '''SICKBEANZ.'''  
        dl_q.put((url, options))
    return render_template("arbdl-download-result.html", result=result)


@app.route('/arbdl/delete', methods=["POST"])
def arbdl_delete():
    file = "./completed" + request.form["file"]
    if os.path.exists(file):
        os.remove(file)
    print(file)
    return redirect(url_for("file_list"))


def list_download(path):
    files = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)) is True:
            files.append(file)
    return files


def dl_worker():
    while not done:
        url, options = dl_q.get()
        download(url, options)
        dl_q.task_done()


def get_arbdl_options(request_options):
    request_vars = {
        'arbdl_EXTRACT_AUDIO_FORMAT': None,
        'arbdl_RECODE_VIDEO_FORMAT': None,
    }

    requested_format = request_options.get('format', 'bestvideo')

    postprocessors = []
    
    arbdl_vars = ChainMap(request_vars, os.environ, app_defaults)

    if (arbdl_vars['arbdl_EXTRACT_AUDIO_FORMAT']):
        postprocessors.append({
            'key': 'FFmpegExtractAudio',
            'preferredcodec': arbdl_vars['arbdl_EXTRACT_AUDIO_FORMAT'],
            'preferredquality': arbdl_vars['arbdl_EXTRACT_AUDIO_QUALITY'],
        })

    if (arbdl_vars['arbdl_RECODE_VIDEO_FORMAT']):
        postprocessors.append({
            'key': 'FFmpegVideoConvertor',
            'preferedformat': arbdl_vars['arbdl_RECODE_VIDEO_FORMAT'],
        })

    return {
        # 'proxy': 'http://127.0.0.1:1087',
        'format': arbdl_vars['arbdl_FORMAT'],
        'postprocessors': postprocessors,
        'outtmpl': arbdl_vars['arbdl_OUTPUT_TEMPLATE'],
        'download_archive': arbdl_vars['arbdl_ARCHIVE_FILE']
    }


def download(url, request_options):
    try:
        with youtube_dl.YoutubeDL(get_arbdl_options(request_options)) as arbdl:
            arbdl.download([url])
    except:
        pass
