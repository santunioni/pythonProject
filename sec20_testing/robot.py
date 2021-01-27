class Robot:

    def __init__(self, name, battery=100, skills=[]):
        self.__name = name
        self.__battery = battery
        self.__skills = skills

    @property
    def name(self):
        return self.__name

    @property
    def battery(self):
        return self.__battery

    @property
    def skills(self):
        return self.__skills

    def charge(self):
        self.__battery = 100

    def say_name(self):
        if self.__battery > 0:
            self.__battery -= 1
            return f"BEEP BOOP BEEP BOOP. I AM {self.__name.upper()}"
        return "Low battery. Please recharge and try again."

    def learn_skill(self, new_skill, battery_cost):
        if self.__battery >= battery_cost:
            self.__skills.append(new_skill)
            return f"Wow! I LEARNED {new_skill}"
        else:
            return "Low battery. Please recharge and try again."
