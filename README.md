

# ARBLOAD

A badass webapp based on <a href="https://github.com/ytdl-org/youtube-dl">youtube-dl</a>

## Get it
```
git clone https://github.com/ohnixc/arbloader.git
cd arbloader
```

## Load it

```
python3 -m venv loadenv
source loadenv/bin/activate
pip install -r requirements.txt
FLASKAPP=app.py
flask run --host=0.0.0.0 --port=5000
```


## Use it
* Connect on <i>port 5000</i> using your local IP 

    ```
    http://127.0.0.1:5000/ 
    ```
* Enter URL (eg https://vimeo.com/xxxxxxx) into web page
* Completed downloads will load in the provided "Completed" folder 

*** Note: Videos can be downloaded from all [supported sites](https://ytdl-org.github.io/youtube-dl/supportedsites.html) 

## Props


* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Microservice Framework built for Python
* [Youtube-DL](https://github.com/ytdl-org/youtube-dl) - Python library to download videos from youtube (and more!)
* [Tachyons](https://tachyons.io/components/) - CSS framework for fast, responsive webpages


#### TODO

* Auto refresh upon completion
* Ansible playbook for NGINX/Jinja2 integration
* Deploy as standalone web application 

