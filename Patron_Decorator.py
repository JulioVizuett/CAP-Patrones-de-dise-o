class Forma():
    """
    The base Forma interface defines operations that can be altered by
    decorators.
    """

    def operation(self) -> str:
        pass


class Circulo(Forma):
    """
    Concrete Formas provide default implementations of the operations. There
    might be several variations of these classes.
    """

    def operation(self) -> str:
        return "Circulo"


class Decorator(Forma):
    """
    The base Decorator class follows the same interface as the other Formas.
    The primary purpose of this class is to define the wrapping interface for
    all concrete decorators. The default implementation of the wrapping code
    might include a field for storing a wrapped Forma and the means to
    initialize it.
    """

    _Forma: Forma = None

    def __init__(self, Forma: Forma) -> None:
        self._Forma = Forma

    @property
    def Forma(self) -> str:
        """
        The Decorator delegates all work to the wrapped Forma.
        """

        return self._Forma

    def operation(self) -> str:
        return self._Forma.operation()


class Rojo(Decorator):
    """
    Concrete Decorators call the wrapped object and alter its result in some
    way.
    """

    def operation(self) -> str:
        """
        Decorators may call parent implementation of the operation, instead of
        calling the wrapped object directly. This approach simplifies extension
        of decorator classes.
        """
        return f"Rojo({self.Forma.operation()})"


class Grande(Decorator):
    """
    Decorators can execute their behavior either before or after the call to a
    wrapped object.
    """

    def operation(self) -> str:
        return f"Grande({self.Forma.operation()})"


def client_code(Forma: Forma) -> None:
    """
    The client code works with all objects using the Forma interface. This
    way it can stay independent of the concrete classes of Formas it works
    with.
    """

    # ...

    print(f"RESULT: {Forma.operation()}", end="")

    # ...


if __name__ == "__main__":
    # This way the client code can support both simple Formas...
    simple = Circulo()
    print("Client: I've got a simple Forma:")
    client_code(simple)
    print("\n")

    # ...as well as decorated ones.
    #
    # Note how decorators can wrap not only simple Formas but the other
    # decorators as well.
    decorator1 = Rojo(simple)
    decorator2 = Grande(decorator1)
    print("Client: Now I've got a decorated Forma:")
    client_code(decorator2)