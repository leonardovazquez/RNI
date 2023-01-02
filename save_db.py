#-----------------------------------------

#    Save Data bases

#-----------------------------------------

#     Libraries

from datetime import datetime
now = datetime.now()
fecha = str(now.day) + "_" + str(now.month) + "_" + str(now.year)

aux2 = ["Antenas_","Mediciones1_","Mediciones2_",".csv"]
for i in range(0,3):
    aux2[i] = aux2[i] + fecha + aux2[3]
    
Antenas.to_csv(aux2[0])
Mediciones1.to_csv(aux2[1])
Mediciones2.to_csv(aux2[2])