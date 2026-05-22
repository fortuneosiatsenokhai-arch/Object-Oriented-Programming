class Vehicle:
    def __init__(self,name,company,speed,color):
        #instantiating
        self.name=name
        self.company=company
        self.speed=speed
        self.color=color

    def display(self):
            print(f"Name:{self.name}\nCompany:{self.company}\nSpeed:{self.speed}\nColor:{self.color}")

vehicle1=Vehicle("Range Rover","Land Rover","200km/h","Black")
vehicle1.display()
Vehicle2=Vehicle("Veiron","Bughati","400km/h","yellow")
Vehicle2.display()
Vehicle3=Vehicle("Lamborghini","Automobili Lamborghini S.p.A.","355km/h","red")
Vehicle3.display()