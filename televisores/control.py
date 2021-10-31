class Control:
    def __init__(self):
        self.tv = None

    def turnOn(self):
        self.tv._estado = True

    def turnOff(self):
        self.tv._estado = False

    def setCanal(self,canal):
        if (self.tv._estado == True and canal>= 1 and canal<=120):
            self.tv._canal = canal    


    def canalUp(self):
        if (self.tv._estado == True and self.tv._canal<120):
            self.tv._canal += 1 

    def canalDown(self):
        if (self.tv._estado == True and self.tv._canal>1):
            self.tv._canal -= 1 

    def volumenUp(self):
        if (self.tv._estado == True and self.tv._volumen<7):
            self.tv._volumen += 1

    def volumenDown(self):
        if (self.tv._estado == True and self.tv._volumen>1):
            self.tv._volumen -= 1    

    def enlazar(self,tv):
        self.tv = tv
        self.tv._control = self

    def getTv(self):
        return self.tv 
    def setTv(self,tv):
        self.tv = tv