class Robot:
    def __init__(self, name):
        self.__name = name
        self.__battery = 100
        self.__x = 0
        self.__y = 0

    def recharge(self):
        if self.__battery == 100:
            print(f"El robot {self.__name} ya esta cargado al 100%")
        else:
            self.__battery = 100
            print(f"Robot {self.__name} cargado al 100%")

    def _move_axis(self, axis):
        if axis == 'x':
            self.__x += 1
            self.__battery -=10
            print(f"({self.__x},{self.__y})")
        elif axis == 'y':
            self.__y += 1
            self.__battery -=10
            print(f"({self.__x},{self.__y})")

    def move(self, dx, dy):
        print(f"\nEl robot {self.__name} se empezara a mover (x, y)")

        print("Eje x:")
        for _ in range(dx):
            if self.__battery - 10 > 0: 
                self._move_axis('x')
            else:
                print(f"Insuficiente energia para moverse en el eje x")
                break

        print("Eje y:")
        for _ in range(dy):
            if self.__battery - 10 > 0: 
                self._move_axis('y')
            else:
                print(f"Insuficiente energia para moverse en el eje y")
                break

    # Getter methods
    def get_name(self):
        return self.__name

    def get_battery(self):
        return self.__battery

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_position(self):
        return f"({self.__x}, {self.__y})"

    # Setter methods
    def _set_battery(self, value):
        self.__battery += value

    def _set_x(self, x):
        if x > 0:
            self.__x += x
        else:
            self.__x -= x

    def _set_y(self, y):
        if y > 0:
            self.__y += y
        else:
            self.__y -= y

    def __str__(self):
        return f"Robot {self.__name}:\n  posición ({self.__x},{self.__y})\n  batería {self.__battery}%"

class RobotExplorador(Robot):
    pass

class RobotCarguero(Robot):
    def __init__(self, name):
        super().__init__(name)
        # Nuevo atributo privado
        self.__load = 0

    # Solo acepta coordenadas positivas
    def move(self, dx, dy):
        if self.__load > 0:
            print("\nSe empezara a mover el robot " + super().get_name())

            print("Eje x:")
            for _ in range(dx):
                if super().get_battery() - 10 > 20:
                    self._move_axis('x')
                else:
                    print(f"Energia insuficiente para mover({self.__load} kg) carga en el eje x")
                    break

            print("Eje y:")
            for _ in range(dy):
                if super().get_battery() - 10 > 20:
                    self._move_axis('y')
                else:
                    print(f"Energia insuficiente para mover({self.__load} kg) carga en el eje y")
                    break
        else:
            super().move(dx, dy)

    def _set_load(self, kg):
        self.__load += kg
        print(f"Carga exitosamente añadida al Robot {super().get_name()}. Carga: {self.__load} kg")
    
    def __str__(self):
        return super().__str__() + f"\n  Carga: {self.__load} kg"

# Creación de robots!
robot1 = Robot("Alexa")
robot2 = Robot("YO")
robot3 = RobotExplorador("Wall-E")
robot4 = RobotExplorador("Eva")
robot5 = RobotCarguero("Optimus")
robot6 = RobotCarguero("Megatron")

list = [robot1, robot2, robot3, robot4, robot5, robot6]

for r in list:
    print(r)

for r in list:
    r.move(4,5)

for r in list:
    r.recharge()

list[4]._set_load(5)
list[5]._set_load(5)

for r in list:
    r.move(6,5)

for r in list:
    print(r)