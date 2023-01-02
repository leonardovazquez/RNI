#-----------------------------------------

#    Save Data bases

#-----------------------------------------

#     Libraries
from datetime import datetime

def save_csv(ant,med1,med2):
    now = datetime.now()
    fecha = str(now.day) + "_" + str(now.month) + "_" + str(now.year)
    aux2 = ["Antenas_","Mediciones1_","Mediciones2_",".csv"]
    for i in range(0,3):
        aux2[i] = aux2[i] + fecha + aux2[3]
    ant.to_csv('database/'+aux2[0])
    med1.to_csv('database/'+aux2[1])
    med2.to_csv('database/'+aux2[2])


