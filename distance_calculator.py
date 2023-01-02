import math
import numpy as np
from numpy import pi, round

def deg2rad(degrees):
    radians = degrees * pi / 180
    return radians

def distancia_r(a,m):
    global Antenas, Mediciones1
    lat1 = float(Mediciones1["Latitude"][m])
    lon1 = float(Mediciones1["Longitude"][m])
    lat2 = float(Antenas["Latitude"][a])
    lon2 = float(Antenas["Longitude"][a])
    h    = float(Antenas["altura"][a])   
    R    = 6367*1000 # Radio de la tierra
    a    = math.sin(deg2rad(lat1)) * math.sin(deg2rad(lat2))
    b    = math.cos(deg2rad(lat1)) * math.cos(deg2rad(lat2)) * math.cos(deg2rad(lon2 - lon1))
    c    = math.acos(a + b)
    d    = R * c   
    r    = np.sqrt(d**2 + h**2)
    return round(r)

def area(rm):
    rcm = rm/100  # m a cm
    return 4 * pi * (rcm**2)