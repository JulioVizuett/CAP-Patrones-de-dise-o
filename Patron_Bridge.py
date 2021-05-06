# Passenger & Cargo Carriers

class Carrier:
    def carry_military(self, items):
        pass
    
    def carry_commercial(self, items):
        pass
    
# Son hijos de carrier

class Cargo(Carrier):
    def carry_military(self, items):
        print("The plane carries ", items," military cargo goods")
        
    def carry_commercial(self, items):
        print("The plane carries ", items," commercial cargo goods") 

class Passenger(Carrier):
    def carry_military(self, passengers):
        print("The plane carries ",  passengers , " military passengers")
        
    def carry_commercial(self, passengers):
        print("The plane carries ",  passengers , " commercial passengers") 

# Military & Commercial Planes
class Plane:
    def __init__(self, Carrier):
        self.carrier = Carrier
        
    def display_description(self):
        pass
    
    def add_objects(self):
        pass
    
class Commercial(Plane):
    def __init__(self, Carrier, objects):
        super().__init__(Carrier)
        self.objects = objects

    def display_description(self):
        self.carrier.carry_commercial(self.objects)

    def add_objects(self, new_objects):
        self.objects += new_objects   

class Military(Plane):
    def __init__(self, Carrier, objects):
        super().__init__(Carrier)
        self.objects = objects

    def display_description(self):
        self.carrier.carry_military(self.objects)

    def add_objects(self, new_objects):
        self.objects += new_objects

if __name__ == "__main__":
    """
    The client code should be able to work with any pre-configured abstraction-
    implementation combination.
    """
    cargo = Cargo()
    passenger = Passenger()
    
    # Se hace un bridge entre las clases Military y Cargo
    military1 = Military(cargo , 100)
    military1.display_description()

    # Se añaden 25 pasajeros más y muestra otro mensaje
    print("Se han sumado 25 pasajeros más")
    military1.add_objects(25)
    military1.display_description()

    print("\n")
    
    #cargo = Cargo()
    #passenger = Passenger()

    # Se hace un bridge entre las clases Military y Passenger
    military2 = Military(passenger , 250)
    military2.display_description()
    # Se añaden 10 pasajeros más y muestra otro mensaje
    print("Se han sumado 25 pasajeros más")
    military2.add_objects(10)
    military2.display_description()    
    