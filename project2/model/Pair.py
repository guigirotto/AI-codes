class Pair:
    def __init__(self, pair_id=None, employee_1=0, employee_2=0, last_shift=-10):
        self.pair_id = pair_id
        self.employee_1 = employee_1
        self.employee_2 = employee_2
        self.last_shift = last_shift

    def set_last_shift(self, last_shift):
        self.last_shift = last_shift
