import time

def move_drone(
    drone,
    path_coordinates
):

    for coordinate in path_coordinates:

        drone.update_position(coordinate)

        drone.drain_battery(2)

        print(

            f"Drone Position: {drone.position}"

        )

        print(

            f"Battery: {drone.battery}"

        )

        time.sleep(1)