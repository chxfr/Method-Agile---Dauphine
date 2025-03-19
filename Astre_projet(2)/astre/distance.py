# distance.py
class Distance:
    def __init__(self, reference_length_real, reference_length_scaled):
        self.reference_length_real = reference_length_real
        self.reference_length_scaled = reference_length_scaled
        self.scale_ratio = self.reference_length_real / self.reference_length_scaled

    def scale_distance(self, real_distance):
        return real_distance / self.scale_ratio

    def get_scale_ratio(self):
        return self.scale_ratio
