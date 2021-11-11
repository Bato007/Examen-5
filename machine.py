class Machine(object):
    def __init__(self, parts):
        self.__finished__ = False
        self.__states__ = parts['states'] 
        self.__iAlphabet__ = parts['iAlphabet']
        self.__cAlphabet__ = parts['cAlphabet']
        self.__transitions__ = parts['transitions']
        self.__start__ = parts['start']
        self.__acceptance__ = parts['acceptance']
        self.__reject__ = parts['reject']
        self.__chain__ = []
        self.__head__ = [0, self.__start__]

    def __str__(self):
        machine = 'states: {0}\niAlphabet: {1}\ncAlphabet: {2}\ntransitions: {3}\nstart: {4}\nacceptance: {5}\nreject: {6}'.format(str(self.__states__), str(self.__iAlphabet__), str(self.__cAlphabet__), str(self.__transitions__), str(self.__start__), str(self.__acceptance__), str(self.__reject__))
        return machine

    def __left__(self, next):
        if self.__head__[0] == 0: return    # No se puede ir antes
        self.__head__ = [self.__head__[0] - 1, next['finish']]

    def __right__(self, next):
        if self.__head__[0] == len(self.__chain__) - 1:
            self.__chain__.append(' ')
        self.__head__ = [self.__head__[0] + 1, next['finish']]

    def loadChain(self, chain):
        self.__chain__ = [letter for letter in chain]
        self.__head__ = [0, self.__start__]
        return self.__start__

    # Moves the turing 
    def move(self):
        if self.__finished__: return [False, self.__head__[0], self.__head__[1], self.__chain__]
        next = None

        # Verificando a donde se debe de mover
        for transition in self.__transitions__:
            if (transition['start'] == self.__head__[1]) and (transition['alph'] == self.__chain__[self.__head__[0]]):
                next = transition

        if (next):
            if (next['finish'] == self.__acceptance__) or (next['finish'] == self.__reject__): 
                self.__finished__ = True

            if (next['direction'] == 'L'): 
                self.__left__(next)
            else: 
                self.__right__(next)

        return [True, self.__head__[0], next, self.__chain__[:]]
