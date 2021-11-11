from machine import *
import json

def loadMachine(file='parts'):
    with open(file + '.json', 'r') as outline:
        return json.load(outline)

def main():
    machine = Machine(loadMachine())
    chain = input('Ingrese la cadena a evaluar: ')


if __name__ == '__main__':
    main()
