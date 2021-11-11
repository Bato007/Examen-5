class Machine(object):
    def __init__(self, parts):
        self.states = parts['states'] 
        self.iAlphabet = parts['iAlphabet']
        self.cAlphabet = parts['cAlphabet']
        self.transitions = parts['transitions']
        self.start = parts['start']
        self.acceptance = parts['acceptance']
        self.reject = parts['reject']

    def __str__(self):
        machine = 'states: {0}\niAlphabet: {1}\ncAlphabet: {2}\ntransitions: {3}\nstart: {4}\nacceptance: {5}\nreject: {6}'.format(str(self.states), str(self.iAlphabet), str(self.cAlphabet), str(self.transitions), str(self.start), str(self.acceptance), str(self.reject))
        return machine

