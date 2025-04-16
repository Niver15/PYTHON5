#assignment 1
#Base Class:Smartphone
class Smartphone:
    def__init__(self,brand,model,color):
        self.brand= brand
        self.model=model
        self.color=color

        def call(self, number):
            print(f"{self.brand} {self.model} is calling{number}...")

            def info(self):
                print(f"brand: {self.brand},model:{self.model},color:{self.color}")

                #subclass:GamingPhone(inheritance example)
                class GamingPhone(Smartphone):
                    def__init__(self, brand, model, color,cooling sytem):
                        super().__init__(brand, model, color)
                        self.cooling system=
                        cooling system

                        def play_game(self, game):
                        print(f"{self.brand} {self.model} is playing{game} with
                        {self.cooling_system} cooling system!")

                        #creating objects using constructors
                        phone1=Smartphone("Samsung", "Galaxy A23",128, "black")
                        phone2=GamingPhone("techno","spark 4", 256, "liquid cooling")

                        #using methods
                        phone1.info()
                        phone1.call("0711910858")

                        phone2.info()
                        phone2.play_game("PUBG Mobile")


#activity 2
#base class
class Vehicle:
    def move(self):
        print("Vehicle is moving")

#subclass:Car
class car(Vehicle):
    def move(self):
        print("driving on the road")

        #subclass:Plane
        class plane(Vehicle):
            def move(self)
            print("Flying in the sky")

            #subclass:Boat
            class boat(Vehicle):
                def move(self):
                    print("sailing on water")

                    #create objects
                    my_car=Car()
                    my_plane=Plane()
                    my_boat=Boat()


                    #polymorphism in action
                    vehicles=[my_car, my_plane, my_boat]

                    for vehicle in vehicle:
                        vehicle.move()