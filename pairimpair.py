import shutil
from random import *
rdm_opt = 2
tour = 0
nm1 = 0
loop = 10000000000-1

n = 10000000000
n1 = n
print(f"La premiere donne est {n}")
while n != 1:
 if (n % 2) == 0:
   print("{0} est Paire".format(n))
   n = n/2
   tour = tour+1
 else:
   print("{0} est Impaire".format(n))
   n = n*3+1
   tour = tour+1
 print(f"{n} avec {tour} tour.")
 if n > nm1:
    nm1 = n
    print(f"point culminant = {nm1}")
 else:
    print(f"point culminant = {nm1}")

print(f"la suite est arriver a la boucle en {tour}")
print(f"Le point culminant est de {nm1}")
file = open(f"{n1}.txt", "w") 
file.write(f"La premiere valeur est {n1} ,la suite est arriver a la boucle en {tour} tour et Le point culminant est de {nm1}") 
file.close()

while loop != 0:
 n = n1 - 1
 n1 = n
 print(f"La premiere donne est {n}")
 while n != 1:
  if (n % 2) == 0:
    print("{0} est Paire".format(n))
    n = n/2
    tour = tour+1
  else:
    print("{0} est Impaire".format(n))
    n = n*3+1
    tour = tour+1
  print(f"{n} avec {tour} tour.")
  if n > nm1:
     nm1 = n
     print(f"point culminant = {nm1}")
  else:
     print(f"point culminant = {nm1}")

 print(f"la suite est arriver a la boucle en {tour}")
 print(f"Le point culminant est de {nm1}")
 file = open(f"{n1}.txt", "w") 
 file.write(f"La premiere valeur est {n1} ,la suite est arriver a la boucle en {tour} tour et Le point culminant est de {nm1}") 
 file.close()
 loop = loop-1