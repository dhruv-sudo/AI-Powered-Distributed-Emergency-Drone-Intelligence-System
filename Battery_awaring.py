def can_complete_route(
    drone_battery,
    route_distance
):

    battery_required = route_distance * 2

    return drone_battery >= battery_required