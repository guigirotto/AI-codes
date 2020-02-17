class Chromossome:

    def __init__(self, geneticCode):
        self.geneticCode = geneticCode
        self.fitness = 0

    def setFitness(self, newFitness):
        self.fitness = newFitness

    def setProbability(self,newProbability):
        self.probability = newProbability