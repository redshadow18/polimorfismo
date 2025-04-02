#creacion superclase animal
class Animal:
  def sonido (self):
    pass

class perro(Animal):
  def sonido(self):
    return "guau"


class gato(Animal):
  def sonido(self):
    return "miau"

def hacer_sonido(animal: Animal):
     print(animal.sonido())

perro=perro()
gato=gato()

hacer_sonido(perro)
hacer_sonido(gato)


