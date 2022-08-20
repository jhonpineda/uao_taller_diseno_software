from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def encendido(self):
        pass

    @abstractmethod
    def apagado(self):
        pass


class LuzBombilla(Switchable):
    def encendido(self):
        print("LuzBombilla: turned on...")

    def apagado(self):
        print("LuzBombilla: turned off...")


class Ventilador(Switchable):
    def encendido(self):
        print("Ventilador: turned on...")

    def apagado(self):
        print("Ventilador: turned off...")


class InterruptorElectrico:

    def __init__(self, c: Switchable):
        self.cliente = c
        self.on = False

    def press(self):
        if self.on:
            self.cliente.apagado()
            self.on = False
        else:
            self.cliente.encendido()
            self.on = True


l = LuzBombilla()
f = Ventilador()
switch = InterruptorElectrico(f)
switch.press()
switch.press()