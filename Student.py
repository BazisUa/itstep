import random

class student:
    print("Hi, I'm a student")
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 0
        self.alive = True

    def to_study(self):
        print("time to study")
        self.progress += 0.12
        self.gladness -= 3
    def to_sleep(self):
        print("time to sleep")
        self.gladness += 3
    def to_chill(self):
        print("time to rest")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 1
        print("money =", self.money)
    def to_work(self):
        print("time to work")
        self.progress += 2
        self.gladness -= 2
        self.money += 5
        print("money =", self.money)
    def is_alive(self):
        if self.progress < -5:
            print("Cast out")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally...")
            self.alive = False
        elif self.money < -10:
            print("You are bankrupt!")
            self.alive = False

    def end_of_day(self):
        print(f"gladless = {self.gladness}")
        print(f"progress = {round(self.progress)}")

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_work()

        self.end_of_day()
        self.is_alive()

nick = student("Nick")

for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)

