import os
import wget




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
    wget.download('https://github.com/oskar123e/icons/archive/master.zip', )

installer()
