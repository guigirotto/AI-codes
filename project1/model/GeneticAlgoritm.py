class GeneticAlgoritm:

    currentChromossomeList = []
    bestChromossome = ""


    def __init__(self, chromossomeSize, populationSize, crossingProbability,
     mutationProbability,methodOfSelection, elitismSize,
      quantityOfCrossing, quantityOfGeneration):
        self.populationSize = int(populationSize)
        self.crossingProbability = int(crossingProbability)
        self.mutationProbability = int(mutationProbability)
        self.elitismSize = int(elitismSize)
        self.quantityOfCrossing = int(quantityOfCrossing)
        self.quantityOfGeneration = int(quantityOfGeneration)
        self.chromossomeSize = int(chromossomeSize)
        self.methodOfSelection = int(methodOfSelection)
        self.minSpanX = -3.1
        self.maxSpanX = 12.1
        self.minSpanY = 4.1
        self.minSpanY = 5.8

    def setTournmentSize(self, tournmentSize):
        self.tournmentSize = int(tournmentSize)

    def getConvertionFromBinaryToRealX(self, numberOnBaseTen):
        numberConverted = self.minSpanX + ((self.maxSpanX - self.minSpanX)/(2^self.chromossomeSize - 1))* int(numberOnBaseTen, 2)
        return numberConverted
    
    def getConvertionFromBinaryToRealY(self, numberOnBaseTen):
        numberConverted = self.minSpanY + ((self.maxSpanY - self.minSpanY)/(2^self.chromossomeSize - 1))* int(numberOnBaseTen, 2)
        return numberConverted
