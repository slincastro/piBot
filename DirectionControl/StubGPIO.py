
class StubGPIO():
    def setmode(self):
        return "mode"

    @property
    def BCM(self):
        return "hi"
