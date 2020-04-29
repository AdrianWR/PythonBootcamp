import time
from random import randint


class CoffeeMachine():
    water_level = 100

    def log(func):
        def wrapper(self, *args, **kwargs):
            log_file = open("machine.log", "a")
            process = self.__current_process(func)
            start_time = time.time()
            result = func(self, *args, **kwargs)
            ex_time = time.time() - start_time
            time_scale = "s"
            if ex_time < 0.001:
                ex_time *= 1000
                time_scale = "ms"
            log_file.write(f"(aroque)Running: {process}\t")
            log_file.write(f"[ exec-time = {ex_time:.3f} {time_scale}\t]\n")
            return result
        return wrapper

    @staticmethod
    def __current_process(func):
        name = func.__name__
        name = [i.capitalize() for i in name.split("_")]
        name = " ".join(name)
        return name

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)
