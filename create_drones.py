#In this i Build Multip-le Drones 

from drone.drone import Drone



drones = [

    Drone((0, 0)),
    Drone((5, 2)),
    Drone((10, 8))

]

for drone in drones:

    print(drone.get_state())