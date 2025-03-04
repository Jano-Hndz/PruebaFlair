import random

class Sensor:
    # Estado inicial del sensor
    def __init__(self):
        self.state = "normal"  
    
    # Cambia el estado del sensor a alerta cuando hay zombis
    def alert(self):
        self.state = "alert"  
    
    # Restablece el estado a normal cuando no hay zombis
    def reset(self):
        self.state = "normal"  

class Room:

    def __init__(self, number):
        self.number = number  
        self.sensor = Sensor()
        self.zombies = False 
    
    #Activa el sensor y coloca un zombi en la pieza
    def add_zombie(self):
        self.zombies = True  
        self.sensor.alert()  
    
    #Resetea el sensor y remueve el zombi de esa pieza
    def remove_zombie(self):
        self.zombies = False 
        self.sensor.reset()  

class Floor:
    def __init__(self, number, rooms_per_floor):
        self.number = number  
        self.rooms = [Room(i) for i in range(rooms_per_floor)]  
        self.pending_spread = False 
    
    def get_room(self, number):
        if 0 <= number < len(self.rooms):
            return self.rooms[number]
        return None

    # Verifica si todas las habitaciones están infectadas
    def is_fully_infected(self):
        return all(room.zombies for room in self.rooms)  

class Building:

    def __init__(self, floors, rooms_per_floor):
        self.floors = [Floor(i, rooms_per_floor) for i in range(floors)] 
    
    def get_floor(self, number):
        if 0 <= number < len(self.floors):
            return self.floors[number]
        return None

class Simulation:

    def __init__(self):
        self.building = None
        self.first_zombie_spawned = False
    
    def configure_building(self, floors, rooms_per_floor):
        self.building = Building(floors, rooms_per_floor)  
        self.first_zombie_spawned = False 
    
    #Se coloca un zombi de manera random dentro del edificio
    def spawn_initial_zombie(self):
        if not self.first_zombie_spawned:
            floor_num = random.randint(0, len(self.building.floors) - 1)
            room_num = random.randint(0, len(self.building.floors[floor_num].rooms) - 1)
            self.building.get_floor(floor_num).get_room(room_num).add_zombie()
            self.first_zombie_spawned = True 
    
    def advance_turn(self):

        #Aviso que todavia no se ha creado el edifico
        if not self.building:
            print("Primero debe configurar el edificio.")
            return
        
        if not self.first_zombie_spawned:
            self.spawn_initial_zombie()
            return
        
        new_infections = []  
        
        # Marcar los pisos completamente infectados para propagar la infección, para así no tener que revisarlo otra vez
        for floor in self.building.floors:
            if floor.is_fully_infected():
                floor.pending_spread = True

        # Propagar la infección a los pisos adyacentes solo en una habitación inicial
        for i, floor in enumerate(self.building.floors):
            if floor.pending_spread:
                if i > 0:  
                    self.building.get_floor(i - 1).get_room(0).add_zombie()
                if i < len(self.building.floors) - 1:  
                    self.building.get_floor(i + 1).get_room(0).add_zombie()
                floor.pending_spread = False

        # Propagación de la infección dentro del mismo piso a habitaciones adyacentes
        for floor in self.building.floors:
            if not floor.is_fully_infected():  # Si el piso aún no está completamente infectado
                for room in floor.rooms:
                    if room.zombies:
                        adjacent_rooms = [room.number - 1, room.number + 1]  # Las dos piezas adyacente para infectar
                        for num in adjacent_rooms:
                            adj_room = floor.get_room(num)
                            if adj_room and not adj_room.zombies:
                                new_infections.append((floor.number, num))
        
        # Aplicar las nuevas infecciones
        for f, r in new_infections:
            self.building.get_floor(f).get_room(r).add_zombie()


    def display_status(self):
        """Muestra el estado actual del edificio indicando qué habitaciones están infectadas."""
        if self.building:
            for floor in reversed(self.building.floors): 
                status_line = f"Piso {floor.number}: " + " ".join(f"[{room.sensor.state}]" for room in floor.rooms)
                print(status_line)
        else:
            print("Primero debe configurar el edificio.")



# Menú de la simulación

def main():
    sim = Simulation()
    
    while True:
        print("\n1. Configurar edificio")
        print("2. Mostrar estado del edificio")
        print("3. Avanzar la simulación")
        print("4. Salir")
        
        choice = input("Seleccione una opción: ")
        
        if choice == "1":
            floors = int(input("Ingrese el número de pisos: "))
            rooms_per_floor = int(input("Ingrese el número de habitaciones por piso: "))
            sim.configure_building(floors, rooms_per_floor)
        elif choice == "2":
            sim.display_status()
        elif choice == "3":
            sim.advance_turn()
        elif choice == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
    
if __name__ == "__main__":
    main()
