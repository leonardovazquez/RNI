#-----------------------------------------

#     Main Programm

#-----------------------------------------

#     Libraries
from pykml import parser
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib, matplotlib_inline
# matplotlib inline

#    Local Methods

from kml_data_extractor import data_upload, send_dataframes

#     Upload File
filename='RNI.kml'
with open(filename) as f:
    folder = parser.parse(f).getroot().Document.Folder
db = data_upload(folder)

#     Dataframes definitions
Antenas     = pd.DataFrame()
Mediciones1 = pd.DataFrame()
Mediciones2 = pd.DataFrame()

#     Dataframes uploads
Antenas     = send_dataframes(0,db)
Mediciones1 = send_dataframes(1,db)
Mediciones2 = send_dataframes(2,db)
