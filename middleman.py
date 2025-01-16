class Middleman:

    def __init__(self):
        pass

    def sort(self, inputList):
        from looper import Looper

        loopObj = Looper()
        res = []

        notDone = True
        while notDone:
            notSorted = loopObj.NotSorted(res)
            if res == []:
                res = loopObj.LoopOnce(inputList)
            elif notSorted == False:
                notDone = False
            else:
                res = loopObj.LoopOnce(res)
        return res