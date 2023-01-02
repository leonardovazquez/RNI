#-----------------------------------------

#    KML Data Extractor

#-----------------------------------------

#  Libraries
import pandas as pd

#  Kml data extractor (local function)
def data_extractor(data):
    aux = ''
    for i in range(5):
        if data[i+5]=='<':
            break
        else:
            aux=aux+data[i+5]  
    return float(aux)

#   Data Upload 
def data_upload(folder):
    #global Ant, Med1, Med2
    aux =[[],[],[],[],[],[]]
    for pm in folder.Placemark:
        plnm1=str(pm.name)
        plcs1=str(pm.Point.coordinates)
        if plnm1.startswith('A',0) or plnm1.startswith('T',0):
            data=str(pm.description)
            aux[0].append(data_extractor(data))
            aux[1].append(plcs1)
        elif plnm1.startswith('M',0):
            data=str(pm.description)
            aux[2].append(data_extractor(data))
            aux[3].append(plcs1)
        elif plnm1.startswith('H',0):
            data=str(pm.description)
            aux[4].append(data_extractor(data))
            aux[5].append(plcs1)
    return aux 
        
#   Send Complete Dataframes

def send_dataframes(i,db):
    aux = pd.DataFrame()
    if i==0:
        aux['altura']      = db[0]
        aux['coordenadas'] = db[1]
    elif i==1:
        aux['densidad de potencia']      = db[2]
        aux['coordenadas'] = db[3]
    elif i==2:
        aux['densidad de potencia']      = db[4]
        aux['coordenadas'] = db[5]
    aux['Longitude'],aux['Latitude'],aux['value']=zip(*aux['coordenadas'].apply(lambda x: x.split(',',2)))
    return aux

