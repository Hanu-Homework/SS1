def calculate_distance(speed: float, time: float) -> float:
    return speed * time


SPEED = 70
for hour in [6, 10, 15]:
    print(f"The distance the car will travel in {hour} hours: {calculate_distance(SPEED, hour)}")
