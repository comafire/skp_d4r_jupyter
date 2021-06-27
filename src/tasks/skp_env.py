import os, sys, json, re
from pprint import pprint

# SKP
SKP_USER = os.environ["SKP_USER"]
SKP_USERID = os.environ["SKP_USERID"]
SKP_HOME = os.environ["SKP_HOME"]

# LOCALE
LOCALE = os.environ["LOCALE"]

# JUPYTER
try:
    JUPYTER_HOME = os.environ["JUPYTER_HOME"]
    JUPYTER_NAME = os.environ["JUPYTER_NAME"]
    JUPYTER_IMAGE = os.environ["JUPYTER_IMAGE"]
    JUPYTER_GPU = os.environ["JUPYTER_GPU"]
    JUPYTER = True
except:
    JUPYTER = False



