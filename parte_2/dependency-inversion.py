class LuzBombilla:
    def encendido(self):
        print("LuzBombilla: turned on...")

    def apagado(self):
        print("LuzBombilla: turned off...")


class InterruptorElectrico:

    def __init__(self, l: LuzBombilla):
        self.LuzBombilla = l
        self.on = False

    def press(self):
        if self.on:
            self.LuzBombilla.apagado()
            self.on = False
        else:
            self.LuzBombilla.encendido()
            self.on = True


l = LuzBombilla()
switch = InterruptorElectrico(l)
switch.press()
switch.press()