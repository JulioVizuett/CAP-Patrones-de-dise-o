from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):
    """
    The Command interface declares a method for executing a command.
    """

    @abstractmethod
    def execute(self) -> None:
        pass


class SimpleCommand(Command):
    """
    Some commands can implement simple operations on their own.
    """

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"Pedido 1: Yo quiero una orden de: "
              f"({self._payload})")


class ComplexCommand(Command):
    """
    However, some commands can delegate more complex operations to other
    objects, called "receivers."
    """

    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        """
        Complex commands can accept one or several receiver objects along with
        any context data via the constructor.
        """

        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        """
        Commands can delegate to any methods of a receiver.
        """

        print("Pedido 2: yo quiero un cafe y huevo revuelto", end="")
        self._receiver.PreparandoCafe(self._a)
        self._receiver.PreparandoHuevos(self._b)

# Quise ver al receiver como el chef
class Receiver:
    """
    The Receiver classes contain some important business logic. They know how to
    perform all kinds of operations, associated with carrying out a request. In
    fact, any class may serve as a Receiver.
    """

    def PreparandoCafe(self, a: str) -> None:
        print(f"\nCocinero: Estoy preparando ({a}.)", end="")

    def PreparandoHuevos(self, b: str) -> None:
        print(f"\nCocinero: También estoy cocinando: ({b}.)", end="")


class Invoker:
    """
    The Invoker is associated with one or several commands. It sends a request
    to the command.
    """

    _on_start = None
    _on_finish = None

    """
    Initialize commands.
    """

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def Orden_enPared(self) -> None:
        """
        The Invoker does not depend on concrete command or receiver classes. The
        Invoker passes a request to a receiver indirectly, by executing a
        command.
        """

        print("Pedido en pared: El cocinero aun no finaliza el anterior, espere")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("...pedidos grandes y complejos en producción...")

        print("Pedido en pared: El cocinero esta por finalizar los platillos anteriores")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == "__main__":
    """
    The client code can parameterize an invoker with any commands.
    """

    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Enchiladas"))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(
        receiver, "Café", "Huevos"))

    invoker.Orden_enPared()