def last(n):
    return n[-1]

def sort(tuples):
    return sorted(tuples,key=last)
a=[(2,5),(1,2),(4,4),(2,3),(2,1)]
print("sorted:")
print(sort(a))