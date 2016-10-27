import os
import time
import wget
from zipfile import *

global home
home = os.path.expanduser('~')


def installer():
    checkDir = bool(os.path.isdir('/Sweet-pepr'))

    if checkDir == True:
        os.rmdir(home + '/Sweet-pepr')
        os.mkdir(home + '/Sweet-pepr')
    else:
        pass

    print('Downloading Packages from Github')
    wget.download('https://github.com/oskar123e/icons/archive/master.zip', home + '/master.zip')
    time.sleep(5)
    zipfile = (home + '/master.zip')
    print('extracting files,')
    zip_archive = ZipFile(zipfile)
    zip_archive.extractall(home + '/Sweet-pepr')
    zip_archive.close()
    time.sleep(5)
    print('cleaning up')
    os.remove(home + '/Sweet-pepr/icons-master/main/install.py')
    os.system('rm -r ~/Sweet-pepr/icons-master/.idea')
    os.remove(home + '/Sweet-pepr/icons-master/tab.svg')
    print('installer finished')
installer()
