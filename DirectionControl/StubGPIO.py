

def setmode():
    return "mode"
    
class StubGPIO():
    @staticmethod
    def setmode():
        return "mode"

    @property
    def BCM(self):
        return "hi"
