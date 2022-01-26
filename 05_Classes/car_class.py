class Car:
    def __init__(self, max_speed=0):
        self.max_speed = max_speed
        self.speed = 0

    def accelerate(self, increase):
        self.speed = min(self.max_speed, self.speed + increase)

    def brake(self, decrease):
        minimum_speed = 0
        self.speed = max(minimum_speed, self.speed - decrease)


if __name__ == "__main__":
    Nissan = Car(200)
    print(Nissan.speed)
    print(Nissan.max_speed)
    Nissan.accelerate(150)
    print(Nissan.speed)
    Nissan.brake(100)
    print(Nissan.speed)
