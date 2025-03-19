import unittest
from astre.astre import Astre
from astre.planet import Planet
from astre.distance import Distance

class TestAstrePlanet(unittest.TestCase):

    def setUp(self):
        self.soleil = Astre("Soleil", 1.3927e6)
        self.terre = Planet("Terre", 1.2756e4)
        self.mars = Planet("Mars", 6.779e3)
        self.lune = Planet("Lune", 3.474e3)

        self.longueur_tete = 0.22  #longeur de tête (m)

    def test_proportion_soleil_tete(self):
        proportion = self.soleil.get_proportion(self.longueur_tete / 1000)  
        print(f"Proportion Soleil/Tête: {proportion:.2e}")
        self.assertAlmostEqual(proportion, 6.33e9, delta=1e7) 

    def test_astre_add_planet(self):
        self.soleil.add_planet(self.terre)
        self.assertIn(self.terre, self.soleil.get_planets())
        self.assertEqual(self.terre.astre, self.soleil)

    def test_astre_remove_planet(self):
        self.soleil.add_planet(self.mars)
        self.soleil.remove_planet(self.mars)
        self.assertNotIn(self.mars, self.soleil.get_planets())
        self.assertIsNone(self.mars.astre)

    def test_planet_bonjour_with_astre(self):
        self.terre.astre = self.soleil
        self.assertEqual(self.terre.bonjour(), "Terre Soleil")

    def test_planet_bonjour_without_astre(self):
        self.assertEqual(self.mars.bonjour(), "Mars")

    def test_scale_down_planetes(self):
        proportion = self.soleil.get_proportion(self.longueur_tete / 1000)

        terre_scaled = self.terre.scale_down(proportion)
        mars_scaled = self.mars.scale_down(proportion)
        lune_scaled = self.lune.scale_down(proportion)

        # voir l'effet d'une mise à l'échelle égale
        print(f"Terre (scaled): {1000000 * terre_scaled:.2} mm")
        print(f"Mars (scaled): {1000000 * mars_scaled:.2} mm")
        print(f"Lune (scaled): {1000000 * lune_scaled:.2} mm")

        # Vérifier la diamètre Terre, Mars, Lune
        self.assertAlmostEqual(terre_scaled * 1000, 2.02e-3, delta=1e-4)  # Terre ~2mm
        self.assertAlmostEqual(mars_scaled * 1000, 1.07e-3, delta=1e-4)   # Mars ~1mm
        self.assertAlmostEqual(lune_scaled * 1000, 5.49e-4, delta=1e-5)   # Lune ~0.5mm

class TestDistance(unittest.TestCase):
    def setUp(self):
        self.scaler = Distance(1.3927e6, 0.00022)  # Ratio entre le diamètre du soleil et la longueur de la tête

    def test_scale_ratio(self):
        ratio = self.scaler.get_scale_ratio()
        print(f"scale ratio: {ratio:.2e}")
        self.assertAlmostEqual(ratio, 6.33e9, delta=1e7)

    def test_scaled_distances(self):
        distances_real = {
            'Soleil-Terre': 1.496e8,
            'Soleil-Mars': 2.2794e8,
            'Terre-Lune': 3.84404e5,
            'Soleil-Proxima Centauri': 4.017499e13
        }

        distances_scaled = {name: self.scaler.scale_distance(dist) for name, dist in distances_real.items()}

        # print distance après réduite
        for name, scaled_dist in distances_scaled.items():
            print(f"{name} (scaled): {scaled_dist:.2e} km")

        # Vérifier la distance Soleil-Terre, distance Soleil-Mars, distance Lune-Terre
        self.assertAlmostEqual(distances_scaled['Soleil-Terre'], 2.36e-2, delta=1e-3)  # 23.6 m
        self.assertAlmostEqual(distances_scaled['Soleil-Mars'], 3.60e-2, delta=1e-3)  # 36.0 m 
        self.assertAlmostEqual(distances_scaled['Terre-Lune'], 6.07e-5, delta=1e-6)   # 0.6 m
        self.assertAlmostEqual(distances_scaled['Soleil-Proxima Centauri'], 6.346e+3, delta=1)   # 6350 km


if __name__ == '__main__':
    unittest.main()