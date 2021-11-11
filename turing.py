from machine import *
import json

def loadMachine(file='parts'):
    with open(file + '.json', 'r') as outline:
        return json.load(outline)

def main():
    MAX_ITERATIONS = 20000
    iteration = 0
    toTxt = []
    machine = Machine(loadMachine())
    # chain = input('Ingrese la cadena a evaluar: ')
    chain = 'aa'
    start = machine.loadChain(chain)
    flag = True
    toTxt.append((str(start) + chain + '\n'))

    while flag and iteration < MAX_ITERATIONS:
        flag, index, target, string = machine.move()
        if flag: 
            string.insert(index, target['finish'])
            res = ''.join(string)
            toTxt.append(res+'\n')
        iteration += 1
        if 0 == iteration%100:
            print(iteration)

    if (iteration == MAX_ITERATIONS): toTxt.append('LOOP')

    with open('result.txt', 'w') as file:
        file.writelines(toTxt)

if __name__ == '__main__':
    main()
