#Ro_pag83_ex1

from math import *

dies = int(input("Digues els dies = "))

anys =  (dies / 365)
mesos = (anys % 30)
residu_dies = (dies %  365) % 30

print ("anys = ",anys)
print ("mesos = ",mesos)
print ("dies = ",residu_dies)