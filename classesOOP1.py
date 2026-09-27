class Vehicle:
    def __init__(self, mdl, spd):
        self._model = mdl
        self.__speed = spd

    def SetSpeed(self, s):
        self.__speed = s

    def GetSpeed(self):
        return self.__speed

class Car(Vehicle):
    def __init__(self, mdl, spd, brand):
        super().__init__(mdl, spd)
        self.__brand = brand
    
    def GetModel(self):
        return self._model
    
    def GetBrand(self):
        return self.__brand
    
    def GetSpeed(self):
        return super().GetSpeed()

    def SetModel(self, mdl):
        self._model = mdl

    def SetBrand(self, brand):
        self.__brand = brand

car1 = Car(2021, 90, "Toyota")

endloop = False

while endloop == False:
    msg = str(input("Enter the command you want to use. | "))

    if(msg == "GetSpeed"):
        print(car1.GetSpeed())
    elif(msg == "GetModel"):
        print(car1.GetModel())
    elif(msg == "GetBrand"):
        print(car1.GetBrand())
    elif(msg == "SetSpeed"):
        car1.SetSpeed(int(input("Enter your desired speed. | ")))
    elif(msg == "SetModel"):
        car1.SetModel(int(input("Enter your car's model. | ")))
    elif(msg == "SetBrand"):
        car1.SetBrand(str(input("Enter your car's brand. | ")))
    elif(msg == "End"):
        endloop = True
    else:
        print("Enter a Valid Query.")