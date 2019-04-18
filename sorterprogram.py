##
## This file is subject to the terms and conditions defined in
## file 'LICENSE.txt', which is part of this source code package.
##

import random, time
global comparisons
comparisons = 0


def selectionsort(array):
    global comparisons
    for i in range(len(array)):
        min_item = i

        for j in range(i+1, len(array)):
            if array[min_item] > array[j]:
                min_item = j
            comparisons += 1


        array[i], array[min_item] = array[min_item], array[i]
        print(array)
    print('Array sorted in ' + str(comparisons) + ' comparisons!')
    main()

def bubblesort(array):
    global comparisons
    while not in_order(array):
        
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
            print(array)
            comparisons += 1
    print('Array sorted in ' + str(comparisons) + ' comparisons!')
    main()
        
def bogosort(array):
    global comparisons
    global attempts
    attempts = 0
    while not in_order(array):
        random.shuffle(array)
        print(array)
        #time.sleep(1)
        attempts += 1
    print('Array sorted in ' + str(comparisons) + ' comparisons!')
    main()


def in_order(array):
    global comparisons
    if not array:
        return True
    last = array[0]
    for x in array[1:]:
        if x < last:
            return(False)
        last = x
        comparisons += 1
    return(True)
    
                 
def makeArray(length, maxval):
    global comparisons
    tosort = []
    for i in range(length):
        x = random.randint(0,maxval)
        tosort.append(x)
    print(tosort)
    return(tosort)
    print(
    '''

    ------------

    ''')
def main():
    comparisons = 0
    print(
'''

---o SorterProgram Version 0.8 o---
(C) 2019 NoiseGenerator

''')
    manual = input('Enter \'MANUAL\' for manual input or press ENTER to continue with random array generation.\n>>>  ').lower()
    
    if manual != 'manual':
        size = input('''
Size of array:
>>> ''')
        randval = input('''
Size of items in array:
>>> ''')
        final_array = makeArray(int(size), int(randval))    


    if manual == 'manual':
        broken_array = input('Enter your array. Split items with commas.\n>>>  ')
        try:
            final_array = [x.strip() for x in broken_array.split(',')]
            final_array = [int(x) for x in final_array]
            print(final_array)
        except:
            print('Please enter only valid whole integers.')
            main()

    to_sort = input('''
Choose a type of sort:

1) Bubble Sort
2) Bogosort
3) Selection Sort

>>> ''')
    if to_sort == '1':
        bubblesort(final_array)
    elif to_sort == '2':
        bogosort(final_array)
    elif to_sort == '3':
        selectionsort(final_array)
    else:
        print('Not a type.')
    
main()
