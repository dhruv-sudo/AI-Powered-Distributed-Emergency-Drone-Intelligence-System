import uuid
from typing import Tuple

class Drone:

    def __init__(
        self,
        position: Tuple[float, float]
    ):

        self.drone_id = str(uuid.uuid4())[:8]

        self.position = position

        self.battery = 100.0

        self.speed = 10

        self.status = "IDLE"

        self.current_mission = None

    def update_position(
        self,
        new_position: Tuple[float, float]
    ):

        self.position = new_position

    def drain_battery(self, amount: float):

        self.battery = max(0, self.battery - amount)

    def assign_mission(self, mission):

        self.current_mission = mission

        self.status = "ACTIVE"

    def complete_mission(self):

        self.current_mission = None

        self.status = "IDLE"

    def get_state(self):

        return {
            "drone_id": self.drone_id,
            "position": self.position,
            "battery": self.battery,
            "status": self.status
        }