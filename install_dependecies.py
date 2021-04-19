import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'nltk'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'pandas'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'matplotlib'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'easygui'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'xlwt']) 
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'tk'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'pandastable'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'openpyxl'])
from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory
import pandas as pd
from pandastable import Table
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import nltk
import re
nltk.download('stopwords')

