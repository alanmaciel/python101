import random

class Dado(object):
  def arrojar(self):
    print("El dado arroja: " +str(random.randint(1,6)))

dado1 = Dado()
dado2 = Dado()

dado1.arrojar()
dado2.arrojar()