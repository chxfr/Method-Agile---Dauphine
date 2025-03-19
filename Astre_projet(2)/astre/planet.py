class Planet:
    def __init__(self, name, diameter, astre=None):
        self.name = name
        self.astre = astre
        self.diameter = float(diameter)

    def bonjour(self):
        if self.astre:
            return f"{self.name} {self.astre.nom}"
        return self.name


    def scale_down(self, proportion):
        # diamètres planétaires réduits
        print(float(1000000000 *(self.diameter / proportion)))
        return float(1000000000 *(self.diameter / proportion))