class Pistol(object):
    def __init__(self, name, soldier):
        self.bullets_left = 18
        self.name = name
        self.clip = True
        self.soldier = soldier
        self.safety_lever = False

    def push_trigger(self):
        self.bullets_left -= 1
        self.clip = True
        self.safety_lever = True
        print(" I now have", self.bullets_left, "bullets left in my clip")

    def reload(self):
        self.bullets_left = 30
        self.magazine = True


print("Ive reloaded my pistol, Now i have 18 bullets in my clip")


gun = Pistol(name =Pistol, soldier=True)
gun.push_trigger()
gun.push_trigger()
gun.push_trigger()
gun.push_trigger()
gun.push_trigger()
gun.push_trigger()
gun.push_trigger()
gun.push_trigger()
gun.push_trigger()
gun.push_trigger()
gun.push_trigger()
gun.push_trigger()
gun.push_trigger()
gun.reload()


