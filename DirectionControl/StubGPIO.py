
class StubGPIO():
    def setmode(self,mode):
        return "none"

    @property
    def BCM(self):
        return "none"
