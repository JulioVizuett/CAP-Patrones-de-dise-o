class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        # Lo probé quitando el if y solamente generando nuevas instancias y funcionó correctamente
        """instance = super().__call__(*args, **kwargs)
        cls._instances[cls] = instance
        return cls._instances[cls]"""

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """

        print("Hola me llamo Julio, si ambas instancias son iguales este mensaje aparecerá en la consola")
        print("También sé como sumar, 2 + 3 = {}".format(2 + 3))

        # ...


if __name__ == "__main__":
    # The client code.

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
        s1.some_business_logic()
    else:
        print("Singleton failed, variables contain different instances.")