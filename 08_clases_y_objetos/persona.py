class Persona(object):
  def __init__(self, name):
    self.name = name
  
  def saluda(self):
    print("Hola " + self.name)

  def despidete(self):
    print("Adios " + self.name)

p = Persona("Ana")
p.saluda()
p.despidete()

c = Persona("Jessica")
c.saluda()
c.despidete()

