class Scales:
    def __init__(self):
        self.massa_right = 0
        self.massa_left = 0

    def add_right(self, massa_kg):
        self.massa_right += massa_kg

    def add_left(self, massa_kg):
        self.massa_left += massa_kg

    def get_result(self):
        if self.massa_right == self.massa_left:
            return 'Весы в равновесии'

        elif self.massa_right > self.massa_left:
            return 'Правая чаша тяжелее'

        return 'Левая чаша тяжелее'


scales = Scales()

scales.add_right(3)
scales.add_left(4)

print(scales.get_result())
