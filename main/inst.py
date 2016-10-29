import os
import time
from zipfile import *

python = os.path.isfile('/usr/bin/python3')
if python:
    try:
        os.system('pip3 install wget')
    finally:
        import wget

# UNIX ~ shortcut
global HOMe

HOMe = os.path.expanduser('~')


def installer():
    checkdir = bool(os.path.isdir('/Sweet-pepr'))

    if checkdir:
        os.rmdir(HOMe + '/Sweet-pepr')
        os.mkdir(HOMe + '/Sweet-pepr')
    else:
        pass

    print('Downloading Packages from Github')
    wget.download('https://github.com/oskar123e/Sweet-pepr/archive/master.zip', HOMe + '/master.zip')
    time.sleep(2)
    zipfile = (HOMe + '/master.zip')
    print('extracting files,')
    zip_archive = ZipFile(zipfile)
    zip_archive.extractall(HOMe + '/Sweet-pepr')
    zip_archive.close()
    time.sleep(2)
    print('cleaning up')
    os.remove(HOMe + '/Sweet-pepr/Sweet-pepr-master/main/inst.py')
    os.system('rm -r ~/Sweet-pepr/Sweet-pepr-master/.idea')

    print('installer finished')

installer()
