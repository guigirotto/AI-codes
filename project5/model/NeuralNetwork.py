class NeuralNetwork:

    

    def __init__(
        self,
        stop_type = 0,
        max_error = 0,
        learning_rate = 0,
        max_cycles = 0,
        actual_cycle = 0,
        interaction_type=0
    ):

        self. stop_type = int(stop_type)
        self.max_error = float(max_error)
        self.learning_rate = float(learning_rate)
        self.max_cycles = int(max_cycles)
        self.actual_cycle = int(actual_cycle)
        self.interaction_type= int (interaction_type)
    