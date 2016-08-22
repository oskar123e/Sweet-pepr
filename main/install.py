import os
import urllib

home = os.path.expanduser('~')


def installer():
    checkDir = os.path.isdir('Sweet-pepr')

    if checkDir == True:
        try:
            os.mkdir('/sweet-peper')
        except:
            pass

        else:
            os.mkdir(home + '/Sweet-pepr')
    urllib.urlretrieve("http://", ".")


installer()
