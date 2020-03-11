class Chromossome:
    def __init__(self, geneticCode, generation):
        self.geneticCode = geneticCode
        self.fitness = 0
        self.generation = generation

    def setFitness(self, newFitness):
        self.fitness = newFitness

    def setProbability(self, newProbability):
        self.probability = newProbability
