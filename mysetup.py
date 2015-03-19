from distutils.core import setup
import py2exe

import sys


sys.argv.append("py2exe")#allow a simple double click to execute

options={"py2exe":{"bundle_files":1}#only one exe
         }

setup(
    options=options,
    name="NewsDownload",
    version="1.0",
    zipfile =None,#no library zip
    #console or window
    console=[{"script":"NewsDownload.py", "icon_resources":[(0,"128.ico")]}]#add a logo ico
    )
