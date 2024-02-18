class Point():
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.interpolated_value = None
        self.error = 0
    def set_interpolated_value(self, interpolated_value):
        self.interpolated_value = interpolated_value
        self.error = abs((self.interpolated_value - self.value) / self.value)**2
    def __lt__(self, other):
        return self.error < other.error
    def __str__(self):
        return 'p(' + str(self.x) + ',' + str(self.y) + ',' + str(self.value) + ')'