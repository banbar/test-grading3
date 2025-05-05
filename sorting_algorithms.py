from ds import *

def bubble_sort( theSeq ):
    if(isinstance(theSeq, list)):
        n = len( theSeq )
        for i in range( n - 1 ):
            for j in range( n-(i+1) ):
                if (theSeq[j] > theSeq[j+1]):
                    tmp = theSeq[j]
                    theSeq[j] = theSeq[j + 1]
                    theSeq[j + 1] = tmp
            #print(theSeq)
        return theSeq
    
        

def selection_sort( theSeq ):
    n = len( theSeq )
    for i in range( n - 1 ):
        smallNdx = i
        for j in range( i + 1, n ):
            if theSeq[j] < theSeq[smallNdx]:
                smallNdx = j
        if smallNdx != i:
            tmp = theSeq[i]
            theSeq[i] = theSeq[smallNdx]
            theSeq[smallNdx] = tmp
        print(theSeq)
    return theSeq

def insertion_sort( theSeq ):
    n = len( theSeq )
    for i in range( 1, n):
        value = theSeq[i]
        pos = i
        while pos > 0 and value < theSeq[pos - 1]:
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
        theSeq[pos] = value
        print(theSeq)
    return theSeq