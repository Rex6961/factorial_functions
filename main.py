# two options how calculate a factorial
import time

#This is wrapper calculate time complete calculate factorial functions
def calculateTimeCompleteFactorial(func):
    def wrapper(*args):
        start = time.time()
        print(func(*args))
        end = time.time() - start
        return end
    return wrapper

#This is iteration factorial function
@calculateTimeCompleteFactorial
def calculateIteratedFactorialFunction(number):
    factorialValue = 1
    for i in range(1, number + 1):
        factorialValue *= i
    return factorialValue

#This is recursive factorial function
factorialValue = 1
@calculateTimeCompleteFactorial
def calculateRecursivedFactorialFunction(number):
    global factorialValue
    if number == 1:
        return
    else:
        factorialValue *= number
        calculateRecursivedFactorialFunction(number - 1)
    return factorialValue

#This is example iteration factorial function sees how running
# recursive factorial function
def factorialStack(number):
    callStack = []
    callStack.append({'returnAddr': 'start', 'number': number})

    returnValue = None

    while len(callStack) > 0:
        number = callStack[-1]['number']
        returnAddr = callStack[-1]['returnAddr']

        if returnAddr == 'start':
            if number == 1:
                returnValue = 1
                callStack.pop()
                continue
            else:
                callStack[-1]['returnAddr'] = 'after recursive call'
                callStack.append({'returnAddr': 'start', 'number': number - 1})
                continue
        elif returnAddr == 'after recursive call':
            returnValue = number * returnValue
            callStack.pop()
            continue
    return returnValue


def main():
    number = int(input('Enter number !factorial (min value = 1, max value = 465) '))
    factorialIterationValue = calculateTimeCompleteFactorial(calculateIteratedFactorialFunction)
    factorialRecursiveValue = calculateTimeCompleteFactorial(calculateRecursivedFactorialFunction)

    print(f'\nfactorial({number}) = {factorialStack(number)},\n\
runningTimeOfIterativeFactorialFunction = {factorialIterationValue(number)},\n\
runningTimeOfRecursiveFactorialFunction = {factorialRecursiveValue(number)}')


if __name__ == '__main__':
    main()
