#Importing the modules to interact with the operating system
import sys
import os

if sys.version_info[0] < 3:
    raise Exception('Python 3 or a more recent version is required.')

import youtube_dl

home = os.path.expanduser('~')

full_path = {
    'format':'bestvideo[height<=360]+bestaudio/best[height<=360]',
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',
    }],
    'outtmpl': os.path.join(home, 'Desktop/yt-dl/Downloads', '%(title)s.%(ext)s'),
    }

while True:
    def file_dl():
        file_path = os.path.join(home, 'Desktop/yt-dl/Downloads')
        return file_path

    usr_input = input('\nURL to download: ')
    youtube_dl.YoutubeDL(full_path).download([usr_input])



    print('\nSuccess!! Huzzah!')
    print('\nVideo is saved at: {}'.format(file_dl()))
    usr_input = input('\nWant another? [y/n]: ')
    if usr_input == 'Y' or usr_input == 'y':
        print('\nAlright coo cool..')
        continue
    else:
        print('\nWell.. whatever then. Byeee')
        sys.exit()
