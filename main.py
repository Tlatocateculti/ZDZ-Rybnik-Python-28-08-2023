menuDict = {1: ("add", "Dodawanie"), 9: ('end', "Koniec"),
            2: ("sub", "Odejmowanie"), 5: ("pow", "Potęgowanie"), 3: ("mul", "Mnożenie"),
            4: ('div', 'Dzielenie'), 6: ('mod', 'Modulo'), 7: ('ord', 'Ciąg arytmetyczny'),
            8: ('fib', 'Ciąg Fibonacciego')}

def fib(x):
    fibRet = [0, 1]
    for i in range(1,x+1):
        fibRet.append(fibRet[i]+fibRet[i-1])
    return fibRet

def adding(x, addNegative=True):
    sum = 0
    for val in x:
        if (not addNegative and val > 0) or addNegative:
            sum += val
    return sum

#def adding(*x, addNegative=True):
#    inList = []
#    for i in x:
#        inList.append(i)
#    return adding(inList, addNegative)
    #sum = 0
    #for val in x:
    ##    if ((not addNegative and val > 0) or addNegative):
    #        sum+=val
    #return sum



while(True):
    print("Menu Programu",)

    tmpDict = {}
    for menu in menuDict:
        tmpDict[menu] = menuDict[menu][1]
    tmpKeys = list(tmpDict.keys())
    tmpKeys.sort()

    for menuKey in tmpKeys:
        print(f'{menuKey}.{tmpDict[menuKey]}')
    choose = int(input("Wprowadź dowolną wartość: "))

    match(menuDict[choose][0]):
        case 'add': #print(adding(8,6,5,23,-90,-100,11,12,0, addNegative=False))
            inList = []
            while True:
                inList.append(float(input("Podawaj kolejne wartości, podanie zero spowoduje wyliczenie sumy: ")))
                if inList[-1] == 0:
                    break
            inList.sort()
            print(inList[::-1])
            print(inList)
            print(max(inList), min(inList), inList.count(12), len(inList))
            #rint(adding(inList))
        case 'end': break
        case 'ord': print([x+y for x in range(2) for y in range(2,5)])
        case 'fib': print(fib(int(input("Podaj ostatni element w ciągu: "))))
        case other: print("Nie znam takiej pozycji")
print("Koniec programu")
