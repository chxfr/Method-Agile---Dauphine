class Planet:
    def __init__(self, name, diametre, astre=None):
        self.name = name
        self.astre = astre
        self.diametre = diametre  #diametre(km)

    def bonjour(self):
        if self.astre:
            return f"{self.name} {self.astre.nom}"
        return self.name


    def scale_down(self, proportion):
        # diamètres planétaires réduits
        return float(1000000 *(self.diametre / proportion))