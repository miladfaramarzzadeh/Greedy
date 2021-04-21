# Greedy
Knapsack(OOP)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 14:44:17 2021

@author: milad
"""

class Item():

    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def __str__(self):
        result = ' < ' + self.name + ' , ' + str(self.value) + ' , ' + str(self.weight) + ' > '
        return result

def value(item):
    return item.getValue()

def weightInverse(item):
    return 1.0/item.getWeight()

def density(item):
    return item.getValue()/item.getWeight()

def OurItems():
    names = ['watch', 'radio', 'book', 'folwer', 'picture', 'glass']
    values = [120, 20, 20, 80, 150, 64]
    weights = [6, 1, 5, 10, 15, 8]
    Items = []
    for i in range(len(values)):
        Items.append(Item(names[i], values[i], weights[i]))
    return Items

def greedy(items, maxWeight, keyFunction):
    sortedItems = sorted(items, key = keyFunction, reverse = True)
    result = []
    totalValue = 0.0
    totalWeight = 0.0
    for i in range(len(sortedItems)):
        if (totalWeight + sortedItems[i].getWeight()) <= maxWeight:
            result.append(sortedItems[i])
            totalWeight += sortedItems[i].getWeight()
            totalValue += sortedItems[i].getValue()
    return (result, totalValue)

def greedytest(items, constraint, keyFunction):
    res, val = greedy(items, constraint, keyFunction)
    print('Total Value  = ', val)
    for item in res:
        print(' ', item)

maxWeight = 15
items = OurItems()
print('filling the knapsack according to Value: ', maxWeight)
greedytest(items, maxWeight, value)
print('filling the knapsack according to inverseweight:  ', maxWeight)
greedytest(items, maxWeight, weightInverse)
print('filling the knapsack according to density : ', maxWeight)
greedytest(items, maxWeight, density)

   
   
