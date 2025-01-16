class Looper:

    def __init__(self):
        pass

    def NotSorted(self, inputList):
        if inputList != []:
            for i in range(len(inputList)):
                if i == 0:
                    pass
                else:
                    current = inputList[i]
                    prev = inputList[i - 1]
                    if current < prev:
                        return True
            return False
        else:
            return False

    def LoopOnce(self, inputList):
        for i in range(len(inputList)):
            if i < len(inputList) - 1:
                if inputList[i] > inputList[i + 1]:
                    for i in range(len(inputList)):
                        if i != 0 or i != len(inputList) + 1:
                            current = inputList[i]
                            prev = inputList[i - 1]
                            if current < prev:
                                inputList.pop(i)
                                inputList.insert(0, current)
        return inputList

