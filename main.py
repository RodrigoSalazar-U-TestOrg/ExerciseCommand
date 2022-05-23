from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class Light:
    def __init__(self, intensity=0):
        self.intensity = intensity

    def __str__(self):
        return "<LIGHT - Intensity:{}>".format(self.intensity)


class SetLightIntensity(Command):
    def __init__(self, light, intensity):
        self.light = light
        self.intensity = intensity

    def execute(self):
        self.light.intensity = self.intensity


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Tower(metaclass=SingletonMeta):
    def __init__(self):
        self.lights = {}
        self.commands = []

    def add_light(self, name, light):
        self.lights[name] = light

    def remove_light(self, name):
        del self.lights[name]

    def get_light(self, name):
        return self.lights[name]

    def add_command(self, command):
        self.commands.append(command)

    def execute_commands(self):
        while self.commands:
            self.commands.pop().execute()

    def __str__(self):
        s = "--- TOWER ---\n"
        for name in self.lights:
            s += str(name) + " = " + str(self.lights[name]) + "\n"
        return s


if __name__ == '__main__':
    t = Tower()
    t.add_light("Red", Light())
    t.add_light("Orange", Light())
    t.add_light("Green", Light())
    t.add_light("Stop", Light())

    c1 = SetLightIntensity(t.get_light("Red"), 0.5)
    c2 = SetLightIntensity(t.get_light("Orange"), 0.7)
    t.add_command(c1)
    t.add_command(c2)
    t.execute_commands()

    print(t)
