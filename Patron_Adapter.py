# Emular un cargador europeo en estados unidos (se necesita un adaptador para que funcione)

class EuropeanSocketInterface:
    def voltage(self): pass

    def live(self): pass
    def neutral(self): pass
    def earth(self): pass

# Adaptee
class Socket(EuropeanSocketInterface):

    """
    The Adaptee contains some useful behavior, but its interface is incompatible
    with the existing client code. The Adaptee needs some adaptation before the
    client code can use it.
    """

    def voltage(self):
        return 230

    def live(self):
        return 1
   
    def neutral(self):
        return -1
   
    def earth(self):
        return 0

# Target interface
class USASocketInterface:

    """
    The Target defines the domain-specific interface used by the client code.
    """

    def voltage(self): pass
    def live(self): pass
    def neutral(self): pass

# The Adapter
class Adapter(USASocketInterface):
    __socket = None
    def __init__(self, socket):
        self.__socket = socket
   
    def voltage(self):
        return 110
   
    def live(self):
        return self.__socket.live()
   
    def neutral(self):
        return self.__socket.neutral()

# Client
class ElectricKettle:
   __power = None
   
   def __init__(self, power):
	   self.__power = power
   
   def boil(self):
      if self.__power.voltage() > 110:
         print ("Sin usar el adaptador: Kettle on fire!")
      else:
         if self.__power.live() == 1 and \
            self.__power.neutral() == -1:
            print ("Utilizando el adaptador: Coffee time!")
         else:
            print ("No power.")

def main():
   # Plug in
   socket = Socket()
   adapter = Adapter(socket)
   kettle = ElectricKettle(adapter)
   # Se manda a llamar sin el adaptador
   kettle2 = ElectricKettle(socket)
	
   # Make coffee
   kettle.boil()

   # Kettle on fire! No se utiliza el adaptador
   kettle2.boil()
	
   return 0
	
if __name__ == "__main__":
   main()