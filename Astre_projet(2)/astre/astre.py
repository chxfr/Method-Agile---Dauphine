class Astre:
    def __init__(self, nom, diameter):
        self.nom = nom 
        self.diameter = diameter  # diamètre
        self.planets = []

    def get_proportion(self, other_length):
        #proportion
        return self.diameter / other_length

    def scale_down(self, proportion):
        # diamètres planétaires réduits
        return self.diameter / proportion
    
    def add_planet(self, planet):
        if planet not in self.planets:
            self.planets.append(planet)
            planet.astre = self

    def remove_planet(self, planet):
        if planet in self.planets:
            self.planets.remove(planet)
            planet.astre = None

    def get_planets(self):
        return self.planets
