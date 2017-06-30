
class StubGPIO():
    @staticmethod
    def setmode(mode):
        return "mode"

    @property
    def BCM(self):
        return "hi"
